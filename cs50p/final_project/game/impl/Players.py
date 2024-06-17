import random
from typing import Tuple

from game.abstract.ABCPlayer import ABCPlayer


class RandomPlayer(ABCPlayer):

    def get_move(self, available_moves: Tuple[int]) -> int:
        return random.choice(available_moves)
