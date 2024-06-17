from itertools import permutations
from typing import Iterable, Set, Tuple
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

    def _get_diagonals(self, array: np.ndarray) -> Tuple[Tuple[int]]:
        if len(array.shape) < 3:
            return [np.diagonal(array).tolist()]
        result = []

        perms = list(permutations(range(self._board_dimensions), 2))
        while len(perms) > 0:
            diags = np.diagonal(array)
            result.extend(diags.tolist())
            result.append(np.diagonal(diags).tolist())
            axes = perms.pop()
            array = np.rot90(array, axes=axes)

        return result

    def _calculate_win_conditions(self) -> Set[Tuple[int]]:
        res = tuple(
            zip(*[iter(range(self._board_size**self._board_dimensions))] * self._board_size)
        )
        for _ in range(2, self._board_dimensions):
            res = tuple(zip(*[iter(res)] * self._board_size))

        array = np.array(res)
        result = list()
        perms = list(permutations(range(self._board_dimensions), 2))
        while len(perms) > 0:
            result.extend(self._get_diagonals(array))
            if len(array.shape) >= self._board_dimensions:
                array.reshape(-1, array.shape[-1])
            result.extend(array.reshape(-1, array.shape[-1]).tolist())
            axes = perms.pop()
            array = np.rot90(array, axes=axes)

        return set(tuple(sorted(item)) for item in result)
