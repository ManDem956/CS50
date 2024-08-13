import random

CONST_USER_PROMPT_LEVEL = "Level"
CONST_ERROR = "EEE"
CONST_ALLOW_RANGE = range(1, 4)


def get_user_input(message: str, sep: str = ": ") -> str:
    return input(f"{message}{sep}").strip()


def get_level(message: str = CONST_USER_PROMPT_LEVEL) -> int:
    result = 0
    while result not in CONST_ALLOW_RANGE:
        try:
            result = int(get_user_input(message))
        except ValueError:
            continue

    return result


def generate_integer(level: int) -> list[tuple[int, int]]:
    if level not in CONST_ALLOW_RANGE:
        raise ValueError(f"Level must in range {list(CONST_ALLOW_RANGE)}")
    the_range = (10**level,) if level <= 1 else (10 ** (level - 1), (10**level))

    result = []
    for _ in range(10):
        result.append((random.randrange(*the_range), random.randrange(*the_range)))
    return result


def do_game(left, right) -> int:
    tries = 3
    # left, right = generate_integer(level), generate_integer(level)
    while tries > 0:
        try:
            answer = int(get_user_input(f"{left} + {right} =", sep=" "))
            if answer != left + right:
                raise ValueError("Answer is incorrect")
        except ValueError:
            print(CONST_ERROR)
        else:
            return 1
        finally:
            tries -= 1

    print(f"{left} + {right} = {left+right}")
    return 0


def main() -> None:
    random.seed(0)
    level = get_level(CONST_USER_PROMPT_LEVEL)
    score = 0
    values = generate_integer(level)
    print(values)
    for left, right in values:
        score += do_game(left, right)

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
