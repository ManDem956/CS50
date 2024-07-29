import pytest
from adieu import main


class Test_Main:
    @pytest.mark.parametrize(
        "input,expected",
        [
            (("Liesl", "^D"), "\nAdieu, adieu, to Liesl\n"),
            (("Liesl", "Friedrich", "^D"), "\nAdieu, adieu, to Liesl and Friedrich\n"),
            (("Liesl", "Friedrich", "Louisa", "^D"), "\nAdieu, adieu, to Liesl, Friedrich, and Louisa\n"),
            (("Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", "Gretl", "^D"),
             "\nAdieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl\n"),
        ],
    )
    def test_main(self, input, expected, monkeypatch, capfd):

        def gen_answers(input):
            for res in input:
                if res == "^D":
                    raise EOFError()
                yield res
        monkeypatch.setattr("builtins.input", lambda _: next(answers))

        answers = iter(gen_answers(input))

        main()
        out, err = capfd.readouterr()
        assert out == expected
