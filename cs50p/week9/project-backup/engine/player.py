import random
from typing import List

from engine.abstracts import Movable, Moves, Winnable


class RandomPlayer(Movable):
    def choose_move(self, moves: Moves) -> List[int]:
        move = random.randrange(len(moves))
        if isinstance(moves[move], Winnable):
            return self.choose_move(moves[move]) + [move]
        else:
            return [move]
        # return result
