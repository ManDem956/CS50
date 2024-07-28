from string import ascii_uppercase as caps


def convert(value: str) -> str:
    result = ""
    for character in value:
        if character in caps:
            result += "_"
        result += character.lower()
    return result


def main() -> None:
    user_input: str = input("Please provide a camelCase variable: ").strip()
    print(f"snake_case: {convert(user_input)}")


if __name__ == "__main__":
    main()
