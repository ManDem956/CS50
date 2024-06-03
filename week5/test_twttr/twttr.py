from typing import NoReturn

CONST_USER_PROMT = "Input"
WOVELS = "aeiou"


def shorten(word: str) -> str:
    res = ""
    for char in word:
        if char not in WOVELS:
            res += char

    return res


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    result = shorten(input)
    print(f"Output: {result.strip()}")


if __name__ == "__main__":
    main()
