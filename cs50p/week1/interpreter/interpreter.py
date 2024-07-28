def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divider can not be 0")

    return a / b


CONST_Y_MAP = {"+": add, "-": subtract, "*": multiply, "/": divide}


def interpret(expr: str) -> float:
    for key in CONST_Y_MAP:
        x, y, z = expr.partition(key)
        if y != '':
            return CONST_Y_MAP[y](float(x.strip()), float(z.strip()))
    else:
        raise ValueError("Unknown operation")


if __name__ == "__main__":
    user_input: str = input("Expression: ").strip().lower()

    print(interpret(user_input))
