from typing import NoReturn
import argparse

CONST_USER_PROMT_LEVEL = "Level"


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


def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Bitcoun", description="Calculate the cost for users bitcoin amount")
    parser.add_argument("amount", required=True)
    args = parser.parse_args()

    main(args.amount)
