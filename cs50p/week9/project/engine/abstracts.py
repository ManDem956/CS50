from typing import Any, Iterable, Protocol, Set


class Movable(Protocol):
    def choose_move(self, moves: Iterable[int]) -> int: ...


class Valuable(Protocol):

    @property
    def value(self) -> Any: ...

    def is_empty(self) -> bool: ...


class Playable(Protocol):
    def play(self) -> None: ...


class Winnable(Protocol):

    def available_moves(self) -> Set[int]: ...

    def winner(self) -> Any: ...
