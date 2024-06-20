from itertools import permutations
from typing import Iterable, List, Set, Tuple

import numpy as np
from game.abstract import Playable
from game.impl.Board import Board
from game.impl.Players import ABCPlayer


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
            calculate_win_conditions (Callable): A callable that calculates the win conditions for
            the game.
            players (Iterable[ABCPlayer]): An iterable of players participating in the game.
            board_size (int, optional): The size of the game board. Defaults to MIN_BOARD_SIZE.
            board_dimensions (int, optional): The number of dimensions of the game board.
            Defaults to the first element of BOARD_DIMENSIONS.
            inception_level (int, optional): The inception level of the game.
            Defaults to MIN_INCEPTION_LEVEL.

        Returns:
            None

        Raises:
            ValueError: If the number of players is greater than MAX_PLAYERS, if the board size
            is less than MIN_BOARD_SIZE, if the board dimensions are not in BOARD_DIMENSIONS,
            or if the inception level is less than MIN_INCEPTION_LEVEL.

        Initializes the game with the specified players, board size, board dimensions,
        inception level, and win conditions.
        """

        self._validate_player_count(len(players))
        self._validate_board_size(board_size)
        self._validate_board_dimensions(board_dimensions)
        self._validate_inception_level(inception_level)

        self._players: ABCPlayer = players
        self._board_size: int = board_size
        self._board_dimensions: int = board_dimensions
        self._inception_level: int = inception_level
        self._win_conditions: Set[Tuple[int]] = self._calculate_win_conditions()
        self._board: Playable = Board(
            self._board_size**self._board_dimensions, self._inception_level
        )

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

    def _calculate_win_conditions(self) -> Set[Tuple[int, ...]]:
        """
        Calculates the win conditions for a game board of given size and dimensions.

        Returns:
            Set[Tuple[int, ...]]: A set of tuples representing the win conditions.
        """

        def generate_diagonals(board: np.ndarray) -> List[List[int]]:
            result = []
            axes = list(permutations(range(self._board_dimensions), 2))
            while axes:
                reshape = self._board_size ** (self._board_dimensions - 2)
                diagonals = np.diagonal(board).reshape(reshape, self._board_size)
                result.extend(diagonals.tolist())
                if diagonals.shape[0] == self._board_size:
                    result.append(np.diagonal(diagonals).tolist())
                board = np.rot90(board, axes=axes.pop())
            return result

        array = np.arange(self._board_size**self._board_dimensions).reshape(
            self._board_size, *([self._board_size] * (self._board_dimensions - 1))
        )
        axes = list(permutations(range(self._board_dimensions), 2))
        win_conditions = []
        while axes:
            reshape = self._board_size ** (self._board_dimensions - 1)
            win_conditions.extend(array.reshape(reshape, self._board_size).tolist())
            diagonals = generate_diagonals(array)
            win_conditions.extend(diagonals)
            array = np.rot90(array, axes=axes.pop())
        return {tuple(sorted(row)) for row in win_conditions}
