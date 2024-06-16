from typing import Any, Protocol, Tuple


class HasValue(Protocol):
    def value(self) -> Any:
        """Can query the cell value"""

    def is_empty(self) -> bool:
        """Cen query it's empty status"""


class Movable(Protocol):
    def symbol(self) -> Any:
        """Returns the symbol of the player"""

    def get_move(self, available_moves: Tuple[int]) -> int:
        """Returns the next player move"""


class Playable(Protocol):
    def available_moves(self) -> Tuple[int]:
        """Returns the list if indices of available moves"""

    def is_won(self) -> bool:
        """Returns True if the board is won"""

    def get_winner(self) -> bool:
        """Returns the winner of the board"""

    def make_move(self, idx: int) -> None:
        """Returns the winner of the board"""
