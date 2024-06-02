from typing import NoReturn
from pyfiglet import Figlet
import argparse
import random

CONST_USER_PROMT = "Input"
# CONST_LANGUAGES = ["en", "alias"]


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def main(f: Figlet) -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    print(f.renderText(input))


if __name__ == "__main__":
    figlet = Figlet()
    parser = argparse.ArgumentParser(
        prog='Figlet',
        description='Rengers user\'s input in ASCII font')
    parser.add_argument(
        '-f', '--font', default=random.choice(figlet.getFonts()))
    args = parser.parse_args()
    figlet.setFont(font=args.font)
    main(figlet)
