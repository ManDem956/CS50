import sys

import argparse
from pathlib import Path
import csv

OUT_HEADERS = ("first", "last", "house")


def convert(in_file_name: str, out_file_name: str) -> NoReturn:
    with open(in_file_name) as in_file, open(out_file_name, "w") as out_file:
        reader = csv.reader(in_file)
        next(reader, None)
        writer = csv.writer(out_file)
        writer.writerow(OUT_HEADERS)
        for name, house in reader:
            last_name, first_name = (cell.strip() for cell in name.split(","))
            writer.writerow((first_name, last_name, house))


def validate(filename: str) -> NoReturn:
    file = Path(filename)
    if not file.is_file():
        raise FileNotFoundError(filename)

    if file.suffix != ".csv":
        raise ValueError(f"{filename} is not a python file")

    if file.stat().st_size <= 0:
        raise ValueError(f"{filename} is empty")


def main() -> None:
    # initialise an argparser object with one positional argument to receive a file name from user
    parser = argparse.ArgumentParser(prog="Lines", description="Count lines in a file")
    parser.add_argument("infile")
    parser.add_argument("outfile")

    try:
        args = parser.parse_args()
        validate(args.infile)
    except SystemExit:
        sys.exit(1)
    else:
        convert(args.infile, args.outfile)


if __name__ == "__main__":
    main()
