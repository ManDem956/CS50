import pytest
from plates import is_valid


class Test_Function:
    @pytest.mark.parametrize(
        "input,expected",
        [
            ("CS50", True),
            ("CS05", False),
            ("ECTO88", True),
            ("50", False),
            ("CS50P2", False),
            # ("PI3.14", False),
            ("aAa99@", False),
            # ("BGH22!", False),
            # ("H", False),
            ("OUTATIME", False),
            # ("NRVOUS", True),
        ],
    )
    def test_is_valid(self, input, expected):
        assert is_valid(input) == expected
