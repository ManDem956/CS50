import sys

import argparse
from pathlib import Path
import csv
from typing import NoReturn

OUT_HEADERS = ("first", "last", "house")


def convert(in_file_name: str, out_file_name: str) -> None:
    with open(in_file_name) as in_file, open(out_file_name, "w") as out_file:
        reader = csv.DictReader(in_file)
        # next(reader, None)
        writer = csv.DictWriter(out_file, fieldnames=OUT_HEADERS)        
        writer.writeheader()
        # writer.writerow(OUT_HEADERS)
        for row in reader:
            last_name, first_name = (cell.strip() for cell in row['name'].split(","))
            new_row = dict(zip(OUT_HEADERS, (first_name, last_name, row['house'])))
            writer.writerow(new_row)


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
