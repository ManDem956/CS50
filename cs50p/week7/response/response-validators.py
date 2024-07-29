import validators


def validate(email: str) -> str:
    result = "Valid" if validators.email(email) else "Invalid"
    return result


def main() -> None:
    print(validate(input("Email: ").strip()))


if __name__ == "__main__":
    exit(main())
