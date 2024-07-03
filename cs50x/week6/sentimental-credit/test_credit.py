import pytest
from credit import detect_carrier


@pytest.mark.parametrize(
    "input, expected",
    [
        ("378282246310005", "AMEX"),
        ("371449635398431", "AMEX"),
        ("5555555555554444", "MASTERCARD"),
        ("5105105105105100", "MASTERCARD"),
        ("4111111111111111", "VISA"),
        ("4012888888881881", "VISA"),
        ("1234567890", "INVALID"),
        ("4222222222223", "INVALID"),
        ("369421438430814", "INVALID"),
        ("4062901840", "INVALID"),
        ("5673598276138003", "INVALID"),
    ],
)
def test_detect_carrier(input, expected):
    assert detect_carrier(input) == expected
