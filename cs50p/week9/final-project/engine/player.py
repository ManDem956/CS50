from dataclasses import dataclass
import random
from typing import List

from engine.abstracts import CanMove, Moves


@dataclass
class RandomPlayer(CanMove):
    token: str = "x"

    def calculate_move(self, moves: Moves[int]) -> List[int]:
        result = []
        result = result + [
            random.choice(moves),
        ]
        return result

    def __str__(self) -> str:
        return self.token
    
    def __hash__(self) -> int:
        return hash(self.token)
