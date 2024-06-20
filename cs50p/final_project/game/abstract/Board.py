from typing import Iterable, Protocol, Tuple

from game.abstract.ABCPlayer import ABCPlayer

type Value = ABCPlayer | Playable | None


class Playable(Protocol):
    def available_moves(self) -> Tuple[int]:  # type: ignore
        """Returns the list if indices of available moves"""

    def is_done(self) -> bool:  # type: ignore
        """Returns True if the board is won"""

    def get_winner(self, win_conditions: Iterable[Iterable[int]]) -> Value | None:  # type: ignore
        """Returns the winner of the board"""

    def make_move(self, idx: int) -> None:
        """Places player's move on the board"""
