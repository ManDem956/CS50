import argparse
from collections.abc import Sequence

from sock import MySocket


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python "+__file__, description="pyhton implemnetation of mkdir"
    )
    parser.add_argument("-d", "--data",  type=str, help="data to send", required=True)
    args = parser.parse_args(argv)
    sender = MySocket()
    sender.connect("localhost", 8000)
    sender.do_send(bytes(args.data, "ascii"))
    return 0


if __name__ == "__main__":
    exit(main())
