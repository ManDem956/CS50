from typing import NoReturn

CONST_USER_PROMT = "Fraction"

def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT).lower()
    if input in CONST_FRUIT_MAPPING:
        print(f"Calories: {CONST_FRUIT_MAPPING.get(input.lower(),"")}")


if __name__ == "__main__":
    main()
