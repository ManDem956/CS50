import random
import sys


def main():
    lvl = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        cnt = 0
        while cnt < 3:
            try:
                z = int(input(f'{x} + {y} = '))
                if z != x + y:
                    cnt += 1
                    print('EEE')
                else:
                    score += 1
                    break
            except:
                print('EEE')
                cnt += 1
        if cnt == 3:
            print(f'{x} + {y} = {x + y}')
    sys.exit(f'Score: {score}')


def get_level():
    while True:
        try:
            a = int(input('Level: '))
            if 1 <= a <= 3:
                return a
            else:
                continue
        except:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
