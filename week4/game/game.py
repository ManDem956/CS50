from typing import NoReturn
import random

CONST_USER_PROMT_LEVEL = "Level"
CONST_USER_PROMT_GESS = "Your Guess"
CONST_GUESS_TOO_SMALL = "Too small!"
CONST_GUESS_TOO_LARGE = "Too large!"
CONST_GUESS_RIGHT = "Just right!"


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()


def get_user_input_int(message: str) -> int:
    while not (result := get_user_input(message)).isdigit():
        pass

    return int(result)


def guess_game(target: int) -> NoReturn:
    user_guess = get_user_input_int(CONST_USER_PROMT_GESS)
    while user_guess != target:
        if user_guess < target:
            print("")



def main() -> NoReturn:
    level = get_user_input_int(CONST_USER_PROMT_LEVEL)

    print(f"{level}")
    target=random.randint(1, level)



if __name__ == "__main__":
    main()
