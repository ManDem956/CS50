import re

REGEXP = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"

# REGEXP = r"\b(?:(?:25[0-5]?))\b"


def validate(ip):
    return re.fullmatch(REGEXP, ip) is not None


def main() -> None:
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
