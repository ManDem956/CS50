import csv
import random
from typing import Iterable
import pathlib


BASE = 4000
path = f"{pathlib.Path(__file__).parent.resolve()}/data"


def gen_data(size: int, seed: int) -> None:
    print()
    random.seed(seed)
    random_data = random.sample(range(size), size)

    write_file(size, ((item,) for item in random_data), "random")
    write_file(size, ((item,) for item in range(size)), "sorted")
    write_file(size, ((item,) for item in range(size - 1, -1, -1)), "reversed")


def write_file(size: int, the_list: Iterable, name) -> None:
    filename =f"{path}/{name}-{size:>06}.txt" 
    print(f"Writing {filename}")
    with open(filename, "w") as csvfile:
        sortwriter = csv.writer(
            csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )

        sortwriter.writerows(the_list)


def main() -> None:

    for i in range(7):
        gen_data((2 ** i) * BASE, 1234)


if __name__ == "__main__":
    main()
