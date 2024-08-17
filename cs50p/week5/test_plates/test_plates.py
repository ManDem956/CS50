import pytest
from plates import is_valid


class Test_Function:
    @pytest.mark.parametrize(
        "input,expected",
        [
            ("CS50", True),
            ("NRVOUS", True),
            ("ECTO88", True),
            ("A", False),
            ("50", False),
            ("5A", False),
            ("A5", False),
            ("12CS50", False),
            ("CS05", False),
            ("CS50P2", False),
            ("aAa99@", False),
            ("aA599@", False),
            ("aA-bbb", False),
            ("OUTATIME", False),
        ],
    )
    def test_is_valid(self, input, expected):
        assert is_valid(input) == expected
