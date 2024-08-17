CONST_USER_PROMPT = "Plate"


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> None:
    input = get_user_input(CONST_USER_PROMPT)
    if is_valid(input):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    length = len(s)
    if not 2 <= length <= 6:
        return False

    first_digit = length
    for idx, char in enumerate(s):
        if char.isdigit():
            if idx < 2:
                return False
            first_digit = min(idx, first_digit)
            if idx <= first_digit and char == '0':
                return False
        elif char.isalpha():
            if first_digit < idx:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    main()
