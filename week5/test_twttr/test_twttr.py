from typing import NoReturn

WOVELS = "aeiou"


def shorten(word: str) -> str:
    res = ""
    for char in word:
        if char not in WOVELS:
            res += char

    return res


def main() -> NoReturn:
    pass


if __name__ == "__main__":
    main()
