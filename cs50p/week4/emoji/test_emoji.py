import pytest
from emojize import get_emoji


@pytest.mark.parametrize(
    "input,expected",
    [
        ((":1st_place_medal:"), "🥇"),
        ((":money_bag:"), "💰"),
        ((":smile_cat:"), "😸"),
        (("hello, :earth_asia:"), "hello, 🌏"),
        ((":candy: or :ice_cream:?"), "🍬 or 🍨?"),
    ],
)
def test_get_emoji(input, expected):
    assert get_emoji(input) == expected