from cmath import e
from validator_collection import validators

REGEX_TIME_12 = r"(\bum\b)"


def validate(email: str) -> str:
    return validators.email(email)


def main():
    try:
        validate(input("Email: ").strip())
    except ValueError:
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()
