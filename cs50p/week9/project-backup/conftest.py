import contextlib
import itertools
from types import NoneType
import pytest
from contextlib import nullcontext as does_not_raise
from engine.abstracts import Movable
from engine import Board
from engine import RandomPlayer

__all__ = ["player_x", "player_o", "players"]


@pytest.fixture
def board(request):
    size = request.param["size"]
    dimensions = request.param["dimensions"]
    inception = request.param["inception"]
    return Board(size, dimensions, inception)


@pytest.fixture(scope="module")
def player_x(module_mocker):
    return module_mocker.Mock(spec=Movable, token="x")


@pytest.fixture(scope="module")
def player_o(module_mocker):
    return module_mocker.Mock(spec=Movable, token="o")


@pytest.fixture(scope="module")
def players(player_x, player_o):
    return itertools.cycle((player_x, player_o))


@pytest.fixture
def random_player_x():
    return RandomPlayer()


@pytest.fixture
def random_player_o():
    return RandomPlayer()


@pytest.fixture
def random_players(random_player_x, random_player_o):
    return itertools.cycle((random_player_x, random_player_o))


def pytest_make_parametrize_id(config: pytest.Config, val: object, argname: str) -> str | None:
    if isinstance(val, (dict,)):
        # note this wouldn't show any hours/minutes/seconds
        return "-".join(f"{key}:{value}" for key, value in val.items())
    elif isinstance(val, (tuple,)):
        return str(len(val))
    elif isinstance(val, (does_not_raise,)):
        return "does_not_raise"
    elif isinstance(val, (NoneType,)):
        return "nothing"
    elif isinstance(val, (contextlib.AbstractContextManager,)):
        return "raises"
    elif isinstance(val, (bool,)):
        return str(val)
    elif isinstance(val, (str,)):
        return val
    else:
        # return None
        return f"[{type(val)}]"
