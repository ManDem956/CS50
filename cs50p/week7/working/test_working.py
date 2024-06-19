import pytest
from working import convert
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "input, expected, exception",
    [
        ("9:00 AM to 5:00 PM", "09:00 to 17:00", does_not_raise()),
        ("9 AM to 5 PM", "09:00 to 17:00", does_not_raise()),
        ("10 PM to 8 AM", "22:00 to 08:00", does_not_raise()),
        ("10:00 PM to 8:00 AM", "22:00 to 08:00", does_not_raise()),
        ("9:60 AM to 5:59 PM", None, pytest.raises(ValueError)),
        ("9 AM - 5 PM", None, pytest.raises(ValueError)),
        ("09:00 AM - 17:00 PM", None, pytest.raises(ValueError)),
        ("cat", None, pytest.raises(ValueError)),
    ],
)
def test_convert(input, expected, exception):
    with exception:
        assert convert(input) == expected
