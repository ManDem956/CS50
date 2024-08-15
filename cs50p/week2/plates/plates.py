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

    for idx, char in enumerate(s):
        if not s.isalnum():
            return False
        if char.isdigit():
            if idx < 2 or char == '0':
                return False
            break
    else:
        return True

    left = s[idx:]

    try:
        int(left)
    except ValueError:
        return False

    return left.isalnum()


if __name__ == "__main__":
    main()
