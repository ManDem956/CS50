from jar import Jar
# from contextlib import nullcontext as does_not_raise
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
    "capacity, expected",
    [
        (10, 10),
        (1, 1),
        (100, 100),
        (1400, 1400),
        (None, 12),
    ],
)
def test_init(capacity, expected):
    jar = Jar(capacity) if capacity is not None else Jar()
    assert jar.capacity == expected
    assert jar.size == 0


@pytest.mark.parametrize(
    "capacity",
    [
        (-10),
    ],
)
def test_init_error(capacity):
    with pytest.raises(ValueError):
        Jar(capacity)


@pytest.mark.parametrize(
    "deposit, expected",
    [
        (10, "🍪" * 10),
        (11, "🍪" * 11),
        (12, "🍪" * 12),
        (1, "🍪" * 1),
        (12, "🍪" * 12),
        (0, "🍪" * 0),
    ],
)
def test_str_default_jar_str(default_jar: Jar, deposit, expected):
    default_jar.deposit(deposit)
    assert str(default_jar) == expected


@pytest.mark.parametrize(
    "deposit, expected",
    [
        (10, 10),
        (1, 1),
        (12, 12),
        (0, 0),
    ],
)
def test_deposit_size(default_jar: Jar, deposit, expected):
    default_jar.deposit(deposit)
    assert default_jar.size == expected


@pytest.mark.parametrize(
    "deposit, exception",
    [
        (-10, pytest.raises(ValueError)),
        (13, pytest.raises(ValueError)),
    ],
)
def test_deposit_size_error(default_jar: Jar, deposit, exception):
    with exception:
        default_jar.deposit(deposit)


@pytest.mark.parametrize(
    "withdraw, expected",
    [
        (10, 2),
        (1, 11),
        (12, 0),
        (0, 12),
    ],
)
def test_withdraw(default_jar_full: Jar, withdraw, expected):
    default_jar_full.withdraw(withdraw)
    assert default_jar_full.size == expected


@pytest.mark.parametrize(
    "withdraw",
    [
        (-10),
        (13),
    ],
)
def test_withdraw_error(default_jar_full: Jar, withdraw):
    with pytest.raises(ValueError):
        default_jar_full.withdraw(withdraw)
