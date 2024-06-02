from typing import NoReturn
import random

CONST_USER_PROMT_LEVEL = "Level"
CONST_USER_PROMT_GESS = "Your Guess"

def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()

def validate_input_int(value: str) -> bool:
    return value.isdigit()

def guess_game(target: int) -> NoReturn:
    while not validate_input_int(user_guess := get_user_input(CONST_USER_PROMT_LEVEL)):
        pass


def main() -> NoReturn:
    while not validate_input_int(level := get_user_input(CONST_USER_PROMT_LEVEL)):
        pass

    print(f"{level}")
    target = random.randint(1, level)



if __name__ == "__main__":
    main()
