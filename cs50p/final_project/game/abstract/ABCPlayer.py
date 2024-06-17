from abc import ABC
from dataclasses import dataclass
from typing import Any, Tuple


@dataclass
class ABCPlayer(ABC):
    name: str
    token: Any

    def get_move(self, available_moves: Tuple[int]) -> int: ...

    def __str__(self) -> str:
        return self.token
