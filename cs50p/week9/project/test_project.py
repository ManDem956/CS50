import numpy as np
import pytest
from project import generate_diagonals, reshape_to_2d

from tests import generic_cell  # noqa


def get_set_from_list(array: np.ndarray) -> set:
    return set(sorted(tuple(sorted(row)) for row in array))


@pytest.fixture
def array_3x2d():
    size = 3
    dim = 2
    array = np.arange(size**dim).reshape(size, *([size] * (dim - 1)))
    return array


@pytest.fixture
def array_3x3d():
    size = 3
    dim = 3
    array = np.arange(size**dim).reshape(size, *([size] * (dim - 1)))
    return array


@pytest.mark.parametrize(
    "input,expected",
    [
        (None, True),
        ("x", False),
        ("o", False),
    ],
)
def test_cell(generic_cell, input: bool, expected: bool) -> None:  # noqa
    generic_cell.value = input
    assert generic_cell.is_empty() == expected


@pytest.mark.parametrize(
    "input, size, expected",
    [
        (
            np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]),
            3,
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]],
        ),
        (
            np.array([1, 2, 3, 4]),
            4,
            [[1, 2, 3, 4]],
        ),
    ],
)
def test_reshape_to_2d(input, size, expected):
    assert reshape_to_2d(input, size).tolist() == expected


@pytest.mark.parametrize(
    "input, size, expected",
    [
        (
            "array_3x2d",
            3,
            [[0, 4, 8], [2, 4, 6]],
        ),
        (
            "array_3x3d",
            3,
            [
                (0, 4, 8),
                (0, 10, 20),
                (0, 12, 24),
                (0, 13, 26),
                (1, 13, 25),
                (2, 4, 6),
                (2, 10, 18),
                (2, 13, 24),
                (2, 14, 26),
                (3, 13, 23),
                (5, 13, 21),
                (6, 12, 18),
                (6, 13, 20),
                (6, 16, 26),
                (7, 13, 19),
                (8, 13, 18),
                (8, 14, 20),
                (8, 16, 24),
                (9, 13, 17),
                (11, 13, 15),
                (18, 22, 26),
                (20, 22, 24),
            ],
        ),
    ],
)
def test_generate_diagonals(input, size, expected, request):
    actual = get_set_from_list(generate_diagonals(request.getfixturevalue(input), size))
    expected = get_set_from_list(expected)
    assert actual == expected
