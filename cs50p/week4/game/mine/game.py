import random

CONST_USER_PROMPT_LEVEL = "Level:"
CONST_USER_PROMPT_GUESS = "Guess:"
CONST_GUESS_TOO_SMALL = "Too small!"
CONST_GUESS_TOO_LARGE = "Too large!"
CONST_GUESS_RIGHT = "Just right!"


def get_user_input(message: str) -> str:
    return input(f"{message}").strip()


def get_user_input_int(message: str) -> int:
    result = 0
    while result <= 0:
        try:
            result = int(get_user_input(f"{message} "))
        except ValueError:
            continue

    return result


def guess_game(target: int) -> None:
    try:
        while (user_guess :=
               get_user_input_int(CONST_USER_PROMPT_GUESS)) != target:
            if user_guess < target:
                print(CONST_GUESS_TOO_SMALL)
            else:
                print(CONST_GUESS_TOO_LARGE)
    except EOFError:
        return

    print(CONST_GUESS_RIGHT)


def main() -> None:
    level = get_user_input_int(CONST_USER_PROMPT_LEVEL)

    target = random.randint(1, level)
    guess_game(target)


if __name__ == "__main__":
    random.seed(0)
    main()
