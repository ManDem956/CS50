import random
from typing import Sequence

CONST_USER_PROMPT_LEVEL = "Level: "
CONST_USER_PROMPT_GUESS = "Guess: "
CONST_GUESS_TOO_SMALL = "Too small! "
CONST_GUESS_TOO_LARGE = "Too large! "
CONST_GUESS_RIGHT = "Just right! "


def main(argv: Sequence | None = None) -> int:
    while True:
        try:
            level = int(input(CONST_USER_PROMPT_LEVEL))
            if level > 0:
                break
        except ValueError:
            continue

    target = random.randint(1, level)
    # print(target)

    try:
        while True:
            try:
                guess = int(input(CONST_USER_PROMPT_GUESS))
            except ValueError:
                continue

            if guess and target == guess:
                print(CONST_GUESS_RIGHT)
                break
            elif guess and target > guess:
                print(CONST_GUESS_TOO_SMALL)
                continue
            elif guess and target < guess:
                print(CONST_GUESS_TOO_LARGE)
                continue
    except EOFError:
        return


if __name__ == "__main__":
    exit(main())
