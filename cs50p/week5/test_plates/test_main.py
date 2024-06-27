import pytest
from plates import main


class Test_Main:
    @pytest.mark.parametrize(
        "input,expected",
        [
            ("CS50", "Valid\n"),
            ("CS05", "Invalid\n"),
            ("ECTO88", "Valid\n"),
            ("50", "Invalid\n"),
            ("CS50P2", "Invalid\n"),
            ("PI3.14", "Invalid\n"),
            ("@#$!%^", "Invalid\n"),
            ("BGH2!", "Invalid\n"),
            ("H", "Invalid\n"),
            ("OUTATIME", "Invalid\n"),
            ("NRVOUS", "Valid\n"),
        ],
    )
    def test_main(self, input, expected, monkeypatch, capfd):
        monkeypatch.setattr("builtins.input", lambda _: input)
        main()
        out, err = capfd.readouterr()
        assert out == expected
