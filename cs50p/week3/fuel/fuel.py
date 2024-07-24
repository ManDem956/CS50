CONST_USER_PROMPT = "Fraction"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def convert(input: str) -> int:
    # Will raise ValueError if int() conversion fails
    # Will raise ValueError if too many values to unpack
    dividend, divisor = (int(value) for value in input.split("/"))

    if dividend > divisor:
        raise ValueError("Dividend can not be larger than divisor.")

    return round((dividend / divisor) * 100)


def gauge(percentage: int) -> str:
    if percentage > 100 or percentage < 0:
        raise ValueError(f"Value {percentage=} is not within [0..100] range")
    elif percentage in range(2, 99):
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    return "F"


def main() -> None:
    while True:
        try:
            result = convert(get_user_input(CONST_USER_PROMPT))
        except (ValueError, ZeroDivisionError):
            continue
        else:
            print(gauge(result))
            break


if __name__ == "__main__":

    main()
