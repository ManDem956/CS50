from typing import Set, Tuple

import numpy as np
import pytest

from project import generate_diagonals, generate_win_combinations, reshape_to_2d


class TestHelpers:
    @staticmethod
    def get_set_from_list(array) -> Set[Tuple[int]]:
        return set(sorted(tuple(sorted(row)) for row in array))

    @pytest.fixture
    def array_nxm(self, request):
        size = request.param["size"]
        dimension = request.param["dimension"]
        array = np.arange(size**dimension).reshape(size, *([size] * (dimension - 1)))
        return array

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
    def test_reshape_to_2d(self, input, size, expected):
        assert reshape_to_2d(input, size).tolist() == expected

    # fmt: off
    @pytest.mark.parametrize(
        "array_nxm, size, expected",
        [
            (
                {"size": 3, "dimension": 2},
                3,
                [[0, 4, 8]],
            ),
            (
                {"size": 3, "dimension": 3},
                3,
                [
                    (0, 4, 8), (0, 10, 20), (0, 12, 24), (0, 13, 26), (1, 13, 25), (2, 14, 26), (3, 13, 23), (6, 16, 26), (9, 13, 17), (18, 22, 26),  # noqa
                ],
            ),
            (
                {"size": 4, "dimension": 3},
                4,
                [
                    (0, 5, 10, 15), (0, 17, 34, 51), (0, 20, 40, 60), (0, 21, 42, 63), (1, 21, 41, 61), (2, 22, 42, 62), (3, 23, 43, 63), (4, 21, 38, 55), (8, 25, 42, 59), (12, 29, 46, 63), (16, 21, 26, 31), (32, 37, 42, 47), (48, 53, 58, 63), # noqa
                ],
            ),
        ],
        indirect=["array_nxm"],
    )
    # fmt: on
    def test_generate_diagonals(self, array_nxm, size, expected):
        actual = self.get_set_from_list(generate_diagonals(array_nxm, size).tolist())
        expected = self.get_set_from_list(expected)
        assert actual == expected

    # (5^n - 3^n)/2.
    @pytest.mark.parametrize(
        "size, dimensions, expected",
        [
            (3, 2, 8),
            (3, 3, 49),
            (4, 3, 76),
        ],
    )
    def test_generate_win_combinations_counts(self, size: int, dimensions: int, expected: int):
        actual = len(generate_win_combinations(size, dimensions))
        assert actual == expected
