import sys

import argparse
from pathlib import Path
import csv
from typing import NoReturn

OUT_HEADERS = ("first", "last", "house")


def convert(in_file: str, out_file: str) -> None:
    try:
        with open(in_file, 'r') as input_file:
            reader = csv.reader(input_file)
            header = next(reader)
            with open(out_file, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header)
                for row in reader:
                    name, house = row
                    last, first = name. split(', ')
                    header = first, last, house
                    print(header)
                    writer.writerow([first, last, house])
    except FileNotFoundError:
        sys.exit(f"Could not read {in_file}")


def validate(filename: str) -> NoReturn:
    file = Path(filename)
    if not file.is_file():
        raise FileNotFoundError(filename)

    if file.suffix != ".csv":
        raise ValueError(f"{filename} is not a python file")

    if file.stat().st_size <= 0:
        raise ValueError(f"{filename} is empty")


def main() -> None:
    # initialise an argparser object with one positional argument to receive
    # a file name from user
    parser = argparse.ArgumentParser(prog="Lines",
                                     description="Count lines in a file")
    parser.add_argument("in_file")
    parser.add_argument("out_file")

    try:
        args = parser.parse_args()
        validate(args.in_file)
    except SystemExit:
        sys.exit(1)
    else:
        convert(args.in_file, args.out_file)


if __name__ == "__main__":
    main()
