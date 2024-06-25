from typing import Dict, Iterable, Protocol, Sequence, Tuple, runtime_checkable


type Moves[T] = T | Dict[T, Tuple[T]]


class Movable(Protocol):
    def choose_move(self, moves: Iterable[int]) -> int: ...


class CanBeEmpty(Protocol):
    @property
    def is_empty(self) -> bool: ...


@runtime_checkable
class Valuable(CanBeEmpty, Protocol):
    @property
    def value(self) -> Movable: ...

    @value.setter
    def value(self, value: Movable) -> None: ...


class Playable(Protocol):
    def play(self) -> None: ...


@runtime_checkable
class Winnable(CanBeEmpty, Protocol):

    @property
    def available_moves(self) -> Moves: ...

    @property
    def winner(self) -> Playable: ...

    def make_move(self, move: Sequence[int], player: Movable) -> None: ...
