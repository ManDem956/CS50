import pytest
from twttr import shorten


@pytest.mark.parametrize("input,expected",
                         [("Twitter", "Twttr"),
                          ("What's your name?", "Wht's yr nm?"),
                          ("CS50", "CS50"),
                          ("I am Groot", " m Grt")])
def test_capital_case(input, expected):
    assert shorten(input) == expected
