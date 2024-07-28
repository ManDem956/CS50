from interpreter import interpret
import pytest


@pytest.mark.parametrize("input, expected",
                         [
                             ("1+1", 2.0),
                             ("2 -3", -1.0),
                             ("2* 2", 4.0),
                             ("50 / 5", 10.0),
                         ])
def test_interpret(input, expected):
    assert interpret(input) == expected


@pytest.mark.parametrize("input",
                         [
                             ("1^1"),
                             ("1**4"),
                         ])
def test_interpret_fail(input):
    with pytest.raises(ValueError):
        interpret(input)


@pytest.mark.parametrize("input",
                         [
                             ("1/0"),
                         ])
def test_interpret_fail_zero_div(input):
    with pytest.raises(ZeroDivisionError):
        interpret(input)
