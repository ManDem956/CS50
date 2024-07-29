from io import StringIO
import random

import pytest
from game import main, CONST_GUESS_TOO_LARGE, CONST_GUESS_TOO_SMALL, CONST_GUESS_RIGHT, CONST_USER_PROMPT_GUESS, CONST_USER_PROMPT_LEVEL


@pytest.mark.parametrize(
    "input,expected",
    [
        ("\n".join(("1", "1")), f"{CONST_USER_PROMPT_LEVEL} {CONST_USER_PROMPT_GUESS} {CONST_GUESS_RIGHT}\n"),
        ("\n".join(("10", "100", "7")), f"{CONST_USER_PROMPT_LEVEL} {CONST_USER_PROMPT_GUESS} {CONST_GUESS_TOO_LARGE}\n{CONST_USER_PROMPT_GUESS} {CONST_GUESS_RIGHT}\n"), # noqa, E501
        ("\n".join(("10", "1", "7")), f"{CONST_USER_PROMPT_LEVEL} {CONST_USER_PROMPT_GUESS} {CONST_GUESS_TOO_SMALL}\n{CONST_USER_PROMPT_GUESS} {CONST_GUESS_RIGHT}\n"), # noqa, E501
        ("\n".join(("10", "0", "7")), f"{CONST_USER_PROMPT_LEVEL} {CONST_USER_PROMPT_GUESS} {CONST_USER_PROMPT_GUESS} {CONST_GUESS_RIGHT}\n"),
    ],
)
def test_main_strdin(input, expected, monkeypatch, capsys):
    random.seed(0)

    # def gen_answers(input):
    #     for res in input:
    #         if res == "^D":
    #             raise EOFError()
    #         yield res
    # answers = gen_answers(input)

    with monkeypatch.context() as m:
        m.setattr("sys.stdin", StringIO(input))
        main()
        out, err = capsys.readouterr()
        assert out == expected
