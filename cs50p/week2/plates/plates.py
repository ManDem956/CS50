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
    if not 2 <= len(s) <= 6:
        return False

    d_idx = get_first_digit_index(s)

    if d_idx > 0:
        if d_idx < 2:
            return False

        if s[d_idx] == "0":
            return False

        if not is_valid_digit(s[d_idx:]):
            return False

        return is_valid_alpha(s[:d_idx])

    return is_valid_alpha(s)


def get_first_digit_index(s: str) -> int:
    for idx, char in enumerate(s):
        if char.isdigit():
            return idx
    return -1


def is_valid_digit(s: str) -> bool:

    return all(char.isdigit() for char in s)


def is_valid_alpha(s: str) -> bool:
    return all(char.isalpha() for char in s)


if __name__ == "__main__":
    main()
