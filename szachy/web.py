import argparse
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Tuple

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from szachy.chess import Game, Score, Tournament, compute_ratings, compute_ranking
from szachy.database import Termination

PlayerPair = Tuple[str, str]


def _abbreviate_name(name: str) -> str:
    parts = name.split(' ')
    return ''.join(f'{part[0]}. ' for part in parts[:-1]) + parts[-1]


def _format_score(score: int) -> str:
    return (str(score // 2) if score != 1 else '') + ('½' if score % 2 == 1 else '')


def _make_player_pair(game: Game) -> PlayerPair:
    return tuple(sorted((game.white, game.black)))


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
                rank,
                _abbreviate_name(name),
                tournament.initial_ratings[name],
                ScoreView(score, tournament.ranked)
            )
            for rank, name, score
            in compute_ranking(tournament.scores, lambda scores: float(scores))
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


# class PairGameView:
#     def __init__(self, player_a: str, player_b: str, game: Game) -> None:
#         # FIXME: simplify
#         if player_a == game.white:
#             self.color_a = 'white'
#             self.score_a = {0: '0', 1: '½', 2: '1'}[game.score]
#             self.color_b = 'black'
#             self.score_b = {0: '1', 1: '½', 2: '0'}[game.score]
#         else:
#             self.color_a = 'black'
#             self.score_a = {0: '1', 1: '½', 2: '0'}[game.score]
#             self.color_b = 'white'
#             self.score_b = {0: '0', 1: '½', 2: '1'}[game.score]
#


@dataclass(frozen=True)
class PairGameView:
    color_a: str
    score_a: str
    color_b: str
    score_b: str


@dataclass(frozen=True)
class PairView:
    player_a: str
    player_b: str
    games: List[PairGameView]
    total_a: str
    total_b: str


class TournamentDetailedView(TournamentView):
    def __init__(self, tournament: Tournament) -> None:
        super().__init__(tournament)

        raw_pairs: Dict[PlayerPair, List[Game]] = defaultdict(list)
        for game in tournament.games:
            raw_pairs[_make_player_pair(game)].append(game)

        self.pairs: List[PairView] = []
        for pair, raw_games in raw_pairs.items():
            player_a, player_b = pair

            games: List[PairGameView] = []
            total_a = 0
            total_b = 0

            for game in raw_games:
                # FIXME: simplify
                if player_a == game.white:
                    color_a = 'white'
                    score_a = game.score
                    color_b = 'black'
                    score_b = 2 - game.score
                else:
                    color_a = 'black'
                    score_a = 2 - game.score
                    color_b = 'white'
                    score_b = game.score

                games.append(PairGameView(
                    color_a,
                    _format_score(score_a),
                    color_b,
                    _format_score(score_b),
                ))

                total_a += score_a
                total_b += score_b

            self.pairs.append(PairView(
                player_a,
                player_b,
                games,
                _format_score(total_a),
                _format_score(total_b),
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
    tpl_tournament = environment.get_template('tournament.html')
    tpl_style = environment.get_template('style.css')

    ratings, tournaments, total_scores = compute_ratings()
    elo_ranking = [*compute_ranking(ratings, lambda rating: rating)]

    tournaments_by_tid = {
        tournament.tid: tournament
        for tournament in tournaments
    }

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

    @routes.get(f'{webroot}/turniej/{{tid}}')
    async def tournament_details(request: web.Request) -> web.Response:
        try:
            tournament = tournaments_by_tid[int(request.match_info['tid'])]
        except ValueError:
            raise web.HTTPBadRequest
        except KeyError:
            raise web.HTTPNotFound

        content = tpl_tournament.render(webroot=webroot, tournament=TournamentDetailedView(tournament))
        text = tpl_header_footer.render(webroot=webroot, content=content)
        return web.Response(text=text, content_type='text/html')

    @routes.get(f'{webroot}/style.css')
    async def style(request: web.Request) -> web.Response:
        tpl_style = environment.get_template('style.css') # DEBUG
        text = tpl_style.render(webroot=webroot)
        return web.Response(text=text, content_type='text/css')

    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=args.host, port=args.port)
