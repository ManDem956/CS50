from typing import NoReturn

CONST_USER_PROMT = "Input"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def value(greeting: str) -> int:
    res = 100
    if greeting.lower().startswith('hello'):
        res = 0
    elif greeting.lower().startswith('h'):
        res = 20
    return res


def main() -> NoReturn:
    user_input: str = get_user_input(CONST_USER_PROMT)
    print(f"${value(user_input)}")


if __name__ == "__main__":
    main()
