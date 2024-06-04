from typing import NoReturn

CONST_USER_PROMT = "Fraction"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def convert(input: str) -> int:
    # Will raise ValueError if int() conversion fails
    # Will raise ValueError if too many values to unpack
    dividend, divisor = (int(value) for value in input.split('/'))


    if dividend > divisor:
        raise ValueError(
            f"Dividend can not be larger than divisor.")

    return round((dividend / divisor) * 100)


def gauge(percentage: int) -> str:
    if percentage in range(2, 99):
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    else:
        return "F"


def main() -> NoReturn:
    while True:
        try:
            result = convert(get_user_input(CONST_USER_PROMT).lower())
        except (ValueError, ZeroDivisionError) as e:
            continue
        else:
            print(gauge(result))
            break


if __name__ == "__main__":
    main()
