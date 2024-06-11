from string import ascii_uppercase as caps


def main() -> None:
    user_input: str = input("Please provide a camelCase variable: ").strip()
    result = ""
    for character in user_input:
        if character in caps:
            result += "_"
        result += character.lower()

    print(f"snake_case: {result}")


if __name__ == "__main__":
    main()
