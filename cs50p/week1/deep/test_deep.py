from deep import check_answer, CONST_ANSWERS
import pytest


@pytest.mark.parametrize("input,expected",
                         [
                             ("42", "Yes"),
                             ("forty two", "Yes"),
                             ("forty-two", "Yes"),
                             ("50", "No"),
                             ("I am groot", "No"),
                         ])
def test_check_answer(input, expected):
    assert check_answer(input, CONST_ANSWERS) == expected
