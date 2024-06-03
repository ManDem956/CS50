import pytest
from twttr import shorten


def test_capital_case():
    assert shorten('Twitter') == 'Twttr'

