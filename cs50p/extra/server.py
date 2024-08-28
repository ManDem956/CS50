from typing import Sequence

from sock import MySocket


def main(argv: Sequence | None = None) -> int:
    server = MySocket()
    server.listen("localhost", 8000)
    while True:
        try:
            print(server.do_receive())
        except EOFError:
            server.sock.close()
            break


if __name__ == "__main__":
    exit(main())
