from typing import Iterable

from engine.abstracts import Movable


class RandomPLayer(Movable):
    def choose_move(self, moves: Iterable[int]) -> int:
        raise NotImplementedError
