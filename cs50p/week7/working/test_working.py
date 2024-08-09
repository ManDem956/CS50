import pytest
from working import convert
# from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "input, expected",
    [
        ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
        ("9 AM to 5 PM", "09:00 to 17:00"),
        ("10 PM to 8 AM", "22:00 to 08:00"),
        ("10:00 PM to 8:00 AM", "22:00 to 08:00"),
    ],
)
def test_convert(input, expected):
    assert convert(input) == expected


@pytest.mark.parametrize(
    "input",
    [
        ("9:60 AM to 5:59 PM"),
        ("9:59 AM to 5:60 PM"),
        ("9:59 AM to 5:600 PM"),
        ("9 AM - 5 PM"),
        # ("9 AM 5 PM"),
        ("cat"),
    ],
)
def test_convert_errors(input):
    with pytest.raises(ValueError):
        convert(input)
