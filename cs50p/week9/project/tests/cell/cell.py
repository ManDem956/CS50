import pytest

from engine import Cell


@pytest.fixture
def generic_cell():
    return Cell()
