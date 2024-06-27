from random import randrange
import random


def main():
    l = get_level()
    score = 0
    i = 0
    while i < 10:
        i += 1
        x, y = generate_integer(l)
        sum = x + y

        z = 0
        while z < 3:
            print(f"{x} + {y} =", end=" ")
            try:
                answer = int(input())
                if answer == sum:
                    score += 1
                    z = 0
                    break
                
                else:
                    raise ValueError
            except ValueError:
                if 0 <= z < 2:
                    z += 1
                    print("EEE")
                else:
                    print(f"{x} + {y} =", sum)
                    z = 0
                    break
    print("Score:", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 0 < level < 4:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = randrange(0, 10)
        y = randrange(0, 10)
    elif level == 2:
        x = randrange(10, 100)
        y = randrange(10, 100)
    elif level == 3:
        x = randrange(100, 1000)
        y = randrange(100, 1000)
    return x, y

if __name__ == "__main__":
    random.seed(0)
    main()
