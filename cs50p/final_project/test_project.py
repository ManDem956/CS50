from contextlib import nullcontext as does_not_raise
from typing import Dict, Iterable, Tuple

import pytest

from game.abstract.ABCPlayer import ABCPlayer
from game.abstract.Board import Playable, Value
from game.impl.Board import Board, Cell
from game.impl.Game import Game

from tests import CONST_WIN_CONDITIONS


@pytest.fixture
def default_board() -> Playable:
    return Board(9, 0)


@pytest.fixture
def default_game(players) -> Game:
    game = Game(players, 3, 2, 0)
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
def players(default_player, another_player) -> Tuple[ABCPlayer, ABCPlayer]:
    return (default_player, another_player)


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
        ({1: 0, 2: 0, 0: 0}, 0),
        ({1: 0, 2: 0, 0: 1}, None),
        ({2: 0, 4: 0, 6: 0}, 0),
        ({2: 0, 4: 0, 6: 1}, None),
        ({0: 0, 3: 0, 6: 0}, 0),
        ({0: 0, 3: 0, 6: 1}, None),
        ({3: 0, 4: 0, 5: 0}, 0),
        ({3: 0, 4: 0, 5: 1}, None),
        ({6: 0, 7: 0, 8: 0}, 0),
        ({6: 0, 7: 0, 8: 1}, None),
        ({2: 0, 5: 0, 8: 0}, 0),
        ({2: 0, 5: 0, 8: 1}, None),
        ({1: 0, 4: 0, 7: 0}, 0),
        ({1: 0, 4: 0, 7: 1}, None),
        ({0: 0, 4: 0, 8: 0}, 0),
        ({0: 0, 4: 0, 8: 1}, None),
    ],
)
def test_get_winner(
    default_board: Playable,
    players: Tuple[ABCPlayer, ABCPlayer],
    win_conditions: Iterable[Iterable[int]],
    moves: Dict[int, str],
    expected: str,
    request,
) -> None:
    if expected is not None:
        expected = players[expected]

    for key, value in moves.items():
        default_board.make_move(key, players[value])

    assert default_board.get_winner(win_conditions) == expected


@pytest.mark.parametrize(
    "params, expected",
    CONST_WIN_CONDITIONS,
)
def test_generate_win_conditions(players, params, expected):
    game = Game(players, *params)

    assert len(game._win_conditions ^ expected) == 0
