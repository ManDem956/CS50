from collections import defaultdict

CONST_USER_PROMPT = ""


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def main() -> None:
    groceries = defaultdict(int)
    while True:
        try:
            input = get_user_input(CONST_USER_PROMPT, "").upper()
            groceries[input] += 1
        except EOFError:
            print()
            for key, value in sorted(groceries.items()):
                print(f"{value} {key}")
            break


if __name__ == "__main__":
    main()
