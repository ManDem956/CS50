from jar import Jar
from contextlib import nullcontext as does_not_raise
import pytest


@pytest.fixture
def default_jar() -> Jar:
    return Jar()


@pytest.fixture
def default_jar_full() -> Jar:
    jar = Jar()
    jar.deposit(12)
    return jar


@pytest.mark.parametrize(
    "capacity, expected, exception",
    [
        (10, 10, does_not_raise()),
        (1, 1, does_not_raise()),
        (100, 100, does_not_raise()),
        (None, 12, does_not_raise()),
        (-10, None, pytest.raises(ValueError)),
    ],
)
def test_init(capacity, expected, exception):
    with exception:
        jar = Jar(capacity) if capacity is not None else Jar()
        assert jar.capacity == expected
        assert jar.size == 0


@pytest.mark.parametrize(
    "deposit, expected, exception",
    [
        (10, "🍪" * 10, does_not_raise()),
        (1, "🍪" * 1, does_not_raise()),
        (12, "🍪" * 12, does_not_raise()),
        (0, "🍪" * 0, does_not_raise()),
    ],
)
def test_str_default_jar(default_jar: Jar, deposit, expected, exception):
    with exception:
        default_jar.deposit(deposit)
        assert str(default_jar) == expected


@pytest.mark.parametrize(
    "deposit, expected, exception",
    [
        (10, 10, does_not_raise()),
        (1, 1, does_not_raise()),
        (12, 12, does_not_raise()),
        (0, 0, does_not_raise()),
        (-10, None, pytest.raises(ValueError)),
        (13, None, pytest.raises(ValueError)),
    ],
)
def test_deposit(default_jar: Jar, deposit, expected, exception):
    with exception:
        default_jar.deposit(deposit)
        assert default_jar.size == expected


@pytest.mark.parametrize(
    "withdraw, expected, exception",
    [
        (10, 2, does_not_raise()),
        (1, 11, does_not_raise()),
        (12, 0, does_not_raise()),
        (0, 12, does_not_raise()),
        (-10, None, pytest.raises(ValueError)),
        (13, None, pytest.raises(ValueError)),
    ],
)
def test_withdraw(default_jar_full: Jar, withdraw, expected, exception):
    with exception:
        default_jar_full.withdraw(withdraw)
        assert default_jar_full.size == expected


def test_dummy():
    pass


def test_dummy1():
    pass


def test_dummy2():
    pass
