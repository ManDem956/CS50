from game.abstract import Playable
from game.impl.Players import ABCPlayer


class Game:
    __player_x: ABCPlayer
    __player_y: ABCPlayer
    __board: Playable
