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

    return f"{year:>04}", f"{month:>02}", f"{day:>02}"


def get_us_date_human(value: str) -> tuple[str, str, str]:
    month, day, year = (element.strip().strip(',')
                        for element in value.split("/"))

    month = CONST_MONTHS.index(month.title())
    if month < 0:
        raise ValueError("Invalid month value.")

    return f"{year:>04}", f"{month:>02}", f"{day:>02}"


def format_iso_date(year: str, month: str, day: str) -> str:
    if int(day) > 31:
        raise ValueError("Day can not be larger han 31")
    
    return "-".join((year, month, day))


def get_date_value(value: str) -> tuple[str, str, str]:
    methods = [get_us_date_human, get_us_date_numerical]
    result = None
    for method in methods:
        try:
            result = method(value)
        except ValueError as e:
            continue
    return result


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    result = get_date_value(inpur)

    if result:
        print(format_iso_date(*result))


if __name__ == "__main__":
    main()
