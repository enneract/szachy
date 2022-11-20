"""
Elo ratings and tournament rankings.
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, TypeVar, Union
import datetime

from szachy.database import TOURNAMENTS, Termination

STARTING_RATING = 400
MINIMUM_RATING = 100
K_FACTOR = 32

T = TypeVar('T')
Number = Union[int, float]  # numbers.Number is broken


@dataclass(frozen=True)
class Game:
    gid: int
    white: str
    white_rating: int
    black: str
    black_rating: int
    pgn: str
    score: int
    termination: Termination
    chess_com_embed: Optional[int]


class Score:
    """
    Total score for a given player in a given tournament.
    """
    games_played: int = 0
    actual: int = 0
    expected: float = 0.0  # Expected score based on Elo ratings
    adjustment: int = 0

    def __float__(self) -> float:
        return self.actual / 2 / self.games_played

    def __eq__(self, other: Any) -> bool:
        assert isinstance(other, Score)
        return float(self) == float(other)


class TotalScore:
    """
    Total score for a given player in all tournaments.
    """
    wins: int = 0
    draws: int = 0
    losses: int = 0


@dataclass(frozen=True)
class Tournament:
    date: datetime.date
    location: str
    games: List[Game]
    ranked: bool
    initial_ratings: Dict[str, int]
    scores: Dict[str, Score]


def elo_expected_score(white_rating: int, black_rating: int) -> float:
    return 2 / (1 + 10 ** ((black_rating - white_rating) / 400))


def elo_adjust_rating(rating: int, score: Score) -> int:
    adjustment = K_FACTOR * (score.actual - score.expected) / 2
    new_rating = max(MINIMUM_RATING, int(round(rating + adjustment)))
    score.adjustment = new_rating - rating
    return new_rating


def compute_ratings() -> Tuple[Dict[str, int], List[Tournament], Dict[str, TotalScore]]:
    ratings: Dict[str, int] = defaultdict(lambda: STARTING_RATING)
    tournaments: List[Tournament] = []
    total_scores: Dict[str, TotalScore] = defaultdict(TotalScore)

    for tournament in TOURNAMENTS:
        initial_ratings: Dict[str, int] = {}
        scores: Dict[str, Score] = defaultdict(Score)
        games: List[Game] = []

        for game in tournament.games:
            scores[game.white].games_played += 1
            scores[game.black].games_played += 1

            scores[game.white].actual += game.score
            scores[game.black].actual += 2 - game.score

            match game.score:
                case 0:
                    total_scores[game.white].losses += 1
                    total_scores[game.black].wins += 1
                case 1:
                    total_scores[game.white].draws += 1
                    total_scores[game.black].draws += 1
                case 2:
                    total_scores[game.white].wins += 1
                    total_scores[game.black].losses += 1

            expected_score = elo_expected_score(ratings[game.white], ratings[game.black])
            scores[game.white].expected += expected_score
            scores[game.black].expected += 2 - expected_score

            initial_ratings[game.white] = ratings[game.white]
            initial_ratings[game.black] = ratings[game.black]

            games.append(Game(
                game.gid,
                game.white,
                ratings[game.white],
                game.black,
                ratings[game.black],
                game.pgn,
                game.score,
                game.termination,
                game.chess_com_embed,
            ))

        if tournament.ranked:
            for player, score in scores.items():
                ratings[player] = elo_adjust_rating(ratings[player], score)

        tournaments.append(Tournament(
            tournament.date,
            tournament.location,
            games,
            tournament.ranked,
            initial_ratings,
            scores,
        ))

    return ratings, tournaments, total_scores


def compute_ranking(dct: Dict[str, T], key: Callable[[T], Number]) -> Iterator[Tuple[int, str, T]]:
    lst = sorted(dct.items(), key=lambda kv: (-key(kv[1]), kv[0]))

    rank = 1
    last_value = lst[0][1]
    yield rank, *lst[0]

    for player, value in lst[1:]:
        if value != last_value:
            rank += 1
            last_value = value

        yield rank, player, value
