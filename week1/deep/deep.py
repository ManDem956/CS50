CONST_ANSWERS = ["42", "forty two", "forty-two"]

if __name__ == "__main__":
    user_input: str = input(
        "What is the Answer to the Great Question of Life, "
        + "the Universe and Everything: "
    ).strip()
    print("Yes") if user_input.lower() in CONST_ANSWERS else print("No")
