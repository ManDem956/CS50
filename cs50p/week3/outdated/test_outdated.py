import pytest
from outdated import get_date_value


@pytest.mark.parametrize(
    "input,expected",
    [
        ("9/8/1636", ("1636", "09", "08")),
        ("September 8, 1636", ("1636", "09", "08")),
    ],
)
def test_get_date_value(input, expected):
    assert get_date_value(input) == expected
