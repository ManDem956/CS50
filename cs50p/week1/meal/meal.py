def convert(time: str) -> float:
    hours, minutes = time.split(":")
    if not hours or not minutes:
        raise ValueError(f"Incorrect time format: `{time=}`")
    if int(hours) not in range(0, 24):
        raise ValueError(f"Incorrect value for hours: `{hours=}`")
    if int(minutes) not in range(0, 60):
        raise ValueError(f"Incorrect value for minutes: `{minutes=}`")

    return (float(hours) * 60 + float(minutes)) / 60


def get_meal(value: float) -> str:
    result = None
    match value:
        case num if 7.0 <= num <= 8.0:
            result = "breakfast"
        case num if 12.0 <= num <= 13.0:
            result = "lunch"
        case num if 18.0 <= num <= 19.0:
            result = "dinner"
    return result


def main() -> None:
    user_input: str = input("What time is it? ").strip().lower()
    result = get_meal(convert(user_input))
    if result:
        print(f"{result} time")


if __name__ == "__main__":
    exit(main())
