from typing import NoReturn

CONST_START_AMOUNT_DUE = 50
CONST_ACCEPTED_COINS = [25, 10, 5]
CONST_USER_PROMT = "Please provide a camelCase variable"

def get_user_input(str) -> int:
    res: int = int(input(f"{str}: "))
    if res not in CONST_ACCEPTED_COINS:
        raise ValueError("Accepted coins are: {CONST_ACCEPTED_COINS}")
    return res


def main() -> NoReturn:
    amount_due = CONST_START_AMOUNT_DUE
    while amount_due >0:
        amount_due -= get_user_input(CONST_USER_PROMT)
    


if __name__ == "__main__":
    main()
