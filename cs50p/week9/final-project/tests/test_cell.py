import pytest

from engine.cell import Cell


class TestCell:

    @pytest.fixture
    def generic_cell(self):
        return Cell()

    @pytest.mark.parametrize(
        "input,expected",
        [(None, True), ("x", False), ("o", False)],
    )
    def test_cell(self, generic_cell, input: bool, expected: bool):
        generic_cell.value = input
        assert generic_cell.is_empty() == expected
