from typing import NoReturn
from string import ascii_uppercase as caps

def main() -> NoReturn:
    user_input: str = input("Please provide a camelCase variable: ").strip()
    indices = []
    for idx, character in enumerate(user_input):
        if character in caps:
            indices.append(idx)
    print(f"{indices=}")



if __name__ == "__main__":
    main()
