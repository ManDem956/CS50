from typing import Any, Dict, Iterable, Protocol


type Moves[T] = Dict[T, Moves[T]]


class CanBeEmpty(Protocol):
    """An object that can be empty."""

    @property
    def value(self) -> Any: ...

    def is_empty(self) -> bool: ...


class Playable(Protocol):
    """An object that can be played."""

    def get_available_moves(self) -> Moves[int]: ...

    def place_move(self, move: Iterable[int], player: Any) -> None: ...


class CanMove(Protocol):
    """An object that can move."""

    def calculate_move(self, moves: Moves[int]) -> None: ...


class HasWinner(Protocol):
    """An object that has a winner."""

    def __get_winner(self) -> Any: ...
