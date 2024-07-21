import pytest
import seasons
from datetime import date


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
    ],
)
def test_calc(monkeypatch, new_today, input, expected):
    class MyDate(date):
        def today():
            return date.fromisoformat(new_today)

    monkeypatch.setattr(seasons.datetime, "date", MyDate)
    calc = seasons.TimeCalculator(input)
    assert calc.humanize() == expected
