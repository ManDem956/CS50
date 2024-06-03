import pytest
from plates import is_valid


@pytest.mark.parametrize("input,expected",
                         [("Hello", 0),
                          ("Hello, Newman", 0),
                          ("How you doing?", 20),
                          ("What's happening?", 100)])
def test_value(input, expected):
    assert value(input) == expected
