import sys
import pytest
from dna import main


@pytest.mark.parametrize(
    "dict, sequence,expected",
    [
        ("databases/small.csv", "sequences/1.txt", "Bob\n"),
        ("databases/small.csv", "sequences/2.txt", "No match\n"),
        ("databases/small.csv", "sequences/3.txt", "No match\n"),
        ("databases/small.csv", "sequences/4.txt", "Alice\n"),
        ("databases/large.csv", "sequences/5.txt", "Lavender\n"),
        ("databases/large.csv", "sequences/6.txt", "Luna\n"),
        ("databases/large.csv", "sequences/7.txt", "Ron\n"),
        ("databases/large.csv", "sequences/8.txt", "Ginny\n"),
        ("databases/large.csv", "sequences/9.txt", "Draco\n"),
        ("databases/large.csv", "sequences/10.txt", "Albus\n"),
        ("databases/large.csv", "sequences/11.txt", "Hermione\n"),
        ("databases/large.csv", "sequences/12.txt", "Lily\n"),
        ("databases/large.csv", "sequences/13.txt", "No match\n"),
        ("databases/large.csv", "sequences/14.txt", "Severus\n"),
        ("databases/large.csv", "sequences/15.txt", "Sirius\n"),
        ("databases/large.csv", "sequences/16.txt", "No match\n"),
        ("databases/large.csv", "sequences/17.txt", "Harry\n"),
        ("databases/large.csv", "sequences/18.txt", "No match\n"),
        ("databases/large.csv", "sequences/19.txt", "Fred\n"),
        ("databases/large.csv", "sequences/20.txt", "No match\n"),
    ],
)
def test_main(monkeypatch, capfd, dict, sequence, expected):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', [sys.argv[0], dict, sequence])
        main()
        out, err = capfd.readouterr()
        assert out == expected
