import contextlib
from types import NoneType
from typing import Sized
import pytest

from contextlib import nullcontext as does_not_raise

from engine.player import RandomPlayer

MAX_VALUE_LENGTH = 16


def shorten(value) -> str:
    result = str(value)
    if len(result) > MAX_VALUE_LENGTH:
        result = f"{result[:MAX_VALUE_LENGTH]}..."
    return f"( {result} )"


def pytest_make_parametrize_id(config: pytest.Config, val: object, argname: str) -> str | None:
    if isinstance(val, (int, float, bool)):
        return f"{argname}:{shorten(val)}"
    if isinstance(val, (dict,)):
        return "-".join(f"{key}:{shorten(value)}" for key, value in val.items())
    elif isinstance(
        val,
        (
            tuple,
            list,
            set,
        ),
    ):
        return f"{argname}:{str(len(val))}"
    elif isinstance(val, (does_not_raise,)):
        return f"{argname}:does_not_raise"
    elif isinstance(val, (NoneType,)):
        return f"{argname}:nothing"
    elif isinstance(val, (contextlib.AbstractContextManager,)):
        return f"{argname}:raises"
    else:
        val_len = f":{len(val)}" if isinstance(val, (Sized,)) else ""
        return f"{argname}:{val.__class__.__name__}{val_len}"


@pytest.fixture
def random_player_x():
    return RandomPlayer('x')


@pytest.fixture
def random_player_y():
    return RandomPlayer('o')


@pytest.fixture
def random_players(random_player_x, random_player_y):
    return (random_player_x, random_player_y)
