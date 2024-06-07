from einstein import energy
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, 90000000000000000),
        (14, 1260000000000000000),
        (50, 4500000000000000000),
    ],
)
def test_energy(input, expected):
    assert energy(input) == expected
