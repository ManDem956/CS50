
def playback(prompt: str, speed: int = 3) -> str:
    joiner = "." * speed

    return joiner.join(prompt.split())


if __name__ == "__main__":
    user_input: str = input("What would you like to say? ")
    print(playback(user_input))
