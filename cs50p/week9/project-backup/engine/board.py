from collections import defaultdict
from typing import MutableSequence, Tuple
from engine.abstracts import Movable, Moves, Valuable, Winnable
from engine.cell import Cell

type BoardCell = Valuable | Winnable
type BoardCollection = Tuple[BoardCell, ...]
type Value = Movable | None


class Board(Winnable):
    _board: BoardCollection

    def __init__(self, size: int, dimensions: int, inception: int) -> None:
        self._winner: Value = None
        self._last_move: int = -1

        if inception < 1:
            self._board = tuple(Cell() for _ in range(size**dimensions))
        else:
            self._board = tuple(
                Board(size, dimensions, inception - 1) for _ in range(size**dimensions)
            )

    @property
    def available_moves(self) -> Moves:
        result = {}
        for idx, cell in enumerate(self._board):
            if cell.is_empty or (self._last_move > -1 and idx == self._last_move):
                if isinstance(cell, Winnable):
                    result[idx] = result.get(idx, ()) + cell.available_moves
                else:
                    result[idx] = result.get(idx, ()) + (idx,)
        return result

    @property
    def winner(self) -> Value:
        return self._winner

    def make_move(self, move: MutableSequence[int], player: Movable) -> None:
        current_move = move.pop()
        cell = self._board[current_move]
        if isinstance(cell, Winnable):
            self._last_move = current_move
            cell.make_move(move, player)
        else:
            cell.value = player

    @property
    def is_empty(self) -> bool:
        return self._winner is None
