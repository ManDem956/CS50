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

    if d_idx in (0, 1):
        return False

    if d_idx > 1:
        if s[d_idx] == "0":
            return False

        try:
            int(s[d_idx:])
        except ValueError:
            return False

        return s[:d_idx].isalpha()

    return s.isalpha()


def get_first_digit_index(s: str) -> int:
    for idx, char in enumerate(s):
        if char.isdigit():
            return idx
    return -1


if __name__ == "__main__":
    main()
