from typing import NoReturn
import random

CONST_USER_PROMT = "Name"


def get_user_input(message: str, sep: str = ": ", validator:Callable) -> Any:
    while True:
        try:
            res: int = validator(input(f"{message}{sep}").strip())
        except ValueError as e:
            continue
        else:
            return res


def main() -> NoReturn:
    user_input = get_user_input(CONST_USER_PROMT)

    print(f"{user_input}")


if __name__ == "__main__":
    main()
