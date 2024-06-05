import re

REGEX_TIME_12 = r"(\bum\b)"


def count(time_delta: str) -> str:
    pattern = re.compile(REGEX_TIME_12, flags=re.I)
    return len(tuple(re.finditer(pattern, time_delta)))


def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()
