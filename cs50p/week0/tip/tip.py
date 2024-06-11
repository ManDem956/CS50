PROMPT_PRICE = "How much was the meal?"
PROMPT_TIP_SIZE = "What percentage would you like to tip?"


def get_user_input(message: str, sep: str = ": ") -> str:
    res: str = input(f"{message}{sep}").strip()
    return res


def dollars_to_float(d: str) -> float:
    return float(d.lstrip("$"))


def percent_to_float(p: str) -> float:
    return float(p.rstrip("%")) / 100


def calculate(price: str, tip_size: str) -> str:
    return f"${dollars_to_float(price) * percent_to_float(tip_size):.2f}"


def main() -> None:
    print(
        f"Leave {calculate(get_user_input(PROMPT_PRICE),
                           get_user_input(PROMPT_TIP_SIZE))}"
    )


if __name__ == "__main__":
    main()
