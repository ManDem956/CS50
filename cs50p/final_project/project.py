from game import Board


def main() -> None:
    board = Board(inception=1)
    print(board)
    print(board.available_moves())
    print(board.cells[0])
    print(board.cells[0].available_moves())
    print(board.cells[0].cells[0])
    print(board.cells[0].cells[0].value)


if __name__ == "__main__":
    main()
