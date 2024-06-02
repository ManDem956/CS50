from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Date"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def main() -> NoReturn:
    result = None
    while result is None:
        try:
            input = get_user_input(CONST_USER_PROMT)
            result = format_iso_date(*get_date_value(input))
            print(result)
        except ValueError as e:
            continue


if __name__ == "__main__":
    main()
