from dataclasses import dataclass, field
from typing import Any, Iterable, Set, Tuple

from engine.abstracts import CanBeEmpty, HasWinner, Moves, Playable
from engine.cell import Cell


@dataclass
class Board(Playable, CanBeEmpty, HasWinner):
    size: int
    dimensions: int
    inception: int
    win_combinations: Set[Tuple[int]]
    cells: Tuple[CanBeEmpty, ...] = field(init=False)

    def __post_init__(self):
        if self.inception == 0:
            self.cells = tuple(Cell() for _ in range(self.size**self.dimensions))
        else:
            self.cells = tuple(
                Board(self.size, self.dimensions, self.inception - 1, self.win_combinations)
                for _ in range(self.size**self.dimensions)
            )

    def is_empty(self) -> bool:
        return any(cell.is_empty() for cell in self.cells)

    def get_available_moves(self) -> Moves[int]:
        if self.inception == 0:
            return tuple(idx for idx, cell in enumerate(self.cells) if cell.is_empty())

        result = {
            idx: cell.get_available_moves()
            for idx, cell in enumerate(self.cells)
            if cell.is_empty()
        }
        return result

    def place_move(self, move: Iterable[int], player: Any) -> None:
        raise NotImplementedError

    def __get_winner(self) -> None:
        for combination in self.win_combinations:
            cell_values = {self.cells[idx].value for idx in combination}
            if len(cell_values) == 1 and cell_values[0] is not None:
                return cell_values.pop()
        return None

    @property
    def value(self) -> Any:
        return self.__get_winner()
