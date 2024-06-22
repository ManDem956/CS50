import random
from typing import Iterable
from engine.player import ABCPlayer


class RandomPLayer(ABCPlayer):

    def choose_move(self, moves: Iterable[int]) -> int:
        return random.choice(moves)
