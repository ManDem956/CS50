from typing import NoReturn

CONST_START_AMOUNT_DUE = 50
CONST_ACCEPTED_COINS = [25, 10, 5]
CONST_USER_PROMT = "Insert coin"


def get_user_input(str) -> int:
    res: int = int(input(f"{str}: "))
    if res not in CONST_ACCEPTED_COINS:
        return 0
    return res


def main() -> None:
    amount_due = CONST_START_AMOUNT_DUE
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        amount_due -= get_user_input(CONST_USER_PROMT)
    print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
