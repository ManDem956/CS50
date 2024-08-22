import re


# REGEX_TIME_12 = r"(\b(?:1[0-2]|0?[1-9])(?::(?:[0-5][0-9])?)?\s(?:AM|PM)\b)(\sto\s)(\b(?:1[0-2]|0?[1-9])(?::(?:[0-5][0-9])?)?\s(?:AM|PM)\b)"  # noqa: E501
# REGEX_TIME_12 = r"\b((?:1[0-2]|0?[1-9])(?::(?:[0-5][0-9])?)?)\s((?:AM|PM))(\sto\s)?"  # noqa: E501
# REGEX_TIME_12 = r"\b(?:(1[0-2]|0?[1-9])(?::([0-5][0-9])?)?)\s((?:AM|PM))(?:\s(to)\s)?"  # noqa: E501
REGEX_TIME_12 = r"\b(?:(0?[1-9]|1[0-2]):?([0-5][0-9])?\s(AM|PM))\sto\s(?:(0?[1-9]|1[0-2]):?([0-5][0-9])?\s(AM|PM))\b"  # noqa: E501
# REGEX_TIME_12 = r"(?:(1[0-2]|0?[1-9]):?([0-5][0-9])?\s(AM|PM)(?:\s(to)\s)?){2}"
# current   ^(\d{1,2})(?::?(\d{1,2}))? (AM|PM) to (\d{1,2})(?::? (\d{1,2})?) (AM|PM)$
# fixed     ^(\d{1,2})(?::?(\d{1,2}))? (AM|PM) to (\d{1,2})(?::?(\d{1,2}))? (AM|PM)


def convert_12_to_24(hours, minutes, noon) -> str:
    if not minutes:
        minutes = 0

    hours = int(hours)
    minutes = int(minutes)

    if hours > 12 or minutes > 59 or noon not in ("AM", "PM"):
        raise ValueError("Invalid hours value")

    if noon == "AM":
        hours = hours % 12
    elif noon == "PM" and (hours % 12) > 0:
        hours += 12

    return f"{hours:>02}:{minutes:>02}"


def chunked(iterable, n):
    return zip(*([iter(iterable)] * n))


def convert(time_delta: str) -> str:
    result = re.fullmatch(REGEX_TIME_12, time_delta, re.I)

    if not result:
        raise ValueError(f"Invalid time delta: {time_delta}")

    res = " to ".join(convert_12_to_24(*time) for time in chunked(result.groups(), 3))

    return res


def main() -> None:
    print(convert(input("Time delta: ")))


if __name__ == "__main__":
    main()
