import pytest
from lines import count, validate


@pytest.mark.parametrize(
        "input, expected",
        [
            ("test_data/six.py", 6),
        ]
)
def test_count(input, expected):
    assert count(input) == expected


@pytest.mark.parametrize(
        "input, expected, msg",
        [
            ("test_data/nil.py", pytest.raises(ValueError), "is empty"),
            ("test_data/test.txt", pytest.raises(ValueError), "not a python file"),
            ("test_data/nofile", pytest.raises(FileNotFoundError), "could not be found"),
        ]
)
def test_validate(input, expected, msg):
    with expected as e:
        validate(input)
        assert msg in e
