import csv
import sys

import argparse
from pathlib import Path
from typing import NoReturn
from tabulate import tabulate


def build_grid(filename: str) -> int:
    with open(filename) as file:
        reader = csv.reader(file)
        return tabulate(reader, tablefmt="grid", headers="firstrow")


def validate(filename: str) -> NoReturn:
    file = Path(filename)
    if not file.is_file():
        raise FileNotFoundError(f"File not found {file.absolute()}")

    if file.suffix != ".csv":
        raise ValueError(f"{file.absolute()} is not a csv file")

    if file.stat().st_size <= 0:
        raise ValueError(f"{file.absolute()} is empty")


def main() -> None:
    # initialise an argparser object with one positional
    # argument to receive a file name from user
    parser = argparse.ArgumentParser(prog="Lines",
                                     description="Count lines in a file")
    parser.add_argument("filename")
    try:
        args = parser.parse_args()
        validate(args.filename)
        print(build_grid(args.filename))
    except (ValueError, FileNotFoundError) as e:
        sys.exit(str(e))


if __name__ == "__main__":
    main()
