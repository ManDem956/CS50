import sys

import argparse
from pathlib import Path
from tabulate import tabulate


def build_grid(filename: str) -> int:
    rows = []
    with open(filename) as file:
        for line in file:
            rows.append(cell.strip() for cell in line.split(","))
    return tabulate(rows, tablefmt="grid", headers="firstrow")


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
    parser.add_argument("filename")
    try:
        args = parser.parse_args()
        validate(args.filename)
    except SystemExit:
        sys.exit(1)
    else:
        print(build_grid(args.filename))


if __name__ == "__main__":
    main()
