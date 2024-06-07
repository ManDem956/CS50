from faces import convert
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Hello :)", "Hello 🙂"),
        ("Goodbye :(", "Goodbye 🙁"),
        ("Hello :) Goodbye :(", "Hello 🙂 Goodbye 🙁"),
    ],
)
def test_faces(input, expected):
    assert convert(input) == expected
