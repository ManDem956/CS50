import random
from typing import Tuple

from game.abstract import ABCPlayer
from game.impl.Game import Game
from game.impl.Players import RandomPlayer


def create_players() -> Tuple[ABCPlayer, ABCPlayer]:
    return (RandomPlayer("X", "'x'"), RandomPlayer("O", "'o'"))


def setup_game(size, dimensions) -> Game:
    return Game(create_players(), size, dimensions, 0)


def main() -> None:
    #  4242 - x wins
    #  424242 - 0 wins
    random.seed(424242)
    size = 4
    dimensions = 3

    game = setup_game(size, dimensions)

    wins = game._win_conditions
    print(f"{len(wins)=}")
    print(wins, sep="\n")


if __name__ == "__main__":
    main()
