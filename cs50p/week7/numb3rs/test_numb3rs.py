import pytest
from numb3rs import validate


@pytest.mark.parametrize(
    "input, expected",
    [
        ("255.255.255.255", True),
        ("0.0.0.0", True),
        ("127.0.0.1", True),
        ("127.00.00.01", True),
        ("255.255.255.255.", False),
        (".255.255.255.255", False),
        ("255.255.255.255.10", False),
        ("255.256.257.258", False),
        ("1.2.3.1000", False),
        ("01.02.03.025", True),
        ("1.2.1000.1", False),
        ("1.1000,200,173", False),
        ("1000.2.3.1", False),
        ("cat", False),
        ("256", False),
        # ("255", False),
        # ("255.", False),
        # ("255.", False),
    ],
)
def test_validate(input, expected):
    assert validate(input) == expected
