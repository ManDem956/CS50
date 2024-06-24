from engine.game import Game


def main() -> None:
    board_size = 4
    board_dimensions = 3
    check_sum = ((board_size + 2) ** board_dimensions - board_size**board_dimensions) // 2

    result = Game.generate_win_combinations(board_size, board_dimensions)
    print(sorted(result), sep="\n")
    print(f"{check_sum == len(result)}, {check_sum=}, {len(result)=}")


if __name__ == "__main__":
    main()
