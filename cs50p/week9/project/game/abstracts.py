
from typing import Hashable, Protocol, Sized


type Value = (Playable | None)


class Playable(Hashable, Protocol):

    def calculate_move(self, moves: tuple[int]) -> int:
        """Calculates next move"""
        ...


class Valuable(Protocol):
    _value: Value

    @property
    def value(self):
        ...

    @value.setter
    def value(self, value):
        ...


class Winnable(Valuable, Protocol):

    def available_moves(self) -> Sized:
        """Returns number of available moves"""
        ...
