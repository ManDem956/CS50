from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Date"



def get_user_input(message:str, sep:str=": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res

def get_us_dage_numerical(value:str) -> tuple[int, int, int]:
    month, day, tear = value.split("/")

    if day >31:
        raise ValueError("Day can not be larger han 31")

    return month, day, tear



def main() -> NoReturn:
    groceries = defaultdict(int)
    input = get_user_input(CONST_USER_PROMT)


if __name__ == "__main__":
    main()
