CONST_VOWELS = "AEIOU"
CONST_USER_PROMPT = "Input"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> None:
    input = get_user_input(CONST_USER_PROMPT)
    result = ""
    for character in input:
        if character.upper() not in CONST_VOWELS:
            result += character

    print(f"Output: {result.strip()}")


if __name__ == "__main__":
    main()
