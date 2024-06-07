
def lower_voice(in_str: str) -> str:
    return in_str.lower()


if __name__ == "__main__":
    user_input: str = input("What would you like to say? ")
    print(lower_voice(user_input))
