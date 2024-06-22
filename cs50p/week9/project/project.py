from itertools import permutations
from typing import List, Tuple
import numpy as np

MAX_DIMENSIONS = 3


def reshape_to_2d(arr: np.ndarray, size: int) -> np.ndarray:
    """Reshapes a numpy array to a 2D array of specified size."""
    if np.prod(arr.shape) % size != 0:
        raise ValueError("Array dimensions must divide into size.")
    return arr.reshape(-1, size)


def generate_diagonals(array: np.ndarray, size: int) -> List[List[int]]:
    """Generate diagonals of a numpy array."""
    result: List[List[int]] = []
    axes: List[Tuple[int, int]] = list(permutations(range(len(array.shape)), 2))
    while axes:
        diagonals = reshape_to_2d(np.diagonal(array), size)
        result.extend(diagonals.tolist())
        while len(diagonals) == len(array.shape):
            diagonals = reshape_to_2d(np.diagonal(diagonals), size)
            result.extend(diagonals.tolist())
        array = np.rot90(array, axes=axes.pop())

    return result


def generate_win_combinations(size: int, dimensions: int):
    """
    Generate all possible winning combinations for a game board.

    Args:
        size (int): The size of each dimension of the game board.
        dimensions (int): The number of dimensions of the game board.

    Raises:
        ValueError: If the number of dimensions is greater than the maximum supported.

    Returns:
        set: A set of tuples representing all possible winning combinations.
    """
    if dimensions > MAX_DIMENSIONS:
        raise ValueError(
            f"I am not smart enough YET to handle extradimensional.\
                         Maximum dimensions supported right no is {MAX_DIMENSIONS}"
        )

    array = np.arange(size**dimensions).reshape(size, *([size] * (dimensions - 1)))

    result = []
    axes = list(permutations(range(dimensions), 2))
    while axes:
        # result.extend(reshape_to_2d(array, size).tolist())
        diags = generate_diagonals(array, size)
        result.extend(diags)
        array = np.rot90(array, axes=axes.pop())

    print(f"{array=}")

    result = set(sorted((tuple(sorted(item)) for item in result)))
    return result


def main() -> None:
    board_size = 3
    board_dimensions = 3
    check_sum = ((board_size + 2) ** board_dimensions - board_size**board_dimensions) // 2

    result = generate_win_combinations(board_size, board_dimensions)
    print(sorted(result), sep="\n")
    print(f"{check_sum == len(result)}, {check_sum = }, {len(result) = }")


if __name__ == "__main__":
    main()
