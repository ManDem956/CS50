import pytest
from coke import main


@pytest.mark.parametrize(
    "input,expected",
    [
        ((25, 25), ("Amount Due: 50", "Amount Due: 25", "Change Owed: 0")),
        ((10, 5, 10, 25), ("Amount Due: 50", "Amount Due: 40", "Amount Due: 35", "Amount Due: 25", "Change Owed: 0")),
        ((25, 10, 25), ("Amount Due: 50", "Amount Due: 25", "Amount Due: 15", "Change Owed: 10")),
        ((10, 49, 5, 10, 25), ("Amount Due: 50", "Amount Due: 40",
         "Amount Due: 40", "Amount Due: 35", "Amount Due: 25", "Change Owed: 0")),
    ],
)
def test_main(input, expected, capfd, monkeypatch):
    answers = iter(input)
    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    main()
    out, err = capfd.readouterr()

    result = out.rstrip("\n").split("\n")
    assert len(result) == len(expected)

    for res, expect in zip(result, expected):
        assert res == expect
