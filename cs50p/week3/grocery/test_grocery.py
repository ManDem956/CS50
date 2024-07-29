import pytest
from grocery import main


class Test_Main:
    @pytest.mark.parametrize(
        "input,expected",
        [
            (("Apple", "banana", "BANANA", "ICE cream", "^D"), "\n1 APPLE\n2 BANANA\n1 ICE CREAM\n"),
            (("milk", "MiLk", "^D"), "\n2 MILK\n"),
            (("MANGO", "strawberry", "^D"), "\n1 MANGO\n1 STRAWBERRY\n"),
            (("SWEET potato", "TOrTIlla", "^D"), "\n1 SWEET POTATO\n1 TORTILLA\n"),
        ],
    )
    def test_main(self, input, expected, monkeypatch, capfd):

        def gen_answers(input):
            for res in input:
                if res == "^D":
                    raise EOFError()
                yield res

        answers = iter(gen_answers(input))

        monkeypatch.setattr("builtins.input", lambda _: next(answers))
        main()
        out, err = capfd.readouterr()
        assert out == expected
