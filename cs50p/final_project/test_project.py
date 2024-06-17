from contextlib import nullcontext as does_not_raise
from typing import Tuple
import pytest

from game.abstract.ABCPlayer import ABCPlayer
from game.impl.Board import Board, Cell


@pytest.fixture
def default_board() -> Board:
    return Board(9, 0)


@pytest.fixture
def default_player(mocker) -> ABCPlayer:
    return mocker.patch.object(ABCPlayer, "get_move")

@pytest.fixture
def full_board(default_board: Board) -> Board:
    for i in range(9):
    pass


@pytest.mark.parametrize(
    "input,expected",
    [
        (None, True),
        ("x", False),
        ("o", False),
    ],
)
def test_cell(input: bool, expected: bool) -> None:
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
        ((5, 8, 0, 4, 2, 1), (3, 6, 7), does_not_raise()),
        ((5, 8, 0, 4, 2, 1, 7), (3, 6), does_not_raise()),
        ((5, 8, 0, 4, 2, 1, 7, 6), (3,), does_not_raise()),
        ((5, 8, 0, 4, 2, 1, 7, 6, 3), (), does_not_raise()),
    ],
)
def test_board_availability(
    default_board: Board, default_player: ABCPlayer, input: Tuple[int], expected: int, expectation
) -> None:
    if input is not None:
        with expectation:
            for move in input:
                default_board.make_move(move, default_player)

    assert len(default_board.available_moves()) == len(expected)
    assert default_board.available_moves() == expected
