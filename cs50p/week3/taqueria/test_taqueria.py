from io import StringIO
import random

import pytest
from taqueria import main


@pytest.mark.parametrize(
    "input,expected",
    [
        ("\n".join(("burrito", "large quesadilla", "super quesadilla")),
         "Item: Total: $7.50\nItem: Item: Total: $17.00\nItem: \n"),
    ],
)
def test_main_strdin_reprompt(input, expected, monkeypatch, capsys):
    random.seed(0)
    with monkeypatch.context() as m:
        m.setattr("sys.stdin", StringIO(input))
        main()
        out, err = capsys.readouterr()
        assert out == expected
