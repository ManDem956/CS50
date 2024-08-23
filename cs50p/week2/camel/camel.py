def convert(value: str) -> str:
    result = "".join("_" * character.isupper() + character.lower() for character in value)
    return result


def main() -> None:
    user_input: str = input("Please provide a camelCase variable: ").strip()
    print(f"snake_case: {convert(user_input)}")


if __name__ == "__main__":
    main()
