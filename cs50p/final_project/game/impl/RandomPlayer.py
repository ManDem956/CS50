import random
from typing import Tuple


class RandomPlayer:

    def get_move(self, available_moves: Tuple[int]) -> int:
        return random.choice(available_moves)
