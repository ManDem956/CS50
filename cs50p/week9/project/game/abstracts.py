from dataclasses import dataclass
from typing import Hashable, Protocol, Set, Tuple


@dataclass
class Valuable(Hashable, Protocol):

    @property
    def value(self) -> Hashable:
        ...


@dataclass
class Player(Valuable, Protocol):

    def calculate_move(self, Winnable) -> int:
        """Calculate next move"""
        ...


class Calculable(Protocol):
    def __call__(self, size: int, dimensions: int) -> Set[Tuple[int]]:
        """Mehtod to calculate win combinations"""
        ...


class Winnable(Valuable, Protocol):

    def place_move(self, idx: int, value: Valuable) -> None:
        """Place move"""
        ...

    def available_moves(self) -> tuple[int]:
        """Get available moves"""
        ...

    def undo_last_move(self) -> None:
        """Undo the last move"""
        ...

    @property
    def last_move(self) -> int:
        """Get last move"""
        ...