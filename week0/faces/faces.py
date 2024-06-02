def convert(prompt: str) -> str:
    return prompt.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    user_input: str = input("What would you like to say? ")
    print(convert(user_input))
