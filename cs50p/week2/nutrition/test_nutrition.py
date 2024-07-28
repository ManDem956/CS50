import pytest
from nutrition import main


@pytest.mark.parametrize(
    "input,expected",
    [
        ("apple", "Calories: 130\n"),
        ("avocado", "Calories: 50\n"),
        ("banana", "Calories: 110\n"),
        ("cantaloupe", "Calories: 50\n"),
        ("grapefruit", "Calories: 60\n"),
        ("grapes", "Calories: 90\n"),
        ("honeydew melon", "Calories: 50\n"),
        ("kiwifruit", "Calories: 90\n"),
        ("lemon", "Calories: 15\n"),
        ("lime", "Calories: 20\n"),
        ("nectarine", "Calories: 60\n"),
        ("orange", "Calories: 80\n"),
        ("peach", "Calories: 60\n"),
        ("pear", "Calories: 100\n"),
        ("pineapple", "Calories: 50\n"),
        ("plums", "Calories: 70\n"),
        ("strawberries", "Calories: 50\n"),
        ("sweet cherries", "Calories: 100\n"),
        ("tangerine", "Calories: 50\n"),
        ("watermelon", "Calories: 80\n"),
        ("negative test", ""),

    ],
)
def test_main(input, expected, capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input)

    main()
    out, err = capfd.readouterr()
    assert out == expected
