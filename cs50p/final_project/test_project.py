from contextlib import nullcontext as does_not_raise
from typing import Dict, Iterable, Tuple

import pytest

from game.abstract.ABCPlayer import ABCPlayer
from game.abstract.Board import Playable, Value
from game.impl.Board import Board, Cell
from game.impl.Game import Game


@pytest.fixture
def default_board() -> Playable:
    return Board(9, 0)


@pytest.fixture
def default_game(default_player, another_player) -> Game:
    game = Game((default_player, another_player), 3, 2, 0)
    return game


@pytest.fixture
def win_conditions(default_game) -> Iterable[Iterable[int]]:
    return default_game._win_conditions


@pytest.fixture
def default_player(mocker) -> Value:
    return mocker.Mock(spec=ABCPlayer)


@pytest.fixture
def another_player(mocker) -> Value:
    return mocker.Mock(spec=ABCPlayer)


@pytest.fixture
def full_board(default_board: Playable, default_player: ABCPlayer) -> Playable:
    for i in range(9):
        default_board.make_move(i, default_player)
    return default_board


@pytest.mark.parametrize(
    "input,expected",
    [
        (None, True),
        ("x", False),
        ("o", False),
    ],
)
def test_cell(input: bool, expected: Playable) -> None:
    cell = Cell()
    if input is not None:
        cell.value = input
    assert cell.is_empty() == expected


@pytest.mark.parametrize(
    "input, expected, expectation",
    [
        (None, (0, 1, 2, 3, 4, 5, 6, 7, 8), does_not_raise()),
        ((5,), (0, 1, 2, 3, 4, 6, 7, 8), does_not_raise()),
        ((5, 8), (0, 1, 2, 3, 4, 6, 7), does_not_raise()),
        ((5, 8, 0), (1, 2, 3, 4, 6, 7), does_not_raise()),
        ((5, 8, 0, 4), (1, 2, 3, 6, 7), does_not_raise()),
        ((5, 8, 0, 4, 2), (1, 3, 6, 7), does_not_raise()),
        ((5, 8, 0, 4, 2, 5), (1, 3, 6, 7), pytest.raises(ValueError)),
        ((5, 8, 0, 4, 2, 8), (1, 3, 6, 7), pytest.raises(ValueError)),
        ((5, 8, 0, 4, 2, 1), (3, 6, 7), does_not_raise()),
        ((5, 8, 0, 4, 2, 1, 7), (3, 6), does_not_raise()),
        ((5, 8, 0, 4, 2, 1, 7, 6), (3,), does_not_raise()),
        ((5, 8, 0, 4, 2, 1, 7, 6, 3), (), does_not_raise()),
    ],
)
def test_board_availability(
    default_board: Playable,
    default_player: ABCPlayer,
    input: Tuple[int],
    expected: int,
    expectation,
) -> None:
    if input is not None:
        with expectation:
            for move in input:
                default_board.make_move(move, default_player)

    assert len(default_board.available_moves()) == len(expected)
    assert default_board.available_moves() == expected


def test_full_board(full_board: Playable) -> None:
    assert full_board.is_done()


@pytest.mark.parametrize(
    "moves, expected",
    [
        ({1: "default_player", 2: "default_player", 0: "default_player"}, "default_player"),
        ({1: "default_player", 2: "default_player", 0: "another_player"}, None),
        ({2: "default_player", 4: "default_player", 6: "default_player"}, "default_player"),
        ({2: "default_player", 4: "default_player", 6: "another_player"}, None),
        ({0: "default_player", 3: "default_player", 6: "default_player"}, "default_player"),
        ({0: "default_player", 3: "default_player", 6: "another_player"}, None),
        ({3: "default_player", 4: "default_player", 5: "default_player"}, "default_player"),
        ({3: "default_player", 4: "default_player", 5: "another_player"}, None),
        ({6: "default_player", 7: "default_player", 8: "default_player"}, "default_player"),
        ({6: "default_player", 7: "default_player", 8: "another_player"}, None),
        ({2: "default_player", 5: "default_player", 8: "default_player"}, "default_player"),
        ({2: "default_player", 5: "default_player", 8: "another_player"}, None),
        ({1: "default_player", 4: "default_player", 7: "default_player"}, "default_player"),
        ({1: "default_player", 4: "default_player", 7: "another_player"}, None),
        ({0: "default_player", 4: "default_player", 8: "default_player"}, "default_player"),
        ({0: "default_player", 4: "default_player", 8: "another_player"}, None),
    ],
)
def test_get_winner(
    default_board: Playable,
    win_conditions: Iterable[Iterable[int]],
    moves: Dict[int, str],
    expected: str,
    request,
) -> None:
    if expected is not None:
        expected = request.getfixturevalue(expected)
    for key, value in moves.items():
        default_board.make_move(key, request.getfixturevalue(value))
    assert default_board.get_winner(win_conditions) == expected


# @pytest.mark.parametrize(
#     "params, expected",
#     [
#         (
#             (3, 2),
#             {
#                 (0, 1, 2),
#                 (3, 4, 5),
#                 (6, 7, 8),
#                 (0, 3, 6),
#                 (1, 4, 7),
#                 (2, 5, 8),
#                 (0, 4, 8),
#                 (2, 4, 6),
#             },
#         ),
#         (
#             (3, 3),
#             {
#                 (0, 4, 8),
#                 (11, 13, 15),
#                 (0, 13, 26),
#                 (11, 14, 17),
#                 (18, 21, 24),
#                 (2, 10, 18),
#                 (0, 3, 6),
#                 (2, 11, 20),
#                 (0, 12, 24),
#                 (4, 13, 22),
#                 (21, 22, 23),
#                 (6, 16, 26),
#                 (9, 13, 17),
#                 (0, 10, 20),
#                 (6, 7, 8),
#                 (18, 19, 20),
#                 (9, 12, 15),
#                 (6, 15, 24),
#                 (0, 1, 2),
#                 (8, 17, 26),
#                 (1, 4, 7),
#                 (15, 16, 17),
#                 (1, 13, 25),
#                 (5, 14, 23),
#                 (0, 9, 18),
#                 (9, 10, 11),
#                 (6, 12, 18),
#                 (7, 16, 25),
#                 (6, 13, 20),
#                 (2, 14, 26),
#                 (8, 16, 24),
#                 (5, 13, 21),
#                 (3, 13, 23),
#                 (10, 13, 16),
#                 (2, 5, 8),
#                 (24, 25, 26),
#                 (8, 14, 20),
#                 (8, 13, 18),
#                 (2, 13, 24),
#                 (20, 23, 26),
#                 (1, 10, 19),
#                 (19, 22, 25),
#                 (3, 4, 5),
#                 (7, 13, 19),
#                 (3, 12, 21),
#                 (18, 22, 26),
#                 (2, 4, 6),
#                 (20, 22, 24),
#                 (12, 13, 14),
#             },
#         ),
#         (
#             (4, 3),
#             {
#                 (15, 26, 37, 48),
#                 (0, 5, 10, 15),
#                 (28, 29, 30, 31),
#                 (2, 22, 42, 62),
#                 (11, 26, 41, 56),
#                 (15, 31, 47, 63),
#                 (24, 25, 26, 27),
#                 (10, 26, 42, 58),
#                 (5, 21, 37, 53),
#                 (18, 22, 26, 30),
#                 (44, 45, 46, 47),
#                 (19, 23, 27, 31),
#                 (11, 27, 43, 59),
#                 (51, 54, 57, 60),
#                 (14, 26, 38, 50),
#                 (34, 38, 42, 46),
#                 (13, 25, 37, 49),
#                 (0, 17, 34, 51),
#                 (2, 18, 34, 50),
#                 (56, 57, 58, 59),
#                 (48, 53, 58, 63),
#                 (8, 9, 10, 11),
#                 (32, 33, 34, 35),
#                 (51, 55, 59, 63),
#                 (17, 21, 25, 29),
#                 (14, 30, 46, 62),
#                 (1, 5, 9, 13),
#                 (15, 30, 45, 60),
#                 (0, 21, 42, 63),
#                 (13, 29, 45, 61),
#                 (12, 13, 14, 15),
#                 (8, 24, 40, 56),
#                 (9, 25, 41, 57),
#                 (4, 20, 36, 52),
#                 (3, 19, 35, 51),
#                 (0, 20, 40, 60),
#                 (3, 7, 11, 15),
#                 (33, 37, 41, 45),
#                 (32, 37, 42, 47),
#                 (12, 24, 36, 48),
#                 (2, 6, 10, 14),
#                 (35, 38, 41, 44),
#                 (3, 18, 33, 48),
#                 (3, 23, 43, 63),
#                 (3, 22, 41, 60),
#                 (7, 22, 37, 52),
#                 (0, 16, 32, 48),
#                 (48, 52, 56, 60),
#                 (40, 41, 42, 43),
#                 (8, 25, 42, 59),
#                 (0, 1, 2, 3),
#                 (36, 37, 38, 39),
#                 (60, 61, 62, 63),
#                 (35, 39, 43, 47),
#                 (49, 53, 57, 61),
#                 (20, 21, 22, 23),
#                 (50, 54, 58, 62),
#                 (4, 21, 38, 55),
#                 (12, 28, 44, 60),
#                 (7, 23, 39, 55),
#                 (6, 22, 38, 54),
#                 (1, 17, 33, 49),
#                 (16, 17, 18, 19),
#                 (12, 25, 38, 51),
#                 (15, 27, 39, 51),
#                 (0, 4, 8, 12),
#                 (3, 6, 9, 12),
#                 (16, 21, 26, 31),
#                 (1, 21, 41, 61),
#                 (48, 49, 50, 51),
#                 (16, 20, 24, 28),
#                 (52, 53, 54, 55),
#                 (12, 29, 46, 63),
#                 (4, 5, 6, 7),
#                 (19, 22, 25, 28),
#                 (32, 36, 40, 44),
#             },
#         ),
#     ],
# )
# def test_generate_win_conditions(default_game, params, expected):
#     assert len(default_game._win_conditions - expected) == 0
