from io import StringIO
import pytest
from outdated import get_date_value, main


@pytest.mark.parametrize(
    "input,expected",
    [
        ("9/8/1636", ("1636", "09", "08")),
        ("September 8, 1636", ("1636", "09", "08")),
    ],
)
def test_get_date_value(input, expected):
    assert get_date_value(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("9/8/1636", "1636-09-08"),
        ("September 8, 1636", "1636-09-08"),
    ],
)
def test_main_strdin_reprompt(input, expected, monkeypatch, capsys):
    with monkeypatch.context() as m:
        m.setattr("sys.stdin", StringIO(input))
        main()
        out, err = capsys.readouterr()
        assert out == expected
