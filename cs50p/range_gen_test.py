
from typing import Sequence
import argparse
import random


def main(argv: Sequence | None = None) -> int:
    parser = argparse.ArgumentParser("tries")
    parser.add_argument("-s", "--start", type=int)
    parser.add_argument("-e", "--end", type=int)
    parser.add_argument("-d", "--digits", type=int)
    args = parser.parse_args()
    random.seed(0)
    if args.digits:
        the_range = (10**args.digits,) if args.digits <= 1 else (10 **
                                                                 (args.digits - 1), (10**args.digits)-1)
    elif (args.start is not None) and (args.end is not None):
        the_range = (args.start, args.end)

    print(random.randint(*the_range),
          random.randint(*the_range))


if __name__ == "__main__":
    exit(main())
