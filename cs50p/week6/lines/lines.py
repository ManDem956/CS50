import sys
import re

import argparse
from pathlib import Path


def is_empty(line: str):
    res = len(line.strip()) <= 0
    return res


def is_comment(line: str):
    res = line.strip()[0] == "#"
    return res


def count(filename: str) -> int:
    is_doc = False
    lines_count = 0
    with open(filename) as file:
        # lines_count = sum(0 if is_empty(line) else 1 for line in file)
        for line in file:
            count_docs = 0
            if is_empty(line):
                continue

            if is_comment(line) and not is_doc:
                continue

            count_docs = len(re.findall('"""|\'\'\'', line))
            if count_docs > 0:
                if count_docs % 2 == 1:
                    is_doc = not is_doc
                else:
                    lines_count += 1
                    continue

            lines_count += 1

    return lines_count


def validate(filename: str) -> None:
    file = Path(filename)
    if not file.is_file():
        raise FileNotFoundError(f"{filename} could not be found")

    if file.suffix != ".py":
        raise ValueError(f"{filename} is not a python file")

    if file.stat().st_size <= 0:
        raise ValueError(f"{filename} is empty")


def main() -> None:
    # initialise an argparser object with one
    # positional argument to receive a file name from user
    parser = argparse.ArgumentParser(prog="Lines",
                                     description="Count lines in a file")
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
