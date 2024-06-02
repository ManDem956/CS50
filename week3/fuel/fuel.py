from typing import NoReturn

CONST_USER_PROMT = "Fraction"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def convert_to_int(value: str) -> int:
    return int(value)


def parse_fraction(input: str) -> tuple[int, int]:
    values = input.split('/')
    if len(values) != 2:
        raise ValueError(
            f"A fraction rewuires divident and divisor. Expected 2 value, got {len(values)}")

    return int(values[0]), int(values[1])


def main() -> NoReturn:
    result = None
    while not result:
        input = get_user_input(CONST_USER_PROMT).lower()
        try:
            divident, divisor = parse_fraction(input)
            result = (divident / divisor)
        except (ValueError, ZeroDivisionError)  as e:
            continue

    print(f"{result:.0%}")


if __name__ == "__main__":
    main()
