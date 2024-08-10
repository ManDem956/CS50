from io import StringIO
import random

import pytest
from game import main, CONST_GUESS_TOO_SMALL, CONST_GUESS_RIGHT, CONST_USER_PROMPT_GUESS, CONST_USER_PROMPT_LEVEL  # noqa, E501


@pytest.mark.parametrize(
    "input,expected",
    [
        ("\n".join(("10", "1", "7")), f"{CONST_USER_PROMPT_LEVEL}{CONST_USER_PROMPT_GUESS}{CONST_GUESS_TOO_SMALL}\n{CONST_USER_PROMPT_GUESS}{CONST_GUESS_RIGHT}\n"),  # noqa, E501
        ("\n".join(("10", "0", "7")), f"{CONST_USER_PROMPT_LEVEL}{CONST_USER_PROMPT_GUESS}{CONST_USER_PROMPT_GUESS}{CONST_GUESS_RIGHT}\n"),  # noqa, E501
        ("\n".join(("10", "-1", "7")), f"{CONST_USER_PROMPT_LEVEL}{CONST_USER_PROMPT_GUESS}{CONST_USER_PROMPT_GUESS}{CONST_GUESS_RIGHT}\n"),  # noqa, E501
    ],
)
def test_main_strdin(input, expected, monkeypatch, capsys):
    random.seed(0)
    with monkeypatch.context() as m:
        m.setattr("sys.stdin", StringIO(input))
        main()
        out, err = capsys.readouterr()
        assert out == expected
