from contextlib import nullcontext as does_not_raise

from dataclasses import dataclass
import itertools
import pytest

from game.board import Board
from project import generate_win_combinations


@dataclass
class Player():
    value: str


@pytest.fixture
def player_x(monkeypatch):

    result = Player("x")
    return result


@pytest.fixture
def player_o(monkeypatch):

    result = Player("o")
    return result


@pytest.fixture
def players(player_x, player_o):
    return (player_x, player_o)


@pytest.fixture
def players_cycle(player_x, player_o):
    return itertools.cycle((player_x, player_o))


@pytest.fixture
def board(request, players_cycle):
    result = Board(request.param[0], request.param[1], request.param[2], generate_win_combinations)
    if isinstance(request.param[3], int):
        for i in range(request.param[3]):
            result.place_move(i, next(players_cycle))
    else:
        for i in request.param[3]:
            result.place_move(i, next(players_cycle))

    return result


@pytest.mark.parametrize(
    "board, expected",
    [
        ((3, 2, 0, 0), tuple(range(3**2))),
        ((3, 2, 0, 1), tuple(range(1, 3**2))),
        ((3, 2, 0, 9), tuple()),
        ((3, 2, 0, (5,)), tuple(set(range(3**2)) - set((5,)))),
        ((3, 2, 0, (5, 8, 0, 1)), tuple(set(range(3**2)) - set((5, 8, 0, 1)))),
        ((3, 3, 0, 0), tuple(range(3**3))),
        ((4, 3, 0, 0), tuple(range(4**3))),
    ],
    indirect=["board"]
)
def test_board_available_moves(board, expected):
    assert board.available_moves() == expected


@pytest.mark.parametrize(
    "board, moves, expected, expectation",
    [
        ((3, 2, 0, 0), (0,), tuple(set(range(3**2)) - set((0,))), does_not_raise()),
        ((3, 2, 0, 0), range(3**2), tuple(), does_not_raise()),
        ((3, 2, 0, 0), (9,), tuple(), pytest.raises(ValueError)),
        ((3, 2, 0, 0), (-1,), tuple(), pytest.raises(ValueError)),
        ((3, 2, 0, 0), ("-1",), tuple(), pytest.raises(ValueError)),
        ((3, 2, 0, 0), tuple(range((3**2)+1)), tuple(), pytest.raises(ValueError)),
    ],
    indirect=["board"]
)
def test_board_make_moves(players_cycle, board, moves, expected, expectation):
    with expectation:
        for i in moves:
            board.place_move(i, next(players_cycle))
        assert board.available_moves() == expected
