
from collections.abc import Collection
from typing import Any, Protocol


class Playable(Protocol):

    def calculate_move(moves: Collection[int]) -> int:
        """Calculates next move"""


class Valuable(Protocol):

    @property
    def value() -> Any:
        """COntacin nullable value"""


class Winnable(Valuable, Protocol):

    def available_moves() -> Collection[int]:
        """Returns number of available moves"""

    def place_move(idx: int, value: Playable):
        """Places player's move"""

    def get_winner() -> Any:
        """Returns current winner"""
