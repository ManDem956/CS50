import pytest
from response import validate


@pytest.mark.parametrize(
    "input, expected",
    [
        ("malan@harvard.edu", "Valid"),
        ("kguryanov@gmail.com", "Valid"),
        ("kguryanov@gmail", "Invalid"),
        ("kguryanov", "Invalid"),
        ("1", "Invalid"),
        ("malan@@@harvard.ed", "Invalid"),
        ("kguryanov@gmail..com", "Invalid"),
        ("malan@@@harvard.ed.", "Invalid"),
    ],
)
def test_validate(input, expected):
    assert validate(input) == expected
