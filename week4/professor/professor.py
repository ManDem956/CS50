from typing import NoReturn
import random

CONST_USER_PROMT_LEVEL = "Level"
CONST_USER_PROMT_GESS = "Guess"
CONST_GUESS_TOO_SMALL = "Too small!"
CONST_GUESS_TOO_LARGE = "Too large!"
CONST_GUESS_RIGHT = "Just right!"


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()


def get_level(message: str = CONST_USER_PROMT_LEVEL) -> int:
    result = 0
    while not result in range(1, 4):
        try:
            result = int(get_user_input(message))
        except ValueError as e:
            continue

    return result


def generate_integer(level: int) -> int:
    if level not in range(1, 4):
        raise ValueError("Level must in range [1..3] inclusive")

    return random.randrange(10**(level-1), 10**level)


def do_game(level) -> int:
    tries = 3
    left, right = generate_integer(level), generate_integer(level)
    while tries > 0:
        try:
            answer = int(get_user_input(f"{left} + {right} ="))
            if answer == left + right:
                return 1
        except ValueError as e:
            continue
        finally:
            tries -= 1

    return 0


def main() -> NoReturn:
    level = get_level(CONST_USER_PROMT_LEVEL)
    score = 0
    for _ in range(10):
        score += do_game(level)

    print(score)


if __name__ == "__main__":
    main()
