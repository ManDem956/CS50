from typing import NoReturn
import random

CONST_USER_PROMT_LEVEL = "Level"
CONST_USER_PROMT_GESS = "Guess"
CONST_GUESS_TOO_SMALL = "Too small!"
CONST_GUESS_TOO_LARGE = "Too large!"
CONST_GUESS_RIGHT = "Just right!"


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()


def get_user_input_int(message: str) -> int:
    while result > 0:
        pass

    return int(result)


def guess_game(target: int) -> NoReturn:
    while (user_guess := get_user_input_int(CONST_USER_PROMT_GESS)) != target:
        if user_guess < target:
            print(CONST_GUESS_TOO_SMALL)
        else:
            print(CONST_GUESS_TOO_LARGE)

    print(CONST_GUESS_RIGHT)


def main() -> NoReturn:
    level = get_user_input_int(CONST_USER_PROMT_LEVEL)

    target = random.randint(1, level)
    guess_game(target)


if __name__ == "__main__":
    main()
