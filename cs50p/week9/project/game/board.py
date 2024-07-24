from dataclasses import dataclass, field
from typing import Hashable, OrderedDict, Set, Tuple
from game.abstracts import Calculable, Valuable, Winnable


@dataclass
class Board(Winnable):
    size: int
    dimentions: int
    inception: int
    calc_win_combinations: Calculable
    wins: Set[Tuple[int, ...]] = field(init=False)
    moves: OrderedDict[int, Valuable] = field(init=False, default_factory=OrderedDict)

    def __post_init__(self):
        self.wins = self.calc_win_combinations(self.size, self.dimentions)

    def available_moves(self) -> tuple[int, ...]:
        existing_moves = tuple(item for item in self.moves)
        return tuple(idx for idx in range(self.size**self.dimentions) if idx not in existing_moves)

    @property
    def value(self) -> Hashable | None:
        raise NotImplementedError

    def place_move(self, idx: int, value: Valuable) -> None:
        if idx not in self.available_moves():
            raise ValueError(f"Invalid move {idx=}")
        self.moves[idx] = value
