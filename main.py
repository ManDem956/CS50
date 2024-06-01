from typing import NoReturn

def power(value: int) -> int:
    return value ** 2

def main() -> NoReturn:
    x = int(input("Please povide a value for x: "))
    print(f"the square of x is {power(x)}")

if __name__ == "__main__":
    main()
