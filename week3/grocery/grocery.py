from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Item"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    groceries = defaultdict(int)
    while True:
        try:
            input = get_user_input(CONST_USER_PROMT).upper()
            groceries[input] += 1
        except EOFError:
            for key, value in sorted(groceries.items()):
                print(f"{value}. {key}")
            break


if __name__ == "__main__":
    main()
