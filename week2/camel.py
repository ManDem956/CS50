from typing import NoReturn
from string import ascii_uppercase as caps

def main() -> NoReturn:
    user_input: str = input("Please provide a camelCase variable: ").strip()
    result=""
    for character in user_input:
        if character in caps:
            result += "_"
        result += character

    print(f"{result.lower()}")



if __name__ == "__main__":
    main()
