from typing import Protocol, Tuple


class Playable(Protocol):
    def available_moves(self) -> Tuple[int]:
        """Returns the list if indices of available moves"""

    def is_won(self) -> bool:
        """Returns True if the board is won"""

    def is_done(self) -> bool:
        """Returns True if the board is won"""

    def get_winner(self) -> bool:
        """Returns the winner of the board"""

    def make_move(self, idx: int) -> None:
        """Places player's move on the board"""
