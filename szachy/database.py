"""
This file contains raw game and tournament data. The objects contain immutable
data, to be considered as historical facts.
"""
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List, Optional


class Termination(Enum):
    RESIGNATION = 1
    CHECKMATE = 2
    STALEMATE = 3


@dataclass(frozen=True)
class GameData:
    gid: int
    white: str
    black: str
    pgn: str
    score: int  # Doubled to avoid floats (0 - Black wins, 1 - draw, 2 - White wins)
    termination: Termination
    chess_com_embed: Optional[int]  # FIXME: move elsewhere (and automate)


@dataclass(frozen=True)
class TournamentData:
    date: date
    location: str
    games: List[GameData]
    ranked: bool = True


# TODO: this will be replaced with a proper SQL database once it grows big enough.
TOURNAMENTS = [
    TournamentData(
        date=date(2022, 11, 5),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=5,
                white='Piżama',
                black='Pion Forward',
                pgn='''1. Nh3 f5 2. e3 Nf6 3. Bd3 e6 4. b3 Bb4 5. c3 Bd6 6. Bb2 b6 7. c4 Nc6 8. Ng5 Nb4 9. a3 Nxd3+ 10. Ke2 Nxb2 11. Qc2 Be5 12. f4 Bd6 13. Qxb2 Bb7 14. h4 h6 15. Nf3 O-O 16. Nc3 Ng4 17. Rh3 e5 18. fxe5 Bxe5 19. Nxe5 Nxe5 20. d4 Bxg2 21. Rg3 Qxh4 22. Rxg2 Ng4 23. Nb5 d5 24. Nxc7 Rac8 25. Na6 Qh3 26. Rgg1 Qh2+ 27. Rg2 Qxg2+ 28. Kd3 Qxb2 29. Rh1 Qxa3 30. cxd5 Qxb3+ 31. Kd2 Nxe3 32. Rh3 Rc2+ 33. Ke1 Qb1#''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9680141,
            ),
            GameData(
                gid=6,
                white='Fryderyk Szopen',
                black='Kubik',
                pgn='''1. Na3 Nc6 2. g4 b6 3. Nf3 Bb7 4. g5 d6 5. c3 Ne5 6. Nd4 Bxh1 7. f4 Ng4 8. h3 Nh2 9. Nc6 Qd7 10. Nd4 Qd8 11. e3 c5 12. Bb5+ Bc6 13. Bxc6+ Qd7 14. b4 Rc8 15. e4 Rxc6 16. Nxc6 Qxc6 17. d3 g6 18. b5 Qc8 19. f5 gxf5 20. exf5 Qxf5 21. Qd2 Nf3+ 22. Ke2 Nxd2 23. Kxd2 Qxh3 24. d4 f6 25. gxf6 Bh6+ 26. Kc2 Nxf6 27. Nc4 Rg8 28. dxc5 Rg2+ 29. Nd2 dxc5 30. c4 Bxd2 31. Bxd2 Ng4 32. Re1 Ne3+ 33. Kd3 Nd5+ 34. Be3 Rxa2 35. Ke4 e6 36. Ke5 Ke7 37. Bg5+ Kd7 38. cxd5 Qg3+ 39. Kf6 Qxe1 40. dxe6+ Kd6 41. Bf4+ Kd5 42. e7 Qxe7+ 43. Kxe7 c4 44. Kd7 c3 45. Ke7 c2 46. Bc1 Ra1 47. Bb2 Rb1 48. Ba3 Ra1 49. Bb2 Ra5 50. Kf7 Rxb5 51. Bc1 Kd6 52. Kg7 Rh5 53. Kf6 b5 54. Bf4+ Kd5 55. Ke7 Ke4 56. Bc1 b4 57. Kd7 b3 58. Kc7 Rh1 59. Bf4 b2 60. Kb7 b1=Q+ 61. Kxa7 Kxf4 62. Ka8 Qa1+ 63. Kb8 c1=Q 64. Kb7 Rd1 65. Kb6 Qab1+ 66. Ka6 Qa3# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9680149,
            ),
        ],
    ),
    TournamentData(
        date=date(2022, 11, 12),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=1,
                white='Pion Forward',
                black='Magnus Carlsen',
                pgn='''1. e4 Nc6 2. c3 e5 3. Bc4 Nf6 4. d3 b6 5. Nf3 Be7 6. Ng5 Rf8 7. Nxh7 Rh8 8.
        Nxf6+ 9. a4 Na5 10. Na3 Bxa3 11. bxa3 Qe7 12. Bd5 d6 13. Bxa8
        Rh4 14. O-O Ba6 15. g3 Qd7 16. gxh4 Qd8 17. Qh5 Qxa8 18. Qh8+ Ke7 19. Qxa8 Bxd3
        20. Re1 Bxe4 21. Qxa7 Nc6 22. Qxc7+ Ke6 23. Rxe4 f5 24. Rc4 Kd5 25. Qxc6+ Ke6
        26. Qxb6 Kd7 27. Bg5 Ke8 28. Rd1 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9661457,
            ),
            GameData(
                gid=2,
                white='Magnus Carlsen',
                black='Pion Forward',
                pgn='''1. e4 e5 2. Nf3 Nf6 3. Nxe5 Nxe4 4. Bd3 d6 5. Bxe4 dxe5 6. Ke2 Bg4+ 7. f3 f5 8.
    fxg4 fxe4 9. Ke3 Qd5 10. Rf1 Bc5+ 11. Ke2 e3 12. Nc3 Qc4+ 13. d3 Qxg4+ 14. Rf3
    Qxg2+ 15. Ke1 Qg1+ 16. Ke2 Qxh2+ 17. Ke1 e4 18. Rf4 Qh1+ 19. Ke2 Qh2+ 20. Kf1
    Rf8 21. Rxf8+ Kxf8 22. Nxe4 Qh3+ 23. Ke2 Nc6 24. Nxc5 Nd4+ 25. Ke1 Nf3+ 26. Qxf3+
    Qxf3 27. Ne6+ Kf7 28. Nd4 Re8 29. Nxf3 h5 30. Bxe3 Rxe3+ 31. Kd2
    Rxf3 32. Ke2 Rf6 33. Rf1 h4 34. Rh1 Rh6 35. c3 g5 36. b3 Re6+ 37. Kd2 Rh6 38.
    Rf1+ Kg6 39. d4 h3 40. Rf3 h2 41. Rf1 h1=Q 42. Rxh1 Rxh1 43. Kd3 Rd1+ 44. Kc4 c6
    45. b4 Kf6 46. a3 Ra1 47. Kb3 g4 48. Kc4 g3 49. a4 g2 50. a5 g1=Q 51. Kc5 Qc1
    52. Kc4 b6 53. a6 b5+ 54. Kb3 Qb1# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9661459,
            ),
            GameData(
                gid=3,
                white='Fryderyk Szopen',
                black='Jerzy Szachy',
                pgn='''1. Nf3 d5 2. d4 Nc6 3. e3 e6 4. Bb5 a6 5. Bxc6+ bxc6 6. Na3 Bxa3 7. bxa3 Rb8 8.
    g4 Nf6 9. g5 Ne4 10. O-O Nc3 11. Qd3 Rb1 12. Bd2 h6 13. Bxc3 Rxf1+ 14. Kxf1 hxg5
    15. Bd2 g4 16. Ne5 g3 17. hxg3 Rh1+ 18. Kg2 Rxa1 19. Nxc6 Qg5 20. Bb4 Qh5 21. f4
    Qh1+ 22. Kf2 Qf1+ 23. Qxf1 Rxf1+ 24. Kxf1 Kd7 25. Ne7 a5 26. Nxc8 axb4 27. Na7
    bxa3 28. Ke2 c6 29. c3 Kc7 30. Kf3 Kb6 31. Nc8+ Kb5 32. e4 dxe4+ 33. Kxe4 Ka4
    34. Ne7 f5+ 35. Kd3 Kb5 36. c4+ Kb4 37. Nxc6+ Ka4 38. Kc3 g6 39. Nb4 Ka5 40. Kb3
    Kb6 41. c5+ Kb5 42. Kxa3 Kc4 43. c6 Kxd4 44. c7 e5 45. c8=Q exf4 46. gxf4 Ke4
    47. Qd8 Kxf4 48. Nd3+ Kf3 49. Kb2 f4 50. Ne5+ Ke4 51. Nxg6 f3 52. Qf8 Ke3 53.
    Nf4 f2 54. Ng2+ Ke2 55. Qe8+ Kf3 56. Nh4+ Kg3 57. Qf8 Kxh4 58. Qxf2+ Kg4 59. Kc3
    Kg5 60. Kd4 Kg6 61. Kd5 Kg7 62. Ke6 Kg6 63. Qg2+ Kh5 64. Kf6 Kh4 65. Kf5 Kh5 66.
    Qh2# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9661463,
            ),
            GameData(
                gid=4,
                white='Jerzy Szachy',
                black='Fryderyk Szopen',
                pgn='''1. e4 g6 2. b3 e6 3. Bb2 c6 4. Bxh8 Bc5 5. d4 Bb6 6. Nf3 Ba5+ 7. c3 b6 8. b4 c5
    9. bxa5 bxa5 10. dxc5 a4 11. Qxa4 Bb7 12. Qb5 Bxe4 13. Nbd2 Bxf3 14. Nxf3 a6 15.
    Qb7 Nc6 16. Bxa6 Na5 17. Qb5 f5 18. Rd1 Nb3 19. Ng5 Qc7 20. Nxe6 Qe5+ 21. Bxe5 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9661467,
            ),
        ]
    )
]
