import contextlib
from types import NoneType
from typing import Sized
import pytest

from contextlib import nullcontext as does_not_raise

from engine.player import RandomPlayer

MAX_VALUE_LENGTH = 70


def shorten(value, max_len=MAX_VALUE_LENGTH) -> str:
    result = str(value)
    if len(result) > max_len:
        result = f"{result[:MAX_VALUE_LENGTH//4]}...{result[-MAX_VALUE_LENGTH//4:]}"
    return result


def shorten_dict(value, max_len=MAX_VALUE_LENGTH) -> str:
    result = str(value)
    if len(result) > max_len:
        return f"{result[:MAX_VALUE_LENGTH//4]}...{result[-MAX_VALUE_LENGTH//4:]}"
    return "-".join(f"{key}:{shorten(val)}" for key, val in value.items())


def pytest_make_parametrize_id(config: pytest.Config, val: object, argname: str) -> str | None:
    if isinstance(val, (int, float, bool)):
        return f"{argname}:{val}"
    elif isinstance(val, (tuple, list, set)):
        return f"{argname}:{shorten(val)}"
    elif isinstance(val, (dict,)):
        return f"{argname}:{shorten_dict(val)}"
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
    return RandomPlayer("x")


@pytest.fixture
def random_player_y():
    return RandomPlayer("o")


@pytest.fixture
def random_players(random_player_x, random_player_y):
    return (random_player_x, random_player_y)
