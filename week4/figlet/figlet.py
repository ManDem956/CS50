from pyfiglet import Figlet
import argparse
import random

CONST_USER_PROMPT = "Input"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def render(f: Figlet, input: str) -> str:
    return f.renderText(input)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Figlet", description="Renders user's input in ASCII font"
    )
    parser.add_argument("-f", "--font",
                        default=random.choice(Figlet().getFonts()))
    args = parser.parse_args()

    figlet = Figlet()
    figlet.setFont(font=args.font)

    input = get_user_input(CONST_USER_PROMPT)

    print(render(figlet, input))


if __name__ == "__main__":
    main()
