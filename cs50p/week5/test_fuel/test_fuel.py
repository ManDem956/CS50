import pytest
from fuel import convert, gauge


@pytest.mark.parametrize(
    "input, expected",
    [
        ("3/4", 75),
    ],
)
def test_convert(input, expected):
    assert convert(input) == expected


@pytest.mark.parametrize(
    "input, expectation",
    [
        ("10/3", pytest.raises(ValueError)),
        ("0/0", pytest.raises(ZeroDivisionError)),
        ("-1/100", pytest.raises(ValueError))

    ],
)
def test_convert_error(input, expectation):
    with expectation:
        assert convert(input)


@pytest.mark.parametrize(
    "input,expected",
    [
        (75, "75%"), (33, "33%"), (67, "67%"), (0, "E"), (1, "E"), (100, "F"), (99, "F"), (101, "F"), (-1, "E"),
    ],
)
def test_gauge(input, expected):
    assert gauge(input) == expected


# if __name__ == "__main__":
#     pytest.main(["."])
