import random


def main():
    random.seed(0)
    level = get_level()
    winrate = 0
    for _ in range(10):
        one, second = generate_integer(level)
        for _ in range(3):
            a = False
            answer = input(f"{one} + {second} = ").strip()
            if answer == str(one + second):
                winrate = winrate + 1
                a = True
                break
            else:
                print("EEE")
        if not a:
            print(f"{one}+{second}={one+second}")
    print("Score:", winrate)


def get_level():
    number = 0
    while number not in ("1", "2", "3"):
        number = input("Level: ")
    return int(number)


def generate_integer(level):
    if level not in (1, 2, 3):
        raise ValueError
    range = (10 ** (level),) if level == 1 else (10 ** (level - 1), 10 ** (level))
    one = random.randrange(*range)
    second = random.randrange(*range)
    return one, second


if __name__ == "__main__":
    main()
