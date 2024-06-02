from typing import NoReturn

CONST_USER_PROMT = "Fraction"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def parse_fraction(input: str) -> tuple[int, int]:
    # Will raise ValueError if int() conversion fails
    # Will raise ValueError if too many values to unpack
    divident, divisor = (int(value) for value in input.split('/'))

    if divident > divisor:
        raise ValueError(
            f"Divient can not be larger tan divisor.")

    return divident, divisor


def main() -> NoReturn:
    result = None
    while result is None:
        input = get_user_input(CONST_USER_PROMT).lower()
        try:
            divident, divisor = parse_fraction(input)
            result = (divident / divisor)
        except (ValueError, ZeroDivisionError) as e:
            continue

    message: str = ""
    if 0.01 < result < 0.99:
        message = f"{result:.0%}"
    elif result <= 0.01:
        message = "E"
    else:
        message = "F"
    print(message)


if __name__ == "__main__":
    main()
