import itertools
import random

from game.impl.Board import Board
from game.impl.Game import Game
from game.impl.Players import RandomPlayer


def printable_board(size: int, dimensions: int, board: Board) -> tuple[tuple[str]]:
    print(board.cells)
    a = board.cells
    cells = tuple(item or str(idx) for idx, item in enumerate(a))
    res = tuple(zip(*[iter(cells)] * size))
    for _ in range(dimensions - 2):
        res = tuple(zip(*[iter(res)] * size))
    return res


def main() -> None:
    #  4242 - x wins
    #  424242 - 0 wins
    random.seed(424242)
    size = 3
    dimensions = 2

    board = Board(size**dimensions, 0)
    player_x = RandomPlayer("X", "'x'")
    player_o = RandomPlayer("O", "'o'")
    player_iter = itertools.cycle((player_x, player_o))
    counter = 1
    while not board.is_done():
        cell_idx = random.choice(board.available_moves())
        print(f"move {counter}: {cell_idx=}")
        board.make_move(cell_idx, next(player_iter))
        # board.make_move(cell_idx, next(player_iter))
        print(*printable_board(size, dimensions, board), sep="\n")
        counter += 1

    game = Game((RandomPlayer("X", "'x'"), RandomPlayer("O", "'o'")), 3, 2, 0)

    wins = game._win_conditions
    print(f"{len(wins)=}")
    print(wins, sep="\n")


if __name__ == "__main__":
    main()
