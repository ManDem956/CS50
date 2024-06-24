import pytest
from pytest_mock import mocker

from engine.abstracts import Movable


@pytest.fixture
def player_x():
    return mocker.Mock(spec=Movable, token="x")


@pytest.fixture
def player_o():
    return mocker.Mock(spec=Movable, token="o")
