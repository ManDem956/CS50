from typing import NoReturn
import random

CONST_USER_PROMT = "Name"


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()

def validate_input_int(value: str) -> bool:
    return value.isdigit()


def main() -> NoReturn:
    while validate_input_int(user_input := get_user_input(CONST_USER_PROMT)):
        pass

    print(f"{user_input}")


if __name__ == "__main__":
    main()
