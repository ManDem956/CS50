from dataclasses import dataclass, field
from typing import Any, List, Set, Tuple

from engine.abstracts import CanBeEmpty, Moves, Playable
from engine.cell import Cell


@dataclass
class Board(Playable):
    size: int
    dimensions: int
    inception: int
    wins: Set[Tuple[int]]
    cells: Tuple[CanBeEmpty, ...] = field(init=False)

    def __post_init__(self):
        if self.inception == 0:
            self.cells = tuple(Cell() for _ in range(self.size**self.dimensions))
        else:
            self.cells = tuple(
                Board(self.size, self.dimensions, self.inception - 1, self.wins)
                for _ in range(self.size**self.dimensions)
            )

    def is_empty(self) -> bool:
        if self.value is not None:
            return False
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

    def place_move(self, move: List[int], player: Any) -> None:
        if len(move) != self.inception + 1:
            raise ValueError("Invalid move")

        current_move = move.pop()

        if current_move not in self.get_available_moves():
            raise ValueError("Invalid move")

        if self.inception == 0:
            self.cells[current_move].value = player
        else:
            self.cells[current_move].place_move(move, player)

    def __get_winner(self) -> Any:
        for combination in self.wins:
            cell_values = {self.cells[idx].value for idx in combination}
            result = cell_values.pop()
            if len(cell_values) == 0 and result is not None:
                return result
        return None

    @property
    def value(self) -> Any:
        return self.__get_winner()
