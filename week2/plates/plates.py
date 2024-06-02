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

    return is_valid_alpha(s[0:2]) and is_valid_digit(s)


def get_first_digit_index(s:str)->int:
    for idx, char in enumerate(s):
        if char.isdigit():
            return idx
    return -1

def is_valid_digit(s:str) -> bool:
    if (digit_index:=get_first_digit_index(s)) > 0:
        return all(char.isdigit() for char in s[digit_index:])
    return True

def is_valid_alpha(s:str) -> bool:
    return all(char.isalpha() for char in s)


if __name__ == "__main__":
    main()
