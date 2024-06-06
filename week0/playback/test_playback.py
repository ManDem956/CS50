from playback import playback
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("This is CS50", "This...is...CS50"),
        ("This is our week on functions",
         "This...is...our...week...on...functions"),
        ("Let's implement a function called hello",
         "Let's...implement...a...function...called...hello"),
    ],
)
def test_playback(input, expected):
    assert playback(input) == expected
