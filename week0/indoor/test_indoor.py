from indoor import lower_voice
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("HELLO", "hello"),
        ("THIS IS CS50", "this is cs50"),
        ("50", "50"),
    ],
)
def test_indoor(input, expected):
    assert lower_voice(input) == expected
