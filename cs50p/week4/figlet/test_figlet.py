import sys
import pytest
from figlet import main


CONST_CS50_SLANT = '   ___________ __________ \n  / ____/ ___// ____/ __ \\\n / /    \\__ \\/___ \\/ / / /\n/ /___ ___/ /___/ / /_/ / \n\\____//____/_____/\\____/  \n                          \n\n'  # noqa: E501


@pytest.mark.parametrize(
    "args, input,expected",
    [
        (["-f", "slant"], "CS50", CONST_CS50_SLANT),
    ],
)
def test_main(args, input, expected, monkeypatch, capfd):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ["mock"]+args)
        m.setattr("builtins.input", lambda _: input)
        main()
        out, err = capfd.readouterr()
        assert out == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        (["test"], "unrecognized arguments"),
        (["a", "slant"], "unrecognized arguments"),
    ],
)
def test_main_attr_error(args, expected, monkeypatch, capfd):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ["mock"]+args)
        with pytest.raises(SystemExit):
            main()
        out, err = capfd.readouterr()
        assert expected in err


@pytest.mark.parametrize(
    "args, expected",
    [
        (["-f", "wrong_fn t_name"], "Invalid font"),
    ],
)
def test_main_font_error(args, expected, monkeypatch, capfd):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ["mock"]+args)
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == expected
