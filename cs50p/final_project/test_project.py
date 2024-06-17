import pytest
from game.impl.Board import Cell


@pytest.mark.parametrize(
    "input,expected",
    [
        (None, True),
        ("x", False),
        ("o", False),
    ],
)
def test_cell_empty(input: bool, expected: bool) -> None:
    cell = Cell()
    if input is not None:
        cell.value = input
    assert cell.is_empty() == expected
