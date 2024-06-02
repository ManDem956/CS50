from typing import NoReturn
from collections import defaultdict

CONST_USER_PROMT = "Item"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    groceries = defaultdict()
    while True:
        try:
            input = get_user_input(CONST_USER_PROMT)
            total += CONST_MENU.get(input.title(), 0)
            print(f"Total: ${total:.2f}")
        except EOFError:
            break




if __name__ == "__main__":
    main()
