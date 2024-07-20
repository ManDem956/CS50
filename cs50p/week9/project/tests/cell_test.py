import pytest

from game.board import Cell


@pytest.mark.parametrize("input, expected", [(None, None), ("1", "1")])
def test_simple(input, expected):
    cell = Cell(input)
    assert cell.value == expected
