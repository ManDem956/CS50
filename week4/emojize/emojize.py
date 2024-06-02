from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Date"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def get_emoji(input: str) -> str

def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    result = get_emoji(input)
    print(result)


if __name__ == "__main__":
    main()
