import argparse
import os


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="python make_dirs.py", description="pyhton implemnetation of mkdir"
    )
    parser.add_argument("path", help="directory structure to create")
    parser.add_argument(
        "-p",
        "--parents",
        action="store_true",
        help="create full path, like `mkdir -p`. Default value: False",
    )
    parser.add_argument(
        "-e",
        "--exists_ok",
        action="store_true",
        help="Suppress error if directory exists. Default value: False",
    )
    args = parser.parse_args()

    try:
        if args.parents:
            print(f"Using `os.makedirs()` with {args.exists_ok=}")
            os.makedirs(args.path, exist_ok=args.exists_ok)
        else:
            print("Using `os.mkdir()`")
            os.mkdir(args.path)
    except OSError as e:
        print(str(e))


if __name__ == "__main__":
    main()
