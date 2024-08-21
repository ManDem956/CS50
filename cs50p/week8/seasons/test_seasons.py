import pytest
from datetime import date

# from seasons import Birthday as TimeCalculator
from seasons import TimeCalculator


@pytest.mark.parametrize(
    "new_today, input, expected",
    [
        (
            "2000-01-01",
            "1999-01-01",
            "Five hundred twenty-five thousand, six hundred minutes",
        ),
        (
            "2000-01-01",
            "1998-06-20",
            "Eight hundred six thousand, four hundred minutes",
        ),
        (
            "2000-01-01",
            "1995-01-01",
            "Two million, six hundred twenty-nine thousand, four hundred forty minutes",
        ),
        (
            "2003-01-01",
            "2001-01-01",
            "One million, fifty-one thousand, two hundred minutes",
        ),
        (
            "2032-01-01",
            "2020-06-01",
            "Six million, ninety-two thousand, six hundred forty minutes",
        ),
        (
            "2024-02-29",
            "2020-02-29",
            "Two million, one hundred three thousand, eight hundred forty minutes",
        ),
        (
            "2024-02-28",
            "2020-02-28",
            "Two million, one hundred three thousand, eight hundred forty minutes",
        ),
        (
            "2023-02-28",
            "2019-02-28",
            "Two million, one hundred three thousand, eight hundred forty minutes",
        ),
        (
            "2023-02-27",
            "2019-02-27",
            "Two million, one hundred three thousand, eight hundred forty minutes",
        ),
        (
            "2023-03-01",
            "2019-03-01",
            "Two million, one hundred three thousand, eight hundred forty minutes",
        ),
        (
            "2023-01-01",
            "2019-01-01",
            "Two million, one hundred three thousand, eight hundred forty minutes",
        ),
    ],
)
def test_calc(monkeypatch, new_today, input, expected):
    class MyDate(date):
        @classmethod
        def today(cls):
            return date.fromisoformat(new_today)

    monkeypatch.setattr("seasons.date", MyDate)
    calc = TimeCalculator(input)
    assert str(calc) == expected
