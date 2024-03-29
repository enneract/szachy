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
                white='Stoned Qń',
                black='Pion Forward',
                pgn='''1. Nh3 f5 2. e3 Nf6 3. Bd3 e6 4. b3 Bb4 5. c3 Bd6 6. Bb2 b6 7. c4 Nc6 8. Ng5 Nb4 9. a3 Nxd3+ 10. Ke2 Nxb2 11. Qc2 Be5 12. f4 Bd6 13. Qxb2 Bb7 14. h4 h6 15. Nf3 O-O 16. Nc3 Ng4 17. Rh3 e5 18. fxe5 Bxe5 19. Nxe5 Nxe5 20. d4 Bxg2 21. Rg3 Qxh4 22. Rxg2 Ng4 23. Nb5 d5 24. Nxc7 Rac8 25. Na6 Qh3 26. Rgg1 Qh2+ 27. Rg2 Qxg2+ 28. Kd3 Qxb2 29. Rh1 Qxa3 30. cxd5 Qxb3+ 31. Kd2 Nxe3 32. Rh3 Rc2+ 33. Ke1 Qb1#''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9680141,
            ),
            GameData(
                gid=6,
                white='Fryderyk Szopen',
                black='Husarski Generał',
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
    ),
    TournamentData(
        date=date(2022, 11, 20),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=7,
                white='Husarski Generał',
                black='Jerzy Szachy',
                pgn='''1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Bxc6 bxc6 5. Nxe5 Qe7 6. f4 g5 7. g3 f6 8. Nd3
Qxe4+ 9. Kf2 Bh6 10. Nc3 Qd4+ 11. Kf3 c5 12. Re1+ Ne7 13. Re4 g4+ 14. Kxg4 f5+
15. Kh5 fxe4 16. Kxh6 exd3 17. cxd3 Qf6+ 18. Kh5 Rg8 19. Qg4 Rxg4 20. Kxg4 Bb7
21. Ne4 h5+ 22. Kxh5 Qf5+ 23. Kh4 Ng6# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9684881,
            ),
            GameData(
                gid=8,
                white='Jerzy Szachy',
                black='Husarski Generał',
                pgn='''1. e4 b5 2. Qf3 a6 3. c4 bxc4 4. Bxc4 Nc6 5. Qxf7# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9684885,
            ),
            GameData(
                gid=9,
                white='Hikaru Hetman',
                black='Stoned Qń',
                pgn='''1. Nc3 d6 2. a3 c5 3. e4 Na6 4. b4 cxb4 5. axb4 Nxb4 6. g3 Nf6 7. Nh3 h6 8. Bg2
g5 9. Ba3 Nc6 10. f4 gxf4 11. gxf4 Nd4 12. e5 dxe5 13. fxe5 Ng4 14. O-O e6 15.
Bxb7 Bxb7 16. Qxg4 f5 17. Qg6+ Kd7 18. Rab1 Nxc2 19. Rxb7+ Kc8 20. Qf7 Nxa3 21.
Nf4 Nc4 22. Nxe6 Nxe5 23. Nxd8 Nxf7 24. Nxf7 Kxb7 25. Nxh8 Bg7 26. Nf7 h5 27.
Rxf5 Rf8 28. Nd6+ Kc6 29. Nce4 Bd4+ 30. Kg2 Re8 31. Rxh5 Bc5 32. Rxc5+ Kb6 33.
Nxe8 a6 34. h4 a5 35. Nc3 Kxc5 36. h5 Kb4 37. h6 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9685083,
            ),
            GameData(
                gid=10,
                white='Stoned Qń',
                black='Hikaru Hetman',
                pgn='''1. Nf3 d5 2. Nd4 e5 3. Nb5 Bd7 4. N5c3 Nc6 5. Nxd5 Be6 6. Ne3 f5 7. d3 f4 8. Nc4
Bxc4 9. dxc4 Qxd1+ 10. Kxd1 Rd8+ 11. Ke1 a5 12. e3 Nb4 13. exf4 Nxc2+ 14. Ke2
Nxa1 15. fxe5 Rd4 16. Be3 Rxc4 17. b3 Rc2+ 18. Kd1 Bb4 19. Bd3 Rxa2 20. Bb5+ c6
21. Ba6 b6 22. Bxb6 Nh6 23. h3 Rxf2 24. Bxf2 Nxb3 25. Bc4 a4 26. Be3 Nf5 27. Bg5
Rf8 28. Bd3 h6 29. g4 Ng3 30. Rg1 a3 31. Bb5 cxb5 32. Be3 Bc5 33. Rxg3 a2 34.
Bxc5 Nxc5 35. Kc1 Nb3+ 36. Kb2 Rf2+ 37. Kxb3 axb1=Q+ 38. Kc3 Qc2+ 39. Kd4 Qc4+
40. Ke3 Re2+ 41. Kf3 Rxe5 42. h4 Qe4+ 43. Kf2 b4 44. g5 Qc2+ 45. Kf3 b3 46. gxh6
gxh6 47. Rg8+ Kd7 48. Rh8 b2 49. Rxh6 b1=Q 50. Rf6 Qc3+ 51. Kf4 Re4+ 52. Kf5
Qe5+ 53. Kg6 Rg4+ 54. Kf7 Qe7# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9685091,
            ),
            GameData(
                gid=11,
                white='Husarski Generał',
                black='Magnus Carlsen',
                pgn='''1. c3 Nc6 2. d4 d5 3. f3 Bf5 4. e4 Be6 5. Nd2 Qd7 6. Nb3 O-O-O 7. Nc5 Qd6 8. b4
b6 9. Na6 Kb7 10. Nc5+ bxc5 11. bxc5 Qd7 12. Rb1+ Kc8 13. Bb5 Nb8 14. Bxd7+ Kxd7
15. Qa4+ Kc8 16. Qxa7 Nc6 17. Qa8+ Kd7 18. Qa6 Rb8 19. Rxb8 Nxb8 20. Qa4+ Kc8
21. c4 dxc4 22. d5 Bd7 23. c6 Be8 24. Qxc4 Nf6 25. Bb2 Nh5 26. a4 g5 27. g4 Ng7
28. Ne2 h6 29. O-O f6 30. Bd4 Na6 31. Rb1 Bg6 32. Qxa6+ Kd8 33. Rb8# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9685095,
            ),
            GameData(
                gid=12,
                white='Magnus Carlsen',
                black='Husarski Generał',
                pgn='''1. e4 b6 2. f4 c5 3. Nf3 d6 4. d3 f6 5. Be3 e5 6. Nc3 exf4 7. Bxf4 g5 8. Be3 Bg4
9. h3 Bh5 10. Nd2 Bxd1 11. Kxd1 Nh6 12. Nc4 b5 13. Nxb5 Rg8 14. Nbxd6+ Bxd6 15.
b3 Bf4 16. Bxf4 gxf4 17. Be2 Rxg2 18. Kd2 Qd7 19. Raf1 Qc7 20. Rfg1 f3 21. Rxg2
fxg2 22. Rh2 Qxh2 23. Ne3 Qxh3 24. Kc3 Qxe3 25. Kb2 Qxe2 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9685107,
            ),
            GameData(
                gid=13,
                white='Jerzy Szachy',
                black='Pion Forward',
                pgn='''1. e4 e5 2. d4 d5 3. Bb5+ Bd7 4. Nc3 a6 5. Bxd7+ Nxd7 6. Nxd5 exd4 7. Qxd4 Ndf6
8. Bg5 Be7 9. O-O-O c5 10. Qa4+ Qd7 11. Nc7+ Kd8 12. Rxd7+ Nxd7 13. Nxa8 Ne5 14.
Qa5+ Kc8 15. Qc7# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9685275,
            ),
            GameData(
                gid=14,
                white='Pion Forward',
                black='Jerzy Szachy',
                pgn='''1. e4 e5 2. d4 f6 3. c3 c6 4. Nf3 Na6 5. b4 Bd6 6. Ba3 Ne7 7. Qd2 O-O 8. g4 Qb6
9. Bc4+ Kh8 10. g5 fxg5 11. Nxg5 exd4 12. cxd4 Bf4 13. Qd3 Bxg5 14. b5 Qa5+ 15.
Kd1 cxb5 16. Bxe7 Bxe7 17. Bd5 Nb4 18. Qd2 d6 19. a3 Bg4+ 20. Ke1 Bf3 21. Rg1
Nc2+ 22. Kf1 Qxd2 23. Nxd2 Nxa1 24. Nxf3 Rxf3 25. Bxb7 Raf8 26. Kg2 Rxf2+ 27.
Kg3 R8f3+ 28. Kg4 d5 29. Rc1 Bxa3 30. Rc8+ Bf8 31. Bxd5 a5 32. e5 Rd3 33. Bf7
Rxf7 34. e6 Rxd4+ 35. Kg5 h6+ 36. Kg6 Rf6+ 37. Kh5 Rxe6 38. Rxf8+ Kh7 39. Rf5
g6# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9685279,
            ),
            GameData(
                gid=15,
                white='Husarski Generał',
                black='Stoned Qń',
                pgn='''1. Nc3 c6 2. d4 d5 3. e3 Na6 4. Bxa6 bxa6 5. b4 Qb6 6. a3 a5 7. bxa5 Qxa5 8. Bb2
Nf6 9. f3 e6 10. e4 dxe4 11. fxe4 Be7 12. e5 Nd5 13. Qd2 h6 14. Nxd5 Qxd2+
15. Kxd2 exd5 16. Nf3 g5 17. g3 f5 18. h3 Rb8 19. Rhb1 g4 20. Nh4 gxh3 21. Rh1
f4 22. Rxh3 Bxh3 23. c4 Rxb2+ 24. Kc1 Rh2 25. Kb1 Rh1+ 26. Kb2 Rxa1 27. Kxa1
dxc4 28. Kb2 fxg3 29. Ng6 Rg8 30. Nf4 Bf1 31. d5 g2 32. dxc6 g1=Q 33. c7 Kf7
34. e6+ Kf6 35. Nd5+ Kxe6 36. Nf4+ Ke5 37. Nh3 Qh2+ 38. Kc3 Qxh3+ 39. Kc2 Kd4
40. a4 Rc8 41. a5 Rxc7 42. a6 Rc6 43. Kd2 c3+ 44. Ke1 Rxa6 45. Kf2
Ra2+ 46. Kg1 Bc5 ½-½''',
                score=1,
                termination=Termination.STALEMATE,
                chess_com_embed=9685289,
            ),
            GameData(
                gid=16,
                white='Hikaru Hetman',
                black='Fryderyk Szopen',
                pgn='''1. Nc3 e5 2. e4 b6 3. Nf3 Bb7 4. Nxe5 f6 5. Nc4 Ne7 6. e5 d6 7. f4 Bd5 8. b3 b5
9. Ne3 b4 10. Ncxd5 Nxd5 11. Nxd5 fxe5 12. Qh5+ g6 13. Qh3 Bg7 14. g3 exf4 15.
Nxf4 Bxa1 16. Qe6+ Qe7 17. Bb5+ Kf8 18. c3 bxc3 19. dxc3 Bxc3+ 20. Ke2 a6 21.
Bd2 axb5 22. Bxc3 Rg8 23. Qe3 Rxa2+ 24. Kd3 g5 25. Ne6+ Kf7 26. Rf1+ Kg6 27.
Qe4+ Kh6 28. Rf6+ Kh5 29. g4+ Kh4 30. Rh6# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9685433,
            ),
            GameData(
                gid=17,
                white='Fryderyk Szopen',
                black='Hikaru Hetman',
                pgn='''1. e4 Nf6 2. d3 e5 3. b4 Bxb4+ 4. Bd2 a5 5. Qf3 Bxd2+ 6. Kxd2 d5 7. Nc3 c6 8. g4
O-O 9. g5 Ng4 10. h3 dxe4 11. Qg3 Qxg5+ 12. f4 exf4 13. Qxg4 e3+ 14. Ke2 Bxg4+
15. Ke1 f3 16. hxg4 f2+ 17. Ke2 Qxg4+ 18. Kxe3 fxg1=Q+ 19. Rxg1 Qxg1+ 20. Ke2
Re8+ 21. Ne4 Qh2+ 22. Kf3 f5 23. Ng3 Rf8 24. Re1 f4 25. Ne4 Qxc2 26. d4 Qxa2 27.
Nd6 Qa3+ 28. Re3 fxe3+ 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9685431,
            ),
        ],
    ),
    TournamentData(
        date=date(2022, 11, 27),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=18,
                white='Jerzy Szachy',
                black='Hikaru Hetman',
                pgn='''1. e4 Nf6 2. d3 e5 3. Nf3 Nc6 4. d4 d6 5. dxe5 Nxe5 6. Nxe5 dxe5 7. Qxd8+ Kxd8
8. Bd3 Bb4+ 9. Nc3 Re8 10. O-O b5 11. Rd1 Bxc3 12. Bxb5+ Bd7 13. Bxd7 Nxd7 14.
bxc3 Kc8 15. Rb1 Rb8 16. Rxb8+ Kxb8 17. Rxd7 Rf8 18. f4 exf4 19. Bxf4 Kc8 20.
Rxc7+ Kb8 21. Bd6 Rd8 22. e5 f6 23. Rxg7+ Ka8 24. exf6 Rxd6 25. f7 Rd1+ 26. Kf2
Rd2+ 27. Ke3 Rd8 28. Rg8 Rxg8  1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9704649,
            ),
            GameData(
                gid=19,
                white='Hikaru Hetman',
                black='Jerzy Szachy',
                pgn='''1. e4 e5 2. Qh5 Nc6 3. d3 Nf6 4. Qh3 d5 5. g4 Bxg4 6. Qg3 dxe4 7. Bg5 Nh5 8.
Qxg4 Be7 9. Bxe7 Qxe7 10. Qxh5 g6 11. Qh3 Qb4+ 12. Nd2 Qxb2 13. Rb1 Qxc2 14. Qe3
exd3 15. Bxd3 O-O-O 16. Bxc2 Nb4 17. Rxb4 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9704655,
            ),
            GameData(
                gid=20,
                white='Hikaru Hetman',
                black='Stoned Qń',
                pgn='''1. e4 Nc6 2. d4 d5 3. exd5 Na5 4. c4 e6 5. Qd2 Nxc4 6. Bxc4 exd5 7. Bb5+ Bd7 8.
Qe3+ Be7 9. Nc3 c6 10. Bd3 h6 11. Nf3 Qa5 12. Ne5 Bc8 13. Qg3 Rh7 14. Bd2 f6 15.
Ng6 Bb4 16. a3 Bxc3 17. Bxc3 Qb6 18. Nh4 g5 19. Bxh7 gxh4 20. Qxh4 Ne7 21. Qxf6
Qc7 22. O-O b6 23. Rfe1 c5 24. Bg6+ Kd7 25. Qxe7+ Kc6 26. Qe8+ Kb7 27. Re7 Kb8
28. Rxc7 Kxc7 29. dxc5 bxc5 30. Qe7+ Bd7 31. Qxc5+ Bc6 32. Be5+ Kd7 33. Bf5+ Kd8
34. Qxc6 Rc8 35. Bxc8 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9704659,
            ),
            GameData(
                gid=21,
                white='Stoned Qń',
                black='Hikaru Hetman',
                pgn='''1. d4 Nc6 2. c3 d5 3. Nf3 Bg4 4. Nh4 h6 5. f3 g5 6. Nf5 Bxf5 7. Na3 e5 8. dxe5
Nxe5 9. e3 c5 10. Bb5+ Nc6 11. Bxc6+ bxc6 12. O-O c4 13. b3 Bd3 14. Re1 Bc5 15.
bxc4 dxc4 16. f4 gxf4 17. Kf2 Qf6 18. Qf3 O-O-O 19. g3 Bxa3 20. Bxa3 Qxc3 21.
Rec1 Qxa3 22. exf4 Qb2+ 23. Ke1 c3 24. Qxc6+ Kb8 25. g4 Ne7 26. Qf6 Qe2# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9704663,
            ),
            GameData(
                gid=22,
                white='Pion Forward',
                black='Fryderyk Szopen',
                pgn='''1. d4 Nc6 2. c3 d6 3. Bf4 Bf5 4. f3 Bxb1 5. Qxb1 f6 6. d5 e5 7. Qe4 Nge7 8. dxc6
bxc6 9. Qa4 exf4 10. Qxf4 Ng6 11. Qe4+ Ne5 12. O-O-O d5 13. Qf5 Bc5 14. Qe6+ Qe7
15. Qxe7+ Bxe7 16. e4 Bc5 17. exd5 Be3+ 18. Kc2 O-O-O 19. Ba6+ Kb8 20. b3 cxd5
21. c4 d4 22. Ne2 d3+ 23. Kc3 dxe2 24. Rxd8+ Rxd8 25. Re1 Rd1 26. Rxe2 Rd3+ 27.
Kb4 Bd2+ 28. Kc5 Nd7+ 29. Kb5 Nb6 30. Re8+ Nc8 31. Rxc8# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9704665,
            ),
            GameData(
                gid=23,
                white='Fryderyk Szopen',
                black='Pion Forward',
                pgn='''1. e4 Nc6 2. d3 e5 3. Nf3 g6 4. b3 Bc5 5. Bb2 Qf6 6. Na3 a6 7. Nc4 Nd4 8. Ncxe5
Nxf3+ 9. gxf3 d6 10. d4 Bxd4 11. Bxd4 dxe5 12. Bc3 c5 13. f4 Qxf4 14. Qe2 Bg4
15. Qe3 Qxe3+ 16. fxe3 O-O-O 17. Bxe5 Bf3 18. Rg1 f6 19. Bg3 Bxe4 20. c3 h5 21.
b4 cxb4 22. cxb4 g5 23. Rd1 h4 24. Bh3+ Bf5 25. Bxf5+ Rd7 26. Bxd7+ Kd8 27. Bc6+
Ke7 28. Bxb7 hxg3 29. Rxg3 Rxh2 30. Bxa6 Nh6 31. Kf1 Rxa2 32. Bb5 Rb2 33. Rd7+
Ke6 34. Rh3 Nf5 35. e4 Nd6 36. Rd3 Nxb5 37. R3d5 Rxb4 38. Rb7 Rxe4 39. Rbxb5 g4
40. Kg2 Re2+ 41. Kg3 Re4 42. Rh5 Kd6 43. Rb6+ Ke7 44. Rh6 f5 45. Rh7+ Kf8 46.
Rb8+ Re8 47. Rh8+ Kf7 48. Rhxe8 f4+ 49. Kxg4 Kf6 50. Kxf4 Kg6 51. Kg4 Kf6 52.
Rb6+ Kf7 53. Rbe6 Kg7 54. Kg5 Kf7 55. Kh6 1/2-1/2''',
                score=1,
                termination=Termination.STALEMATE,
                chess_com_embed=9704667,
            ),
            GameData(
                gid=24,
                white='Fryderyk Szopen',
                black='Jerzy Szachy',
                pgn='''1. e4 e5 2. Nf3 Nf6 3. Nxe5 Qe7 4. f4 Nxe4 5. d3 Qb4+ 6. Bd2 Nxd2 7. Qxd2 Qxb2
8. Qc3 Ba3 9. Qxa3 Qxa1 10. Qb3 Qd4 11. Qxf7+ Kd8 12. Qxg7 Qe3+ 13. Be2 Qc1+ 14.
Bd1 Qe3+ 15. Kf1 Qxf4+ 16. Bf3 Rf8 17. g3 Qc1+ 18. Kg2 Qxc2+ 19. Kh3 d6+ 20. Ng4
Rxf3 21. Qg5+ Kd7 22. Nf6+ Kc6+ 23. Kh4 Nd7 24. Qd5+ Kb6 25. Qxf3 Qa4+ 26. Ne4
Nc5 27. Nc3 Qe8 28. Rb1+ Kc6 29. Nf6+ Ne4 30. Ncxe4 Qd8 31. Rc1+ Kb6 32. a4 Bd7
33. Qe3+ c5 34. Nxc5 Qxf6+ 35. Qg5 Qd4+ 36. g4 Qf2+ 37. Kh3 Bxg4+ 38. Kxg4 Qg2+
39. Kh4 Qxg5+ 40. Kxg5 Rg8+ 41. Kf4 dxc5 42. Rb1+ Ka5 43. Ra1 Rd8 44. Ra3 Rd4+
45. Ke5 Kb4 46. Ra1 Rxd3 47. Ke4 c4 48. a5 Kb3 49. Rc1 Rd2 50. Ke3 c3 51. Rb1+
Kc2 52. Re1 Rd1 53. Ke2 Rxe1+ 54. Kxe1 Kb2 55. Kd1 c2+ 56. Kd2 c1=Q+ 57. Ke2 b6
58. axb6 axb6 59. h4 b5 60. Kf3 b4 61. h5 b3 62. Kg4 Kc2 63. Kf5 b2 64. Kf6 b1=Q
65. Kg7 Kd1 66. h6 Qc6 67. Kf7 Qbb7+ 68. Kg8 Qcc8# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9704673,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 1, 8),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=25,
                white='Jerzy Szachy',
                black='Fryderyk Szopen',
                pgn='''1. d4 e6 2. Bf4 Bd6 3. Bxd6 cxd6 4. Nf3 Qa5+ 5. Nc3 e5 6. d5 e4 7. Ng5 Nf6 8.
Qd2 h6 9. Ngxe4 Nxe4 10. Nxe4 Qa6 11. e3 f5 12. Bxa6 fxe4 13. Bc4 O-O 14. O-O g5
15. f4 a6 16. fxg5 hxg5 17. Rxf8+ Kxf8 18. Rf1+ Ke8 19. Qf2 Kd8 20. g4 b5 21. h4
bxc4 22. h5 Bb7 23. Rd1 a5 24. h6 Na6 25. h7 Kc7 26. Qf6 Nc5 27. h8=Q Rxh8 28.
Qxh8 Nd3 29. cxd3 cxd3 30. Rc1+ Kb6 31. Qd8+ Kb5 32. Qxd7+ Kb4 33. Qxb7+ Ka4 34.
Rc4# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9848491,
            ),
            GameData(
                gid=28,
                white='Pion Forward',
                black='Stoned Qń',
                pgn='''1. e4 e5 2. Nf3 Nc6 3. d4 Nxd4 4. Nxd4 exd4 5. Qxd4 d6 6. Qa4+ Bd7 7. Bb5 c6 8.
Bc4 b5 9. Bxf7+ Kxf7 10. Qb3+ Ke8 11. g3 Nf6 12. f3 Qa5+ 13. Bd2 Qb6 14. Nc3 Qb7
15. a4 d5 16. axb5 cxb5 17. Nxd5 Rb8 18. Bf4 Rc8 19. O-O Bc6 20. Qd3 Bc5+ 21.
Kg2 a5 22. Rxa5 Bb4 23. Nxb4 Nxe4 24. Re1 Rd8 25. Bd6 Rxd6 26. Qb3 Rd2+ 27. Kh3
Bd7+ 28. Kh4 Rxh2# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9920929,
            ),
            GameData(
                gid=26,
                white='Husarski Generał',
                black='Stoned Qń',
                pgn='''1. Nc3 e5 2. a4 Nc6 3. e3 d6 4. Bb5 Nf6 5. h3 a6 6. Bxc6+ bxc6 7. f3 c5 8. d4
cxd4 9. Ne4 Nd5 10. exd4 Ne3 11. Bxe3 d5 12. Nc5 Be7 13. Nb3 O-O 14. dxe5 Bb4+
15. c3 Be7 16. Ne2 c6 17. Ned4 Rb8 18. f4 a5 19. Nxc6 Qc7 20. Nxb8 Qxb8 21. Nxa5
Bh4+ 22. Ke2 Ba6+ 23. Kd2 Qxb2+ 24. Qc2 Qb7 25. Nxb7 Bxb7 26. Rab1 Bc8 27. Rb8
1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9848791,
            ),
            GameData(
                gid=27,
                white='Stoned Qń',
                black='Husarski Generał',
                pgn='''1. e4 Nf6 2. d3 e5 3. Nf3 d6 4. Bg5 Bg4 5. Bxf6 gxf6 6. h3 Bh5 7. g4 Bg6 8. Nc3
c6 9. h4 d5 10. h5 dxe4 11. dxe4 Qxd1+ 12. Kxd1 Bb4 13. Na4 b5 14. Nc3 Na6 15.
hxg6 Bxc3 16. bxc3 fxg6 17. c4 Nc5 18. cxb5 Nxe4 19. Rh2 Rd8+ 20. Ke1 g5 21.
bxc6 a5 22. Bb5 Ke7 23. Rh6 Rb8 24. c4 Kf7 25. c7 Rbc8 26. Rc1 Rxc7 27. a3 Kg7
28. Ke2 Kxh6 29. Rh1+ Kg6 30. Ke3 Nc3 31. Ba6 Ra8 32. Rc1 Na2 33. Rc2 Rxa6 34.
Rxa2 Rxc4 35. Nd2 Rxg4 36. Rc2 f5 37. Rc8 f4+ 38. Ke2 Rg2 39. Rg8+ Kh6 40. Nf3
g4 41. Nxe5 f3+ 42. Ke3 Re6 43. Ke4 Rxf2 44. Rxg4 Kh5 45. Rf4 Re2+ 46. Kf5
R6xe5+ 47. Kf6 f2 48. a4 R5e4 49. Rf5+ Kg4 50. Rxa5 f1=Q+ 51. Kg7 Re7+ 52. Kg8
Qf7+ 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9848979,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 1, 13),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=29,
                white='Magnus Carlsen',
                black='Pion Forward',
                pgn='''1. Nf3 d5 2. e3 f6 3. Nc3 c6 4. Nd4 Qd7 5. Be2 c5 6. Nb3 Nc6 7. O-O g6 8. f4 e5
9. Nxc5 Qd6 10. Nd3 e4 11. b4 exd3 12. cxd3 Qxb4 13. a4 d4 14. exd4 Nxd4 15. Na2
Qd6 16. Rb1 Qe6 17. Rb4 Nxe2+ 18. Qxe2 Qxe2 19. Re4+ Qxe4 20. dxe4 Be6 21. Nc3
Bc4 22. d3 Bc5+ 23. Kh1 Bxd3 24. Rf3 Rd8 25. Ba3 Bxa3 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9872765,
            ),
            GameData(
                gid=30,
                white='Pion Forward',
                black='Magnus Carlsen',
                pgn='''1. e4 Nf6 2. f3 Nc6 3. c3 e5 4. g4 g5 5. Bc4 d5 6. exd5 Bd7 7. dxc6 Bxc6 8. Qb3
Nd7 9. Bxf7+ Ke7 10. Qe6# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9872771,
            ),
            GameData(
                gid=31,
                white='Stoned Qń',
                black='Fryderyk Szopen',
                pgn='''1. e4 Nf6 2. d3 e5 3. Nf3 d6 4. d4 exd4 5. Nxd4 Nxe4 6. Bb5+ Nd7 7. Qe2 d5 8. c4
Bb4+ 9. Nc3 c6 10. Nxc6 bxc6 11. Ba4 O-O 12. Bxc6 Bxc3+ 13. bxc3 Ba6 14. Qe3 Re8
15. cxd5 g5 16. f3 Nef6 17. h4 h6 18. hxg5 Rxe3+ 19. Bxe3 Nxd5 20. Bxd5 Rc8 21.
gxh6 Rxc3 22. Bxa7 Qa5 23. h7+ Kg7 24. h8=Q+ Kg6 25. Be4+ f5 26. Rh5 Rc1+ 27.
Kf2 Rc2+ 28. Bxc2 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9872777,
            ),
            GameData(
                gid=32,
                white='Fryderyk Szopen',
                black='Stoned Qń',
                pgn='''1. e4 e5 2. Nc3 d6 3. Bb5+ c6 4. Ba4 b5 5. Bb3 a6 6. Nf3 Nf6 7. d3 Bg4 8. a4 a5
9. h3 Bh5 10. Ng5 Bxd1 11. Nxf7 Qe7 12. Nxh8 Bh5 13. axb5 cxb5 14. Nxb5 a4 15.
Rxa4 Qb7 16. Na7 Rxa7 17. Rxa7 Qxa7 18. Be3 Qa1+ 19. Kd2 Qxh1 20. Ba4+ Nbd7 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9872783,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 1, 15),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=33,
                white='Hikaru Hetman',
                black='Pion Forward',
                pgn='''1. d4 d5 2. Nf3 f6 $2 3. Nc3 c6 $6 4. e4 Bg4 5. h3 Bxf3 $6 6. Qxf3 e5 7. exd5 cxd5 $2
8. Nxd5 Qa5+ 9. Bd2 exd4 10. Bxa5 Kd7 $2 11. Nc7 $2 Nc6 $2 12. Qd5+ Bd6 13. Nxa8 $2 Nxa5
14. Qxa5 Ne7 15. Bb5+ Ke6 16. Nc7+ Kf7 17. Bc4+ Kg6 18. Bd3+ Kh6 19. Ne6 Nc6 $2
20. Qd2+ g5 21. h4 Re8 $6 22. hxg5# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9883815,
            ),
            GameData(
                gid=34,
                white='Pion Forward',
                black='Hikaru Hetman',
                pgn='''1. e4 e5 2. Nc3 d6 3. Nf3 Nc6 4. Bc4 Nd4 5. Nd5 c6 6. c3 Nxf3+ 7. gxf3 cxd5 8.
Qa4+ Bd7 9. Bb5 Nf6 10. d4 a6 11. Bxd7+ Nxd7 12. dxe5 dxe5 13. exd5 b5 14. Qc2
Bc5 15. b4 Bd6 16. a4 bxa4 17. Qxa4 O-O 18. Qc6 Nb6 19. Be3 Rb8 20. Rxa6 Re8 21.
Bxb6 Rxb6 22. Rxb6 h6 23. Qxd6 Qxd6 24. Rxd6 e4 25. fxe4 Rxe4+ 26. Kf1 Re8 27.
f4 Rc8 28. Rg1 Rxc3 29. Rg3 Rc1+ 30. Kf2 Rc2+ 31. Kf3 Rxh2 32. Rd8+ Kh7 33. Rf8
Rd2 34. Rxf7 Rd3+ 35. Kg4 Rxg3+ 36. Kxg3 Kg6 37. Ra7 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9883823,
            ),
            GameData(
                gid=35,
                white='Fryderyk Szopen',
                black='Jerzy Szachy',
                pgn='''1. Nf3 d6 2. e4 e5 3. Bb5+ Bd7 4. Bd3 Nf6 5. Bc4 Bc6 6. Ng5 d5 7. Bd3 Nxe4 8.
Nxe4 dxe4 9. Bxe4 Bxe4 10. f3 Bd5 11. Nc3 Bc5 12. Qe2 Nc6 13. Qb5 Qe7 14. Nxd5
Qd6 15. Qxb7 Kd7 16. Nc3 Na5 17. Qd5 Bb4 18. a3 Bxc3 19. Qxd6+ cxd6 20. dxc3 Nc4
21. b3 Rhc8 22. f4 e4 23. bxc4 Rxc4 24. Bd2 Re8 25. O-O-O e3 26. Rhe1 exd2+ 27.
Kxd2 Rxf4 28. g3 Rf2+ 29. Kd3 Rxh2 30. Rb1 Rxe1 31. Rxe1 f5 32. c4 g5 33. Kd4 f4
34. gxf4 gxf4 35. c5 f3 36. Kd5 dxc5 37. Kxc5 f2 38. Rf1 h5 39. a4 h4 40. a5 h3
41. Kb5 Kc7 42. a6 Rg2 43. Rh1 h2 44. c3 Rg1 45. Rxh2 f1=Q+ 46. c4 Rg5+ 47. Kb4
Qe1+ 48. Kb3 Qg3+''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9883833,
            ),
            GameData(
                gid=36,
                white='Stoned Qń',
                black='Jerzy Szachy',
                pgn='''1. e4 e5 2. Nf3 Bd6 $2 3. c3 b5 $4 4. d4 $1 exd4 5. Nxd4 $2 Ba6 $2 6. Bxb5 c6 $2 7. Bc4 $4
Bxc4 8. b3 $2 Be6 $6 9. O-O Nf6 10. Re1 $6 O-O $4 11. e5 $1 Bg4 $2 12. f3 $1 Qb6 $4 13. fxg4
Bxe5 14. Rxe5 d6 15. Rf5 Nbd7 16. Na3 $6 c5 $6 17. Nc4 Qc7 18. Nb5 Qc6 19. a4 Rfe8
20. g5 Qe4 21. gxf6 Qxf5 22. Ncxd6 Qxf6 23. Nxe8 Rxe8 24. Qxd7 $4 Qxc3 25. Qxe8#
1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9883841,
            ),
            GameData(
                gid=37,
                white='Stoned Qń',
                black='Fryderyk Szopen',
                pgn='''1. e4 e5 2. Nf3 Qe7 3. Nc3 d5 4. Bb5+ c6 5. Nxd5 Qc7 6. Nxc7+ 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9883845,
            ),
            GameData(
                gid=38,
                white='Jerzy Szachy',
                black='Stoned Qń',
                pgn='''1. d4 d5 2. Bf4 f6 3. Nf3 e5 4. dxe5 fxe5 5. Bxe5 Bb4+ 6. Nbd2 Nc6 7. Bxg7 Nge7
8. Bxh8 Qd7 9. c3 Ba5 10. Qc2 Qe6 11. Ng5 Qf6 12. Bxf6 h6 13. Bxe7 Kxe7 14. Qh7+
Kd6 15. Qxh6+ Kc5 16. b4+ Bxb4 17. cxb4+ Nxb4 18. Rc1+ Kb5 19. e4+ Ka4 20. exd5
Nxa2 21. Rc4+ Kb5 22. Rc2+''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9883851,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 1, 22),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=39,
                white='Hikaru Hetman',
                black='Magnus Carlsen',
                pgn='''1. e4 e5 2. Qh5 Nf6 3. Qxe5+ Be7 4. Nf3 d6 5. Qg3 Nxe4 6. Qf4 Nf6 7. Bc4 O-O 8.
Ng5 h6 9. Bxf7+ Kh8 10. h4 hxg5 11. hxg5+ Nh7 12. g6 Rxf7 13. gxf7 Qf8 14. b4
Nc6 15. Ba3 b5 16. Bb2 d5 17. Qh6 Qxf7 18. Qxh7# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9920935,
            ),
            GameData(
                gid=40,
                white='Magnus Carlsen',
                black='Hikaru Hetman',
                pgn='''1. e4 e5 2. d3 Nc6 3. Nf3 Qe7 4. Nc3 b5 5. Bg5 f6 6. Nd5 Qc5 7. Nxc7+ Kd8 8.
Nxa8 Qb4+ 9. Ke2 Nd4+ 10. Nxd4 exd4 11. f4 fxg5 12. fxg5 Bb7 13. c3 Qxb2+ 14.
Ke1 dxc3 15. Rb1 Qxa2 16. Ra1 Qb2 17. Rb1 Bb4 18. Rxb2 cxb2+ 19. Kf2 Bxa8 20.
Be2 Ne7 21. Qb1 Ba3 22. Rd1 Rf8+ 23. Ke1 Nc6 24. Qa2 Bb4+ 25. Rd2 Bxd2+ 26. Kd1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=9920939,
            ),
            GameData(
                gid=41,
                white='Fryderyk Szopen',
                black='Stoned Qń',
                pgn='''1. Nc3 c6 2. Nf3 d5 3. e4 Qa5 4. exd5 cxd5 5. Bb5+ Nc6 6. a3 a6 7. b4 Qb6 8. Rb1
axb5 9. Nxd5 Qa6 10. Nc7+ Kd7 11. Nxa6 Rxa6 12. d4 Nf6 13. Rb3 Ke8 14. d5 Nd8
15. Rd3 Bf5 16. Rd2 Rxa3 17. Bxa3 e6 18. dxe6 Be7 19. exf7+ Kf8 20. Ne5 Bg4 21.
Rxd8+ Bxd8 22. Qxd8+ Ne8 23. Qxe8# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9921031,
            ),
            GameData(
                gid=42,
                white='Jerzy Szachy',
                black='Fryderyk Szopen',
                pgn='''1. d4 Nf6 2. Bf4 d5 3. Nf3 Bg4 4. e3 Bxf3 5. Qxf3 e6 6. Nd2 Bb4 7. c3 Bd6 8. Bd3
h5 9. Bg5 Be7 10. O-O Nc6 11. e4 h4 12. exd5 Nxd5 13. Rae1 Bxg5 14. Ne4 Ne5 15.
dxe5 b5 16. Nxg5 Qxg5 17. Bxb5+ Ke7 18. Bc6 Rab8 19. Bxd5 Rxb2 20. h3 exd5 21.
Qxd5 Rd8 22. Qc5+ Kd7 23. Rd1+ Rd2 24. e6+ Kxe6 25. Qxg5 Rxd1 26. Rxd1 Rxd1+ 27.
Kh2 f6 28. Qg4+ f5 29. Qxd1''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9921159,
            ),
            GameData(
                gid=43,
                white='Hikaru Hetman',
                black='Pion Forward',
                pgn='''1. e4 Nf6 2. Nc3 c6 3. Qe2 d5 4. e5 Bg4 5. f3 Bf5 6. exf6 gxf6 7. g4 Bxc2 8. b4
Qd7 9. b5 a6 10. a4 axb5 11. a5 e5 12. Bb2 Bc5 13. Nh3 d4 14. Ne4 Ke7 15. Nxc5
Qc7 16. g5 fxg5 17. Nxg5 b6 18. axb6 Rxa1+ 19. Bxa1 Qd6 20. Nge4 Qg6 21. Bh3 f5
22. Nf2 Nd7 23. Nxd7 Kxd7 24. Qxe5 Re8 25. Bxf5+ Qe6 26. Bxe6+ Rxe6 27. Qxe6+
Kxe6 28. b7 b4 29. b8=Q b3 30. Qe8+ Kd5 31. Qh5+ Kc4 32. Ne4 Kd3 33. Qxh7 Bb1
34. Bxd4 Kxd4 35. Qd7+ Ke5 36. Qd6+ Kf5 37. Qf6# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9921383,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 2, 3),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=44,
                white='Jerzy Szachy',
                black='Magnus Carlsen',
                pgn='''1. d4 Nf6 2. Bf4 d5 3. Nf3 Nc6 4. e3 h5 5. Bd3 Bf5 6. Bxf5 Rh7 7. Bxh7 Nxh7 8.
O-O Qd7 9. Nbd2 O-O-O 10. Ne5 Qd6 11. Nxf7 Rd7 12. Nxd6+ exd6 13. Qxh5 Re7 14.
Qxh7 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=9990183,
            ),
            GameData(
                gid=45,
                white='Magnus Carlsen',
                black='Jerzy Szachy',
                pgn='''1. e4 c5 2. Bd3 d6 3. f4 e5 4. c4 exf4 5. Qg4 Bxg4 6. Kf1 Qh4 7. h3 h5 8. a4 g6
9. b3 Bg7 10. Ra2 Bd4 11. Ne2 Qf2# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9990189,
            ),
            GameData(
                gid=46,
                white='Fryderyk Szopen',
                black='Stoned Qń',
                pgn='''1. e4 e5 2. Nf3 d6 3. d4 Bg4 4. dxe5 Bxf3 5. gxf3 Nc6 6. exd6 cxd6 7. Bb5 Qa5+
8. Nc3 Rc8 9. f4 a6 10. Bxc6+ Rxc6 11. Bd2 Nf6 12. Qe2 Qh5 13. e5 dxe5 14. fxe5
Ng4 15. e6 fxe6 16. h3 Nf6 17. f3 e5 18. f4 g5 19. fxe5 Qh6 20. exf6+ Kf7 21.
Rf1 Qxh3 22. Bxg5 Rc5 23. Rg1 a5 24. Be3 b6 25. Bxc5 bxc5 26. Ne4 h5 27. Rd1 Rh6
28. Nd6+ Bxd6 29. Rxd6 Qh4+ 30. Kd1 c4 31. Rg7+ Kf8 32. Rd8# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=9991037,
            ),
            GameData(
                gid=47,
                white='Stoned Qń',
                black='Fryderyk Szopen',
                pgn='''1. e4 e5 2. Qh5 Qe7 3. Nf3 Nf6 4. Qf5 g6 5. Qh3 d6 6. b3 Bxh3 7. gxh3 Nxe4 8.
Ba3 g5 9. d3 Nc5 10. h4 g4 11. Nfd2 Bg7 12. Nc3 e4 13. Nd5 Qe5 14. Rb1 exd3+ 15.
Kd1 dxc2+ 16. Kxc2 Qxd5 17. Bb5+ c6 18. Rhe1+ Be5 19. Ba4 Nd3 20. Re3 Nc5 21.
Rg1 f5 22. f3 Nxa4 23. bxa4 Qxa2+ 24. Kd1 gxf3 25. Nxf3 f4 26. Ree1 Qxa3 27.
Nxe5 dxe5 28. Rxe5+ Qe7 29. Rxe7+ Kxe7 30. Re1+ Kf7 31. Kd2 Rd8+ 32. Ke2 b5 33.
Rf1 bxa4 34. Rxf4+ Ke7 35. h5 a3 36. Ra4 Nd7 37. Rxa3 Ne5 38. Re3 Rd5 39. Rg3
Rb8 40. Rg7+ Kf6 41. Rxh7 Rb2+ 42. Ke3 Ng4+ 43. Kf3 Nxh2+ 44. Kg3 Nf1+ 45. Kg4
Rd4+ 46. Kf3 Rb3+ 47. Ke2 Ng3+ 48. Kf2 Rd2+ 49. Ke1 Ne4 50. Rh6+ Kg5 51. Rh7
Rb1# 0-1''',
                score=0,
                termination=Termination.CHECKMATE,
                chess_com_embed=9991045,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 2, 5),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=48,
                white='Jerzy Szachy',
                black='Hikaru Hetman',
                pgn='''1. d4 d5 2. Bf4 Nc6 3. Nf3 Bf5 4. e3 Nf6 5. Bd3 Ne4 6. Nbd2 e6 7. O-O g5 8. Nxg5
Nxg5 9. Bxg5 Qxg5 10. f4 Qg4 11. Qxg4 Bxg4 12. e4 Nxd4 13. e5 Bc5 14. Kh1 O-O-O
15. Rae1 Rdg8 16. c3 Nf5 17. b4 Be3 18. h3 Ng3+ 19. Kh2 Nxf1+ 20. Nxf1 Bxf4+ 21.
g3 Bd2 22. Nxd2 Bf5 23. Bxf5 exf5 24. e6 fxe6 25. Rxe6 h5 26. Re5 h4 27. gxh4
Rxh4 28. Rxf5 c6 29. Nf3 Rc4 30. a3 Rxc3 31. Ne5 Rc2+ 32. Kh1 Rc1+ 33. Kh2 d4
34. h4 Rc2+ 35. Kh3 Ra2 36. h5 Rd8 37. Rf3 Re8 38. h6 Rxe5 39. Rf8+ Kc7 40. h7
Rh5+ 41. Kg3 Rxh7 42. Kf3 Rxa3+ 43. Ke4 d3 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=10001947,
            ),
            GameData(
                gid=49,
                white='Hikaru Hetman',
                black='Jerzy Szachy',
                pgn='''1. e4 c6 2. d4 d5 3. exd5 cxd5 4. Nc3 Nf6 5. Bg5 Nbd7 6. Bb5 a6 7. Bxd7+ Bxd7 8.
Bxf6 exf6 9. Qe2+ Qe7 10. Nxd5 Qxe2+ 11. Nxe2 Rc8 12. O-O-O Bb5 13. Nb6 Bxe2 14.
Rde1 Rd8 15. c3 Be7 16. Rxe2 O-O 17. Rxe7 Rd6 18. Rxb7 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=10001955,
            ),
            GameData(
                gid=50,
                white='Myster Robakov',
                black='Magnus Carlsen',
                pgn='''1. d4 Nc6 2. Bf4 Nxd4 3. Nc3 Nxc2+ 4. Qxc2 d5 5. Nf3 Nf6 6. a4 g6 7. e3 c6 8.
    Ra3 Bg7 9. Bd3 O-O 10. b4 e6 11. O-O h6 12. Rb3 h5 13. Nh4 Ng4 14. Rbb1 f6 15.
    Be2 g5 16. Ng6 gxf4 17. exf4 e5 18. Nxd5 Qxd5 19. fxe5 Re8 20. Rbd1 Qf7 21. Bc4
    Re6 22. Rde1 Qxg6 23. Qxg6 Nxe5 24. Qxh5 Nxc4 25. Rxe6 Bxe6 26. Re1 Bf7 27. Re7
    Kf8 28. Rxf7+ Kg8 29. Rxg7+ Kxg7 30. Qh4 f5 31. Qxc4 Rd8 32. a5 b5 33. Qc3+ Kg6
    34. Qg3+ Kf6 35. h4 Rd4 36. h5 Rxb4 37. Qc3+ Rd4 38. Qxd4+ Kg5 39. Qd8+ Kxh5 40.
    g3 Kg4 41. Qg8+ Kf3 42. Kf1 Ke4 43. Qa8 f4 44. Qxa7 b4 45. Qb7 b3 46. Qxb3 1-0''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=10002413,
            ),
            GameData(
                gid=51,
                white='Magnus Carlsen',
                black='Myster Robakov',
                pgn='''1. e4 e5 2. d3 Bb4+ 3. Bd2 Bc5 4. Be3 Bb4+ 5. c3 Ba5 6. Nf3 f6 7. Nbd2 Nc6 8.
Qa4 d6 9. Nc4 Bg4 10. Nxa5 Qd7 11. Nd2 h6 12. f3 Bh5 13. f4 Nge7 14. f5 g5 15.
Be2 a6 16. Ndc4 g4 17. h3 Rg8 18. hxg4 Bxg4 19. Bxh6 Bxf5 20. exf5 Nxf5 21. Rf1
Qe6 22. Bg4 Rxg4 23. Ne3 Rxa4 24. Rxf5 Rxa5 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=10002695,
            ),
        ],
    ),
    TournamentData(
        date=date(2023, 2, 26),
        location='Rezydencja J. Szachego',
        games=[
            GameData(
                gid=52,
                white='Stoned Qń',
                black='Husarski Generał',
                pgn='''1. e4 d6 2. Bb5+ c6 3. Bc4 Nf6 4. d3 d5 5. Nc3 dxc4 6. dxc4 e6 7. e5 Bb4 8. a3
Bxc3+ 9. bxc3 Qxd1+ 10. Kxd1 Ne4 11. f3 Nf2+ 12. Ke1 Nxh1 13. f4 O-O 14. c5 g6
15. Nf3 Nd7 16. Ng5 Nxc5 17. Be3 Na4 18. Ke2 Nxc3+ 19. Kd2 Nd5 20. Bc5 Rd8 21.
Rxh1 Nxf4+ 22. Ke3 Nd5+ 23. Ke4 b6 24. Be7 Nxe7 25. Rf1 Rf8 26. h4 Ba6 27. Rf6
h6 28. Nxf7 Rxf7 29. Rxe6 Kg7 30. g4 Rc8 31. g5 hxg5 32. hxg5 c5 33. a4 c4 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=10134589,
            ),
            GameData(
                gid=53,
                white='Jerzy Szachy',
                black='Husarski Generał',
                pgn='''1. d4 d5 2. Bf4 Nc6 3. e3 f5 4. Bd3 a6 5. Nf3 h6 6. O-O g5 7. Be5 g4 8. Bxh8
gxf3 9. Qxf3 e6 10. Qh5+ Ke7 11. Qh4+ Kf7 12. Qxd8 Nxd8 13. Nd2 Ke8 14. f3 Nf7
15. Be5 Bb4 16. c3 Ba5 17. e4 dxe4 18. fxe4 fxe4 19. Bxe4 c6 20. Bg6 Bd7 21.
Bxf7+ Kf8 22. Bxe6+ Ke7 23. Rf7+ Kxe6 24. Raf1 Be8 25. Rf8 Ne7 26. R1f6+ Kd7 27.
Rd6+ Kc7 28. Rxh6+ Kb6 29. Nc4+ Kb5 30. Nxa5 Kxa5 31. Rhh8 Ng6 32. Rxe8 Nxh8 33.
Rxh8 Rxh8 34. Bxh8 b6 35. h4 b5 36. h5 Ka4 37. h6 b4 38. h7 bxc3 39. bxc3 Ka3
40. Be5 Kxa2 41. h8=Q a5 42. Qa8 Kb3 43. Qb7+ Kxc3 44. d5+ Kc4 45. dxc6 a4 46.
c7 a3 47. c8=Q+''',
                score=2,
                termination=Termination.RESIGNATION,
                chess_com_embed=10135297,
            ),
            GameData(
                gid=54,
                white='Fryderyk Szopen',
                black='Pion Forward',
                pgn='''1. e4 Nf6 2. Nc3 e5 3. d4 d5 4. Nxd5 Bg4 5. f3 Nxd5 6. dxe5 Bb4+ 7. c3 Ne3 8.
Qa4+ Nc6 9. Bxe3 Be6 10. cxb4 a5 11. f4 Qh4+ 12. g3 Qh5 13. b5 Nb4 14. b6+ c6
15. Bd2 Nc2+ 16. Qxc2 Ra6 17. Bxa6 bxa6 18. b7 O-O 19. Qxc6 a4 20. Qxa6 g5 21.
Bb4 Rd8 22. Qa8 Rxa8 23. bxa8=Q+ Kg7 24. Bf8+ Kg6 25. Be7 Bg4 26. Qg8+ Kh6 27.
Bf8# 1-0''',
                score=2,
                termination=Termination.CHECKMATE,
                chess_com_embed=10135301,
            ),
            GameData(
                gid=55,
                white='Husarski Generał',
                black='Jerzy Szachy',
                pgn='''1. Nf3 d5 2. d4 Nf6 3. Bg5 Nbd7 4. Bxf6 Nxf6 5. Nc3 e6 6. h3 Bd6 7. g4 O-O 8. a3
c5 9. dxc5 Bxc5 10. b4 Bb6 11. e3 Ne4 12. Nxe4 dxe4 13. Ng5 h6 14. Nxe4 Qd5 15.
Bd3 f5 16. gxf5 exf5 17. Ng3 Bc7 18. Bxf5 Qe5 19. Qd4 Qxd4 20. exd4 Bxf5 21.
Nxf5 Rae8+ 22. Kd2 Rxf5 23. Rhf1 Bf4+ 24. Kd3 Bg5 25. Rae1 Rxe1 26. Rxe1 Rf3+
27. Ke2 Rxh3 28. f3 h5 29. Kf2 Rh2+ 30. Kg3 Rxc2 31. f4 Bf6 32. Re8+ Kf7 33. Ra8
Rc3+ 34. Kg2 Rxa3 35. Rd8 Bxd8 36. d5 Ra4 37. Kf3 Rxb4 38. d6 a5 39. f5 a4 0-1''',
                score=0,
                termination=Termination.RESIGNATION,
                chess_com_embed=10135305,
            ),
            GameData(
                gid=56,
                white='Pion Forward',
                black='Fryderyk Szopen',
                pgn='''1. e4 Nf6 2. Nc3 c6 3. g4 d5 4. f3 dxe4 5. fxe4 Bxg4 6. Be2 h5 7. Nf3 Bxf3 8.
Bxf3 e5 9. d3 Bb4 10. Bd2 Qa5 11. a3 Bd6 12. d4 exd4 13. Na4 Qxa4 14. b3 Qa6 15.
Rg1 Nbd7 16. Rxg7 Bxh2 17. c4 Nc5 18. e5 Nd3+ 19. Ke2 Nxe5 20. Bb4 Nxf3 21. Kxf3
b5 22. Qxd4 Qb7 23. Qxf6 c5+ 24. Ke3 Qe7+ 25. Qxe7+ Kxe7 26. Bxc5+ Kf6 27. Rg2
Rhe8+ 28. Kd4 Be5+ 29. Ke3 Bxa1+ 30. Kd3 Rad8+ 31. Kc2 bxc4 32. bxc4 a6 33. Rh2
Rd4 34. Bxd4+ Bxd4 35. Rxh5 Re2+ 36. Kd1 Ra2 37. Rh6+ Kg7 38. Rxa6 Ra1+ 39. Kd2
f6 40. Kd3 Rd1+ 41. Ke4 Kg6 42. a4 Kg5 43. Kf3 f5 44. Ke2 Rc1 45. Rd6 Rxc4 46.
Kd3 Rxa4 47. Rxd4 Rxd4+ 48. Kxd4 f4 49. Ke4 Kg4 50. Kd3 f3 51. Kd2 f2 52. Ke2
Kg3 53. Kf1 Kf3 1/2-1/2''',
                score=1,
                termination=Termination.STALEMATE,
                chess_com_embed=10135315,
            ),
        ],
    ),
]
