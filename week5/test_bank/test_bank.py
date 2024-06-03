import pytest
from bank import value


@pytest.mark.parametrize("input,expected",
                         [("Hello", 0),
                          ("Hello, Newman", "Wht's yr nm?"),
                          ("CS50", "CS50"),
                          ("I am Groot", " m Grt"),
                          ("PYTHON", "PYTHN")])
def test_value(input, expected):
    assert value(input) == expected
