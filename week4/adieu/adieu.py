from typing import NoReturn
import inflect

CONST_USER_PROMT = "Name"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def main(p: inflect.engine) -> NoReturn:
    user_input = []
    while True:
        try:
            user_input.append(get_user_input(CONST_USER_PROMT))
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(user_input)}")

if __name__ == "__main__":
    p = inflect.engine()
    main(p)
