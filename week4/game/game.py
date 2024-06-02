from typing import NoReturn
import random

CONST_USER_PROMT = "Name"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()

def validate_input_int(value: int) -> bool
    while True:


def main() -> NoReturn:
    user_input = get_user_input(CONST_USER_PROMT)

    print(f"{user_input}")


if __name__ == "__main__":
    main()
