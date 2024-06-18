from itertools import permutations
from typing import Iterable, List, Set, Tuple
from game.abstract import Playable
from game.impl.Board import Board
from game.impl.Players import ABCPlayer

import numpy as np


class Game:
    MAX_PLAYERS = 2
    MIN_BOARD_SIZE = 3
    BOARD_DIMENSIONS = (2, 3)
    MIN_INCEPTION_LEVEL = 0

    def __init__(
        self,
        players: Iterable[ABCPlayer],
        board_size: int = MIN_BOARD_SIZE,
        board_dimensions: int = BOARD_DIMENSIONS[0],
        inception_level: int = MIN_INCEPTION_LEVEL,
    ) -> None:
        """
        Initializes a new instance of the Game class.

        Args:
            players (Iterable[ABCPlayer]): An iterable of ABCPlayer objects
                                            representing the players.
            board_size (int, optional): The size of the game board.
                                            Defaults to MIN_BOARD_SIZE.
            board_dimensions (int, optional): The dimensions of the game board.
                                                Defaults to MIN_BOARD_DIMENSIONS.
            inception_level (int, optional): The inception level of the game.
                                                Defaults to MIN_INCEPTION_LEVEL.

        Returns:
            None

        Raises:
            ValueError: If the number of players exceeds the maximum allowed.
            ValueError: If the board size is less than the minimum allowed.
            ValueError: If the board dimensions are less than the minimum allowed.
            ValueError: If the inception level is less than the minimum allowed.
        """
        self._validate_player_count(len(players))
        self._validate_board_size(board_size)
        self._validate_board_dimensions(board_dimensions)
        self._validate_inception_level(inception_level)

        self._players = players
        self._board_size = board_size
        self._board_dimensions = board_dimensions
        self._inception_level = inception_level
        self._win_conditions = self._calculate_win_conditions()
        self._board = Board(self._board_size**self._board_dimensions, self._inception_level)

    def _validate_player_count(self, player_count):
        if player_count > self.MAX_PLAYERS:
            raise ValueError(f"Maximum number of players is {self.MAX_PLAYERS}")

    def _validate_board_size(self, size):
        if size < self.MIN_BOARD_SIZE:
            raise ValueError(f"Minimum board size is {self.MIN_BOARD_SIZE}")

    def _validate_board_dimensions(self, dimensions):
        if dimensions not in self.BOARD_DIMENSIONS:
            raise ValueError(f"ALlowed board dimensions are {self.BOARD_DIMENSIONS}")

    def _validate_inception_level(self, level):
        if level < self.MIN_INCEPTION_LEVEL:
            raise ValueError(f"Minimum inception level is {self.MIN_INCEPTION_LEVEL}")

    @property
    def board(self) -> Playable:
        return self._board

    @property
    def players(self) -> Iterable[ABCPlayer]:
        return self._players

    def _calculate_diagonals(self, board: np.ndarray) -> List[List[int]]:
        result = []
        permutations_ = list(permutations(range(self._board_dimensions), 2))
        while permutations_:
            reshape = self._board_size ** (self._board_dimensions - 2)
            diagonals = np.diagonal(board).reshape(reshape, self._board_size)
            result.extend(diagonals.tolist())
            if diagonals.shape[0] == self._board_size:
                result.append(np.diagonal(diagonals).tolist())
            board = np.rot90(board, axes=permutations_.pop())

        return result

    def _calculate_win_conditions(self) -> Set[Tuple[int]]:
        """
        Calculates all possible win conditions for the game board.

        Returns:
            A set of tuples representing all possible win conditions.
        """
        # Generate all possible win conditions
        result = []
        array = np.arange(self._board_size**self._board_dimensions).reshape(
            self._board_size, *([self._board_size] * (self._board_dimensions - 1))
        )
        permutations_ = list(permutations(range(self._board_dimensions), 2))
        while permutations_:
            # add all rows in current array
            reshape = self._board_size ** (self._board_dimensions - 1)
            tmp = array.reshape(reshape, self._board_size)
            result.extend(tmp.tolist())
            # Generate all possible diagonals
            diagonals = self._calculate_diagonals(array)
            result.extend(diagonals)
            # Rotate the array
            array = np.rot90(array, axes=permutations_.pop())
        # Flatten and sort the result
        return {tuple(sorted(item)) for item in result}
