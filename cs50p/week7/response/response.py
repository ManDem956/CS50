from validator_collection import validators


def validate(email: str) -> str:
    try:
        validators.email(email)
    except ValueError:
        return "Invalid"
    else:
        return "Valid"


def main() -> None:
    print(validate(input("Email: ").strip()))


if __name__ == "__main__":
    exit(main())
