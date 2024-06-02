from typing import NoReturn

CONST_VOWELS = "AEIOU"
CONST_USER_PROMT = "Insert coin"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    input = get_user_input("Input")
    result = ""
    for character in input:
        if character.upper() not in CONST_VOWELS:
            result += character

    print(f"Output: {result.strip()}")


if __name__ == "__main__":
    main()
