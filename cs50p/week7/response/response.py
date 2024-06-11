from validator_collection import validators


def validate(email: str) -> str:
    return validators.email(email)


def main() -> None:
    try:
        validate(input("Email: ").strip())
    except ValueError:
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()
