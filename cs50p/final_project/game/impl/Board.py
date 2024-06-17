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
        return tuple(
            idx for idx, item in enumerate(self.__cells) if item.is_empty()
        )

    def is_empty(self):
        return not self.is_won()

    def is_won(self) -> bool:
        return False

    def is_done(self) -> bool:
        return len(self.available_moves()) == 0

    def get_winner(self) -> ABCPlayer:
        return None

    def value(self) -> ABCPlayer:
        return self.get_winner()

    @property
    def size(self) -> int:
        return self.__size

    @property
    def dimensions(self) -> int:
        return self.__dimensions

    @property
    def inception(self) -> int:
        return self.__inception

    @property
    def cells(self) -> Tuple[HasValue]:
        return (
            (item if item.value is not None else idx)
            for idx, item in enumerate(self.__cells)
        )

    @property
    def cells_filler(self) -> Tuple[HasValue]:
        return (
            (item if item.value is not None else chr(32))
            for item in self.__cells
        )

    def make_move(self, idx: int, item: ABCPlayer) -> None:
        self.__cells[idx].value = item
