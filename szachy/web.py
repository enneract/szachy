import argparse
from collections import defaultdict
from typing import Dict, List, Tuple

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from szachy.chess import Game, Score, Tournament, compute_ratings, compute_ranking, elo_expected_score
from szachy.database import Termination


def _abbreviate_name(name: str) -> str:
    parts = name.split(' ')
    return ''.join(f'{part[0]}. ' for part in parts[:-1]) + parts[-1]


def _make_initials(name: str) -> str:
    parts = name.split(' ')
    return ''.join(f'{part[0]}. ' for part in parts)


def _format_score(score: int) -> str:
    return (str(score // 2) if score != 1 else '') + ('½' if score % 2 == 1 else '')


class GameView:
    def __init__(self, game: Game) -> None:
        self.gid = game.gid
        self.white = _abbreviate_name(game.white)
        self.black = _abbreviate_name(game.black)
        self.score = {0: '0-1', 1: '½-½', 2: '1-0'}[game.score]


class ScoreView:
    def __init__(self, score: Score, ranked: bool) -> None:
        self.games_played = score.games_played
        self.actual = _format_score(score.actual)

        if not ranked:
            self.adjustment = 'N.R.'
        elif score.adjustment >= 0:
            self.adjustment = f'+{score.adjustment}'
        else:
            self.adjustment = f'\N{EN DASH}{-score.adjustment}'


class TournamentView:
    def __init__(self, tournament: Tournament) -> None:
        self.date = tournament.date
        self.location = tournament.location
        self.games = [GameView(game) for game in tournament.games]
        self.ranked = tournament.ranked

        self.ranking = [
            (
                _abbreviate_name(name),
                tournament.initial_ratings[name],
                ScoreView(score, tournament.ranked)
            )
            for rank, name, score
            in compute_ranking(tournament.scores, lambda scores: scores.adjustment)
        ]


class GameDetailedView(GameView):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self.termination = {
            Termination.RESIGNATION: 'rezygnacja',
            Termination.CHECKMATE: 'szach mat',
            Termination.STALEMATE: 'pat',
        }[game.termination]

        self.chess_com_embed = game.chess_com_embed
        self.pgn = game.pgn


class PlannerView:
    def __init__(self, ratings: Dict[str, int], tournaments: List[Tournament]) -> None:
        players = [*ratings.keys()]
        names = [*map(_abbreviate_name, players)]
        self.initials = [*map(_make_initials, players)]

        game_counts: Dict[str, int] = defaultdict(int)
        for tournament in tournaments:
            for game in tournament.games:
                game_counts[game.white] += 1
                game_counts[game.black] += 1

        self.least_played = [
            (player, count)
            for rank, player, count in compute_ranking(game_counts, lambda x: -x)
        ]

        def probability(a: str, a_rating: int, b: str, b_rating: int) -> str:
            if a == b:
                return ''

            score = elo_expected_score(a_rating, b_rating)
            return f'{50 * score:.0f}'

        probability_matrix = [
            [
                probability(a, a_rating, b, b_rating)
                for b, b_rating in ratings.items()
            ]
            for a, a_rating in ratings.items()
        ]
        self.names_and_probabilities = zip(names, probability_matrix)

        color_counts = [[0 for b in ratings] for a in ratings]
        for tournament in tournaments:
            for game in tournament.games:
                i = players.index(game.white)
                j = players.index(game.black)
                color_counts[i][j] += 1
                color_counts[j][i] -= 1

        self.unpaired_games: List[Tuple[str, str, int]] = []
        for i, row in enumerate(color_counts):
            for j, count in enumerate(row):
                if count <= 0:
                    continue
                self.unpaired_games.append((
                    names[i],
                    names[j],
                    count,
                ))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--webroot', type=str, default='')
    args = parser.parse_args()

    webroot = args.webroot

    routes = web.RouteTableDef()
    routes.static(f'{webroot}/static', 'static')

    environment = Environment(loader=FileSystemLoader('templates/'), autoescape=True)
    tpl_header_footer = environment.get_template('header_footer.html')
    tpl_index = environment.get_template('index.html')
    tpl_game = environment.get_template('game.html')
    tpl_style = environment.get_template('style.css')
    tpl_planner = environment.get_template('planner.html')

    ratings, tournaments, total_scores = compute_ratings()

    ranked_ratings = {
        player: rating
        for player, rating in ratings.items()
        if total_scores[player].games_played >= 10
    }

    elo_ranking = [*compute_ranking(ranked_ratings, lambda rating: rating)]

    unranked_ratings = {
        player: rating
        for player, rating in ratings.items()
        if total_scores[player].games_played < 10
    }

    unranked_listing = [
        (player, rating)
        for rank, player, rating in
        compute_ranking(unranked_ratings, lambda rating: rating)
    ]

    games_by_gid = {
        game.gid: game
        for tournament in tournaments
        for game in tournament.games
    }

    @routes.get(webroot)
    @routes.get(f'{webroot}/')
    async def index(request: web.Request) -> web.Response:
        tournament_summaries = [*map(TournamentView, tournaments)]
        content = tpl_index.render(
            webroot=webroot,
            elo_ranking=elo_ranking,
            unranked_listing=unranked_listing,
            total_scores=total_scores,
            tournaments=tournament_summaries,
        )
        text = tpl_header_footer.render(webroot=webroot, content=content)
        return web.Response(text=text, content_type='text/html')

    @routes.get(f'{webroot}/gra/{{gid}}')
    async def game_details(request: web.Request) -> web.Response:
        try:
            game = games_by_gid[int(request.match_info['gid'])]
        except ValueError:
            raise web.HTTPBadRequest
        except KeyError:
            raise web.HTTPNotFound

        content = tpl_game.render(webroot=webroot, game=GameDetailedView(game))
        text = tpl_header_footer.render(webroot=webroot, content=content)
        return web.Response(text=text, content_type='text/html')

    @routes.get(f'{webroot}/planer')
    async def planner(request: web.Request) -> web.Response:
        content = tpl_planner.render(webroot=webroot, planner=PlannerView(ratings, tournaments))
        text = tpl_header_footer.render(webroot=webroot, content=content)
        return web.Response(text=text, content_type='text/html')

    @routes.get(f'{webroot}/style.css')
    async def style(request: web.Request) -> web.Response:
        text = tpl_style.render(webroot=webroot)
        return web.Response(text=text, content_type='text/css')

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=args.host, port=args.port)
