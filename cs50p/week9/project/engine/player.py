from abc import ABC, abstractmethod
from dataclasses import dataclass
import random
from typing import Hashable, Iterable


@dataclass
class ABCPlayer(ABC):
    name: str
    token: Hashable

    @abstractmethod
    def choose_move(self, moves: Iterable[int]) -> int:
        raise NotImplementedError()


class RandomPLayer(ABCPlayer):

    def choose_move(self, moves: Iterable[int]) -> int:
        return random.choice(moves)
