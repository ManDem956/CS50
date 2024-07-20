from dataclasses import dataclass, field
from typing import Set, Sized, Tuple
from .abstracts import Playable, Valuable, Value, Winnable

type cellValue = tuple[Cell, ...] | tuple[Board, ...]


@dataclass
class Cell(Valuable):
    _value: Value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


@dataclass
class Board(Winnable):
    _value: cellValue = field(init=False)
    size: int
    dimensions: int
    inception: int
    wins: Set[Tuple[int, ...]]
    last_move: int = field(init=False, default=-1)

    def __post_init__(self):
        if self.inception == 0:
            self._value = tuple(Cell(None) for _ in range(self.size**self.dimensions))
        else:
            self._value = tuple(
                Board(self.size, self.dimensions, self.inception - 1, self.wins)
                for _ in range(self.size**self.dimensions)
            )

    @property
    def value(self):
        for win in self.wins:
            result = set(self._value[idx].value for idx in win)
            if (res := result.pop()) is not None and len(result) == 0:
                return res
        return None

    @value.setter
    def value(self, value):
        idx = value.calculate_move(self.available_moves())
        self._value[idx].value = value

    def available_moves(self) -> Sized:
        return tuple(idx for idx, item in enumerate(self._value) if item.value is None or (self.last_move > 0 and idx == self.last_move))

    def get_winner(self) -> Playable | None:
        raise NotImplementedError
