import pytest
from fuel import convert, gauge


@pytest.mark.parametrize("input,expected",
                         [("3/4", 75"),
                          ("1/3", 33),
                          ("2/3", 67),
                          ("0/100", 0),
                          ("1/100", 1),
                          ("100/100", 100),
                          ("99/100", 99),
                          ("OUTATIME", False),
                          ("NRVOUS", True)])
def test_convert(input, expected):
    assert convert(input) == expected
