from twttr import shorten


def test_twttr_lowercase():
    assert shorten('twitter') == 'twttr'
    assert shorten('eagle') == 'gl'


def test_twttr_uppercase():
    assert shorten('LUFFY') == 'LFFY'
    assert shorten('HELLO') == 'HLL'


def test_twttr_spaces():
    assert shorten(" L U F F Y ") == " L  F F Y "
