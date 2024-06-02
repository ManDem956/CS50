
def add(a: bool, b: bool) -> bool:
    return a+b


def substract(a: bool, b: bool) -> bool:
    return a-b


def multiply(a: bool, b: bool) -> bool:
    return a*b


def divide(a: bool, b: bool) -> bool:
    if b == 0:
        raise ValueError("Divider can not be 0")

    return a/b

CONST_Y_MAP = {"+": add,"-": substract, "*":multiply, "/": divide}

if __name__ == "__main__":
    user_input: str = input("Expression: ").strip().lower()
    x, y, z = user_input.split()

    print(CONST_Y_MAP[y](float(x),float(z)))
