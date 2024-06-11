import re


REGEX_TIME_12 = r"(\b(?:1[0-2]|0?[1-9])(?::(?:[0-5][0-9])?)?\s(?:AM|PM)\b)(\sto\s)(\b(?:1[0-2]|0?[1-9])(?::(?:[0-5][0-9])?)?\s(?:AM|PM)\b)"


def convert_12_to_24(value: str) -> str:
    time, noon = value.split()
    hours, _, minutes = time.partition(":")

    if not minutes:
        minutes = "00"

    if noon == "PM":
        hours = str(int(hours) + 12) if int(hours) < 12 else hours
    else:
        hours = str(int(hours) % 12)

    return f"{hours:>02}:{minutes}"


def do_replace(match: re.Match) -> str:
    return f"{convert_12_to_24(match.group(1))}\
        {match.group(2)}{convert_12_to_24(match.group(3))}"


def convert(time_delta: str) -> str:
    pattern = re.compile(REGEX_TIME_12)
    res = re.sub(pattern, do_replace, time_delta)

    if res == time_delta:
        raise ValueError(f"Invalid time delta: {time_delta}")

    return res


def main() -> None:
    print(convert(input("Time delta: ")))


if __name__ == "__main__":
    main()
