CONST_USER_PROMPT = "Item"
CONST_MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> None:
    total = 0
    while True:
        try:
            input = get_user_input(CONST_USER_PROMPT)
            if (price := CONST_MENU.get(input.title())) is not None:
                total += price
                print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            break


if __name__ == "__main__":
    main()
