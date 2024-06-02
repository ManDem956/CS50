from typing import NoReturn
from pyfiglet import Figlet

CONST_USER_PROMT = "Input"
# CONST_LANGUAGES = ["en", "alias"]

def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def get_emoji(input: str) -> str:
    for language in ['alias'] + emoji.LANGUAGES:
        result = emoji.emojize(input, language=language)
        if result != input:
            break

    return result


def main() -> NoReturn:
    figlet = Figlet()
    input = get_user_input(CONST_USER_PROMT)
    result = get_emoji(input)
    print(result)


if __name__ == "__main__":
    main()
