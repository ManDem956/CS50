from tip import calculate
import pytest


@pytest.mark.parametrize(
    "price, tip, expected",
    [
        ("$50.00", "15%", "$7.50"),
        ("$100.00", "18%", "$18.00"),
        ("$15.00", "25%", "$3.75"),
    ],
)
def test_calculate(price, tip, expected):
    assert calculate(price, tip) == expected
