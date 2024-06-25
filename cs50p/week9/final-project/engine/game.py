from itertools import combinations, permutations
from typing import Set, Tuple
import numpy as np

MAX_DIMENSIONS = 3


class Game:
    @classmethod
    def reshape_to_2d(cls, arr: np.ndarray, size: int) -> np.ndarray:
        """Reshapes a numpy array to a 2D array of specified size."""
        if np.prod(arr.shape) % size != 0:
            raise ValueError("Array dimensions must divide into size.")
        return arr.reshape(-1, size)

    @classmethod
    def generate_diagonals(cls, array: np.ndarray, size: int) -> np.ndarray:
        """Generate diagonals of a numpy array."""

        if len(array.shape) < 2:
            return cls.reshape_to_2d(array, size)

        result = cls.reshape_to_2d(np.diagonal(array), size)
        axes = list(combinations(range(len(array.shape)), 2))
        while axes:
            diagonals = np.diagonal(array, 0, *axes.pop())
            result = np.concatenate([result, cls.reshape_to_2d(diagonals, size)])
            result = np.concatenate([result, cls.generate_diagonals(diagonals, size)])

        return result

    @classmethod
    def generate_win_combinations(cls, size: int, dimensions: int) -> Set[Tuple[int]]:
        """
        Generates combinations of integers for a given size and dimensions.

        Parameters:
            size (int): The size of the combinations.
            dimensions (int): The number of dimensions for the combinations.

        Returns:
            Set[Tuple[int]]: A set of tuples representing the combinations.
        """
        if dimensions > MAX_DIMENSIONS:
            raise ValueError(
                f"I am not smart enough YET to handle extradimensional.\
                            Maximum dimensions supported right no is {MAX_DIMENSIONS}"
            )

        array = np.arange(size**dimensions).reshape(size, *([size] * (dimensions - 1)))

        # result = generate_diagonals(array, size).tolist()

        result = cls.reshape_to_2d(array, size).tolist()
        axes = list(permutations(range(dimensions), 2))
        while axes:
            array = np.rot90(array, axes=axes.pop())
            result.extend(cls.reshape_to_2d(array, size).tolist())
            diags = cls.generate_diagonals(array, size)
            result.extend(diags.tolist())

        result = set(sorted((tuple(sorted(item)) for item in result)))
        return result
