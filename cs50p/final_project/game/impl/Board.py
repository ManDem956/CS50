from typing import Iterable, Tuple

from game.abstract.Board import Value
from game.abstract.Cell import HasValue
from game.impl.Players import ABCPlayer


class Cell:
    def __init__(self, value: Value = None) -> None:
        self._value = value

    @property
    def value(self) -> Value:
        return self._value

    @value.setter
    def value(self, value: Value) -> None:
        self._value = value

    def is_empty(self) -> bool:
        return self._value is None

    def __str__(self) -> str | None:
        if self._value is None:
            return None
        return str(self._value)

    def __repr__(self) -> str:
        return str(self._value)

    def __bool__(self) -> bool:
        return bool(self._value)


class Board:
    def __init__(self, cells_count: int, inception: int) -> None:
        self._cells: Tuple[HasValue, ...] = self.__fill_cells(cells_count, inception=inception)

    def __fill_cells(self, cells_count: int, inception: int) -> Tuple[HasValue, ...]:
        """
        Fills the cells of the board based on the inception level.

        Args:
            inception (int): The inception level for filling the cells.

        Returns:
            tuple: A tuple of Cell objects representing the filled cells.
        """
        if inception == 0:
            return tuple(Cell() for _ in range(cells_count))
        return tuple(
            Board(
                cells_count,
                inception=inception - 1,
            )
            for _ in range(cells_count)
        )

    def available_moves(self) -> Tuple[int, ...]:
        """
        Returns a tuple of available moves represented by their indices.
        """
        return tuple(idx for idx, item in enumerate(self._cells) if item.is_empty())

    def is_empty(self):
        """
        Check if the board is empty when the current board is a cell.

        Returns:
            bool: True if the board is empty, False otherwise.
        """
        return not self.is_done()

    def is_done(self) -> bool:
        """
        Check if the game is completed regardless of the result.

        Returns:
            bool: True if there are no more available moves, False otherwise.
        """
        return len(self.available_moves()) == 0

    def get_winner(self, conditions: Iterable[Iterable[int]]) -> Value | None:
        """
        Check if any of the win conditions are satisfied.

        Args:
            conditions (Iterable[Iterable[int]]): The win conditions to check.

        Returns:
            Value | None: The value of the winner, or None if no winner.
        """
        for condition in conditions:
            values = [
                self._cells[index].value
                for index in condition
                if self._cells[index].value is not None
            ]
            if len(values) == len(condition) and len(set(values)) == 1:
                return values.pop()
        return None

    def value(self) -> Value:

        return None

    @property
    def cells(self) -> Tuple[Value, ...]:
        """
        Returns a tuple of cells, where each cell is either the cell itself if it
        has a value, or its index if it doesn't.
        """
        return self._cells

    def make_move(self, cell_index: int, player: ABCPlayer) -> None:
        if cell_index not in self.available_moves():
            raise ValueError("Invalid move")
        self._cells[cell_index].value = player
