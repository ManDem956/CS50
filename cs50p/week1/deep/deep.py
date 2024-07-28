CONST_ANSWERS = ["42", "forty two", "forty-two"]


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def check_answer(answer: str, options: list[str]):
    result = "Yes" if answer.lower() in options else "No"
    return result


def main():
    user_input: str = get_user_input(
        "What is the Answer to the Great Question of Life, "
        + "the Universe and Everything: "
    ).strip()
    print(check_answer(user_input, CONST_ANSWERS))


if __name__ == "__main__":
    exit(main())
