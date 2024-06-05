import pytest
from response import validate
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "input, expected, exception",
    [
        ("malan@harvard.edu", "malan@harvard.edu", does_not_raise()),
        ("kguryanov@gmail.com", "kguryanov@gmail.com", does_not_raise()),
        ("kguryanov@gmail", None, pytest.raises(ValueError)),
        ("kguryanov", None, pytest.raises(ValueError)),
        ("1", None, pytest.raises(ValueError)),
        ("malan@@@harvard.ed", None, pytest.raises(ValueError)),
        ("kguryanov@gmail..com", None, pytest.raises(ValueError)),
        ("malan@@@harvard.ed.", None, pytest.raises(ValueError)),
    ],
)
def test_validate(input, expected, exception):
    with exception:
        assert validate(input) == expected
