from abc import ABC
from dataclasses import dataclass
from typing import Hashable, Protocol


class Valuable(Hashable, Protocol):

    @property
    def value(self) -> Hashable:
        """retriurns a value"""


class Playable(Valuable, Protocol):

    def place_move(self, idx: int, value: Valuable) -> None:
        """Place move"""

    @property
    def last_move(self) -> int:
        """Get last move"""

    def undo(self) -> None:
        """Undo the last move"""


class Calculated(Valuable, Protocol):

    def calculate_move(self, board: Playable) -> int:
        """Calculate next move"""


class Available(Protocol):

    def get_available_moves(self, board: Playable) -> tuple[int]:
        """Get available moves"""


class Winnable(Protocol):

    def get_winner(self, board: Playable) -> Valuable | None:
        """Check if winner exists"""


@dataclass
class Manageable(ABC):
    moves_strategy: Available
    win_strategy: Winnable
