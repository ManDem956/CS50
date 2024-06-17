from typing import Tuple

from game.abstract import HasValue
from game.impl.Players import ABCPlayer


class Cell:
    def __init__(self, value: ABCPlayer = None) -> None:
        self._value = value

    @property
    def value(self) -> ABCPlayer:
        return self._value

    @value.setter
    def value(self, value: ABCPlayer) -> None:
        self._value = value

    def is_empty(self) -> bool:
        return self._value is None

    def __str__(self) -> str:
        if self._value is None:
            return None
        return str(self._value)

    def __repr__(self) -> str:
        return str(self._value)

    def __bool__(self) -> bool:
        return bool(self._value)


class Board:
    def __init__(self, cells_count: int, inception: int) -> None:
        self._cells = self.__fill_cells(cells_count, inception=inception)

    def __fill_cells(self, cells_count: int, inception: int):
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

    def available_moves(self) -> Tuple[int]:
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

    def is_won(self) -> bool:
        """
        Returns True if the board is won.

        :return: A boolean value indicating if the board is won.
        :rtype: bool
        """
        return False

    def is_done(self) -> bool:
        """
        Check if the game is completed regardless of the result.

        Returns:
            bool: True if there are no more available moves, False otherwise.
        """
        return len(self.available_moves()) == 0

    def get_winner(self) -> ABCPlayer:
        """
        Returns the winner of the board.

        :return: An ABCPlayer representing the winner of the board.
        :rtype: ABCPlayer
        """
        return None

    def value(self) -> ABCPlayer:
        """
        Returns the value of the board is the the board itself is a cell.

        :return: An ABCPlayer representing the winner of the board.
        :rtype: ABCPlayer
        """
        return self.get_winner()

    @property
    def cells(self) -> Tuple[HasValue]:
        """
        Returns a tuple of cells, where each cell is either the cell itself if it
        has a value, or its index if it doesn't.
        """
        return self._cells

    def make_move(self, cell_index: int, player: ABCPlayer) -> None:
        if cell_index not in self.available_moves():
            raise ValueError("Invalid move")
        self._cells[cell_index].value = player
