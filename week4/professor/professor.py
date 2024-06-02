from typing import NoReturn
import random

CONST_USER_PROMT_LEVEL = "Level"
CONST_USER_PROMT_GESS = "Guess"
CONST_GUESS_TOO_SMALL = "Too small!"
CONST_GUESS_TOO_LARGE = "Too large!"
CONST_GUESS_RIGHT = "Just right!"


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()


def get_user_input_int(message: str = CONST_USER_PROMT_LEVEL, bounds: tuple[int, int]) -> int:
    result = 0
    while not result in range(bounds):
        try:
            result = int(get_user_input(message))
        except ValueError as e:
            continue

    return result


def get_level(message: str = CONST_USER_PROMT_LEVEL) -> int:
    return get_user_input_int(message, (1, 4))


def generate_integer(level: int) -> int:
    if level not in range(1, 4):
        raise ValueError("Level must in range [1..3] inclusive")

    return random.randrange(10**(level-1), 10**level)


def main() -> NoReturn:
    level = get_level(CONST_USER_PROMT_LEVEL)
    problems = []
    for _ in range(10):
        left, right = generate_integer(level), generate_integer(level)
        answer = get_user_input_int(f"{left} + {right} = ", )

    print(problems)


if __name__ == "__main__":
    main()
