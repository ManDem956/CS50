if __name__ == "__main__":
    user_input: str = input("Greeting: ").strip().lower()
    fee = 100
    if user_input.startswith('hello'):
        fee = 0
    elif user_input.startswith('h'):
        fee = 20

    print(f"${fee}")
