from dataclasses import dataclass
import random
from game.abstracts import Playable


@dataclass
class RandomPlayer(Playable):
    value: str

    def __hash__(self) -> int:
        return hash(self.value)

    def calculate_move(self, moves: tuple[int]) -> int:
        return random.choice(moves)
