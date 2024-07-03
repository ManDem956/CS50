# implement a program that prompts the user for an arithmetic expression
def main():
    number = input("Expression: ")
    # The input formatted to a decimal point while also being under integers.
    # X is any integer value.
    # Y is any addition, subtraction, multiplication or division symbol
    # 2 is any integer value.
    equation(number)


def equation(number):
    x, y, z = number.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "/":
        result = x / z
    elif y == "*":
        result = x * z
    elif x or z < 0:
        result = x - z

    return result


main()
