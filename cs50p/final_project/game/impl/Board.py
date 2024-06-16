from typing import Any, Tuple

from game.abstract import HasValue, Movable


class Cell:

    def __init__(self, value: Any = None) -> None:
        self.__value = value

    @property
    def value(self) -> Movable:
        return self.__value

    @value.setter
    def value(self, value: Movable) -> None:
        self.__value = value

    def is_empty(self) -> bool:
        return self.__value is None


class Board:

    def __init__(
        self, size: int = 3, dimensions: int = 2, inception: int = 0
    ) -> None:
        if size < 3:
            raise ValueError("Board size must be at least 3")
        if dimensions < 2:
            raise ValueError("Board dimensions must be at least 2")
        if inception < 0:
            raise ValueError("Board inception must be at least 0")
        self.__size = size
        self.__dimensions = dimensions
        self.__inception = inception
        self.__cells = self.__fill_cells(inception=self.__inception)

    def __fill_cells(self, inception=int):
        if inception == 0:
            return (Cell(),) * (self.__size**self.__dimensions)
        return (
            Board(
                size=self.__size,
                dimensions=self.__dimensions,
                inception=inception - 1,
            ),
        ) * (self.__size**self.__dimensions)

    def available_moves(self) -> Tuple[int]:
        return tuple(
            idx for idx, item in enumerate(self.__cells) if item.is_empty()
        )

    def is_empty(self):
        return not self.is_won()

    def is_won(self) -> bool:
        return False

    def get_winner(self) -> Movable:
        return None

    def value(self) -> Movable:
        return self.get_winner()

    @property
    def cells(self) -> Tuple[HasValue]:
        return self.__cells
