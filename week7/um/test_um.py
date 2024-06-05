import pytest
from um import count


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Um, thanks, um...", 2),
        ("Um", 1),
        ("Um,ah,um", 2),
        ("Um,ah,UM", 2),
        ("myumka", 0),
    ],
)
def test_count(input, expected):
    assert count(input) == expected
