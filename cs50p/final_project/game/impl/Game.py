from typing import Iterable
from game.abstract import Playable
from game.impl.Board import Board
from game.impl.Players import ABCPlayer


class Game:
    MAX_PLAYERS: int = 2
    __players: Iterable[ABCPlayer]
    __board: Playable

    def __init__(self, players: Iterable[ABCPlayer], board: Playable) -> None:
        """
        Initializes a new instance of the Game class.

        Args:
            players (Iterable[ABCPlayer]): An iterable of players participating in the game.
            board (Playable): The game board.

        Raises:
            ValueError: If the number of players exceeds the maximum allowed number of players.

        Returns:
            None
        """
        if len(players) > self.MAX_PLAYERS:
            raise ValueError(f"Maximum number of players is {self.MAX_PLAYERS}")
        self.__players: Iterable[ABCPlayer] = players
        self.__board: Playable = Board

    @property
    def board(self) -> Playable:
        """Returns the game board"""
        return self.__board

    @property
    def players(self) -> Iterable[ABCPlayer]:
        """
        Returns the players in the game.

        :return: Iterable of players in the game.
        :rtype: Iterable[ABCPlayer]
        """
        return self.__players
