import pytest
from pytest_mock import mocker

from engine.player import ABCPlayer


@pytest.fixture
def player_x():
    return mocker.Mock(spec=ABCPlayer, token="x")


@pytest.fixture
def player_o():
    return mocker.Mock(spec=ABCPlayer, token="o")
