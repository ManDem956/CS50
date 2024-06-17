import itertools
import random
from game import Board
from game.impl.Players import RandomPlayer


def printable_board(board: Board) -> tuple[tuple[str]]:
    res = tuple(zip(*[iter(board.cells_filler)] * board.size))
    for _ in range(board.dimensions - 2):
        res = tuple(zip(*[iter(res)] * board.size))
    return res


def main() -> None:
    #  4242 - x wins
    #  424242 - 0 wins
    random.seed(424242)
    board = Board()
    player_x = RandomPlayer("X", "'x'")
    player_o = RandomPlayer("O", "'o'")
    player_iter = itertools.cycle((player_x, player_o))
    counter = 1
    while not board.is_done():
        print(f"move {counter}:")
        board.make_move(
            random.choice(board.available_moves()), next(player_iter)
        )
        print(*printable_board(board), sep="\n")
        counter += 1


if __name__ == "__main__":
    main()
