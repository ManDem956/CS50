import sys
from typing import NoReturn
import argparse
from pathlib import Path


def is_empty(line: str):
    res = len(line.strip()) <= 0 or (line.strip()[0] == "#")
    return res


def count(filename: str) -> int:
    with open(filename) as file:
        lines_count = sum(0 if is_empty(line) else 1 for line in file)
    return lines_count


def validate(filename: str) -> NoReturn:
    file = Path(filename)
    if not file.is_file():
        raise FileNotFoundError(filename)

    if file.suffix != ".py":
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
        print(count(args.filename))


if __name__ == "__main__":
    main()
