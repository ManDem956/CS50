from typing import Any, Tuple

from game.abstract import HasValue
from game.impl.Players import ABCPlayer


class Cell:

    def __init__(self, value: Any = None) -> None:
        self.__value = value

    @property
    def value(self) -> ABCPlayer:
        return self.__value

    @value.setter
    def value(self, value: ABCPlayer) -> None:
        self.__value = value

    def is_empty(self) -> bool:
        return self.__value is None

    def __str__(self) -> str:
        return str(self.__value)

    def __repr__(self) -> str:
        return str(self.__value)


class Board:
    __MIN_SIZE: int = 3
    __MIN_DIMENSION: int = 2
    __MIN_INCEPTION: int = 0

    def __init__(self, size: int = 3, dimensions: int = 2, inception: int = 0) -> None:
        """
        Initializes a new instance of the Board class.

        Args:
            size (int, optional): The size of the board. Defaults to 3.
            dimensions (int, optional): The number of dimensions of the board. Defaults to 2.
            inception (int, optional): The inception level of the board. Defaults to 0.

        Raises:
            ValueError: If the size is less than the minimum size, if the dimensions
            are less than the minimum dimensions, or if the inception level
            is less than the minimum inception level.

        Returns:
            None
        """
        if size < self.__MIN_SIZE:
            raise ValueError(f"Board size must be at least {self.__MIN_SIZE}")
        if dimensions < self.__MIN_DIMENSION:
            raise ValueError(f"Board dimensions must be at least {self.__MIN_DIMENSION}")
        if inception < self.__MIN_INCEPTION:
            raise ValueError(f"Board inception must be at least {self.__MIN_INCEPTION}")
        self.__size = size
        self.__dimensions = dimensions
        self.__inception = inception
        self.__cells = self.__fill_cells(inception=self.__inception)

    def __fill_cells(self, inception: int):
        """
        Fills the cells of the board based on the inception level.

        Args:
            inception (int): The inception level for filling the cells.

        Returns:
            tuple: A tuple of Cell objects representing the filled cells.
        """
        if inception == 0:
            return tuple(Cell() for _ in range(self.__size**self.__dimensions))
        return tuple(
            Board(
                size=self.__size,
                dimensions=self.__dimensions,
                inception=inception - 1,
            )
            for _ in range(self.__size**self.__dimensions)
        )

    def available_moves(self) -> Tuple[int]:
        """
        Returns a tuple of available moves represented by their indices.
        """
        return tuple(idx for idx, item in enumerate(self.__cells) if item.is_empty())

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
    def board_size(self) -> int:
        """
        Returns the size of the board.

        :return: An integer representing the size of the board.
        :rtype: int
        """
        return self.__size

    @property
    def dimensions(self) -> int:
        """
        Returns the number of dimensions of the board.

        :return: An integer representing the number of dimensions of the board.
        :rtype: int
        """
        return self.__dimensions

    @property
    def inception(self) -> int:
        """
        Returns the inception level of the board.
        """
        return self.__inception

    @property
    def cells(self) -> Tuple[HasValue]:
        """
        Returns a tuple of cells, where each cell is either the cell itself if it
        has a value, or its index if it doesn't.
        """
        return tuple(
            cell if cell.value is not None else idx for idx, cell in enumerate(self.__cells)
        )

    @property
    def filled_cells(self) -> Tuple[HasValue]:
        """
        Returns a tuple of cells that have a value.

        :return: A tuple of cells that have a value.
        :rtype: Tuple[HasValue]
        """
        return tuple(cell for cell in self.__cells if cell.value is not None)

    def make_move(self, cell_index: int, player: ABCPlayer) -> None:
        self.__cells[cell_index].value = player
