import inflect

CONST_USER_PROMPT = "Name"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def main() -> None:
    p = inflect.engine()
    user_input = []
    while True:
        try:
            user_input.append(get_user_input(CONST_USER_PROMPT))
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(user_input)}")


if __name__ == "__main__":
    exit(main())
