from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Date"
CONST_MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def get_us_date_numerical(value: str) -> tuple[str, str, str]:
    month, day, year = (int(element) for element in value.split("/"))

    if day > 31:
        raise ValueError("Day can not be larger han 31.")

    month =CONST_MONTHS.index(month.tiile())
    if month <0:
        raise ValueError("Invalid month value.")

    return f"{year:>04}", f"{month:>02}", f"{day:>02}"


def get_us_date_human(value: str) -> tuple[str, str, str]:
    month, day, year = (element.strip().strip(',')
                        for element in value.split("/"))

    if int(day) > 31:
        raise ValueError("Day can not be larger han 31")

    return f"{year:>04}", f"{month:>02}", f"{day:>02}"


def get_iso_date(year: str, month: str, day: str) -> str:
    return "-".join((year, month, day))


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    print(get_iso_date(*get_us_date_numerical(input)))


if __name__ == "__main__":
    main()
