from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Date"



def get_user_input(message:str, sep:str=": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res

def get_us_date_numerical(value:str) -> tuple[int, int, int]:
    month, day, tear = (int(element) for element in value.split("/"))

    if day >31:
        raise ValueError("Day can not be larger han 31")

    return month, day, tear

def get_iso_date(year:int, month:int, day:int) -> str:
    return "-".join((year, month, day))


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    print(get_iso_date(*get_us_date_numerical(input)))

if __name__ == "__main__":
    main()
