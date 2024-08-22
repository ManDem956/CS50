import csv
import sys

import argparse
from pathlib import Path
from tabulate import tabulate


def build_grid(filename: str) -> str:
    with open(filename) as file:
        reader = csv.reader(file)
        # tabulate can just accept reader, no need to buffer in the form of a python collection
        return tabulate(reader, tablefmt="grid", headers="firstrow")


def validate(filename: str) -> None:
    """Validate the file. file.stat() will throw the FileNotFoundError"""
    file = Path(filename)

    try:
        if file.stat().st_size <= 0:
            raise ValueError(f"{file.absolute()} is an empty file.")
    except FileNotFoundError as e:
        # replae file name with absolute path
        msg = str(e).replace(filename, str(file.absolute()))
        raise FileNotFoundError(msg)

    if file.suffix != ".csv":
        raise ValueError(f"{file.absolute()} is not a csv file.")


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
