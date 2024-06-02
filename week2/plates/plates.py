from typing import NoReturn

CONST_VOWELS = "AEIOU"
CONST_USER_PROMT = "Plate"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    if is_valid(input):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str) -> bool:
    if s.lemgth() > 6:
        return false


if __name__ == "__main__":
    main()
