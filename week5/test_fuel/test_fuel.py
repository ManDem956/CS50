import pytest
from plates import is_valid


@pytest.mark.parametrize("input,expected",
                         [("CS50", True),
                          ("CS05", False),
                          ("ECTO88", True),
                          ("50", False),
                          ("CS50P2", False),
                          ("PI3.14", False),
                          ("H", False),
                          ("OUTATIME", False),
                          ("NRVOUS", True)])
def test_is_valid(input, expected):
    assert is_valid(input) == expected
