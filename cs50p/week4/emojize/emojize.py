import emoji

CONST_USER_PROMPT = "Input"
# CONST_LANGUAGES = ["en", "alias"]


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def get_emoji(input: str) -> str:
    result = emoji.emojize(input, language='alias')
    return result


def main() -> None:
    input = get_user_input(CONST_USER_PROMPT)
    result = get_emoji(input)
    print(result)


if __name__ == "__main__":
    exit(main())
