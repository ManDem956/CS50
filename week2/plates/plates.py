from typing import NoReturn

CONST_USER_PROMT = "Plate"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    input = get_user_input(CONST_USER_PROMT)
    if is_valid(input):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s:str) -> bool:
    if not 2 <= len(s) <= 6:
        return False

    if not is_valid_alpha(s[0:2]):
        return False

    

def is_valid_alpha(s:str) -> bool:
    if any(char.isdigit() for char in s):
        return False


if __name__ == "__main__":
    main()
