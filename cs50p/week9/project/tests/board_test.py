
from dataclasses import dataclass
import itertools
import pytest
import random


from game.abstracts import Playable
from game.board import Board
from game.player import RandomPlayer

WINS_3x2 = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 5, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}


@dataclass
class MockPlayer(Playable):
    value: str

    def __str__(self) -> str:
        return self.value

    def __hash__(self) -> int:
        return hash(self.value)

    def calculate_move(self, moves: tuple[int]) -> int:
        return moves[0]


@pytest.fixture
def players():
    players = (RandomPlayer("x"), RandomPlayer("o"))
    return players


@pytest.fixture
def board(players, request, monkeypatch):
    random.seed(request.param[1])
    players_cycle = itertools.cycle(players)

    board = Board(*request.param[0])
    while len(board.available_moves()) > 0 and board.value is None:
        board.value = next(players_cycle)

    monkeypatch.setattr(Board, "available_moves", tmp)

    return board


@pytest.mark.parametrize("board, expected, winner", [(((3, 2, 0, {(0, 1, 2)}), ()), tuple(range(9)), None),
                                                     (((3, 2, 1, {(0, 1, 2)}), ()), tuple(range(9)), None)],
                         indirect=["board"])
def test_simple(board, expected, winner):
    assert board.available_moves() == expected
    assert board.value == winner


@pytest.mark.parametrize("players, board, expected, winner", [(None, ((3, 2, 0, WINS_3x2), 4242), tuple(sorted((5, 1, 7, 8))), 0),
                                                              (None, ((3, 2, 0, WINS_3x2), 42424242), tuple(range(9)), 0)],
                         indirect=["players", "board"])
def test_board_moves(players, board, expected, winner):
    assert board.available_moves() == expected
    assert board.value == players[0]
