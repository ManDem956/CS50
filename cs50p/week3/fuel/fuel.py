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

    result = round((dividend / divisor) * 100)

    if result not in range(0, 101):
        raise ValueError("Result must be an int between 0 and 100, inclusive.")

    return result


def gauge(percentage: int) -> str:
    if percentage in range(2, 99):
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    return "F"


def main() -> None:
    while True:
        try:
            result = convert(get_user_input(CONST_USER_PROMPT))
        except (ValueError, ZeroDivisionError) as e:
            print(str(e))
            continue
        else:
            print(gauge(result))
            break


if __name__ == "__main__":

    main()
