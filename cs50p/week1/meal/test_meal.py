import pytest
from meal import convert, get_meal


@pytest.mark.parametrize("input, expected",
                         [
                             ("7:30", 7.5),
                         ])
def test_convert(input, expected):
    assert convert(input) == expected


@pytest.mark.parametrize("input",
                         ["7:60", "24:00",])
def test_convert_fail(input):
    with pytest.raises(ValueError):
        convert(input)


@pytest.mark.parametrize("input, expected",
                         [
                             (7.50, "breakfast"),
                             (7.00, "breakfast"),
                             (12+(42/60), "lunch"),
                             (18+(32/60), "dinner"),
                             (11+11/60, None),
                         ])
def test_get_meal(input, expected):
    assert get_meal(input) == expected
