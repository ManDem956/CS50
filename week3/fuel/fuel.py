from typing import NoReturn

CONST_USER_PROMT = "Fraction"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def parse_fraction(input: str) -> tuple[int, int]:
    values = input.split('/')
    if len(values) != 2:
        raise ValueError(
            f"A fraction requires divident and divisor. Expected 2 values, got {len(values)}")

    # Will raise ValueError is int() conversion fails
    return int(values[0]), int(values[1])


def main() -> NoReturn:
    result = None
    while not result:
        input = get_user_input(CONST_USER_PROMT).lower()
        try:
            divident, divisor = parse_fraction(input)
            result = (divident / divisor)
        except (ValueError, ZeroDivisionError) as e:
            continue

    print(f"{result:.0%}") if result > 0.01 else print("E")


if __name__ == "__main__":
    main()
