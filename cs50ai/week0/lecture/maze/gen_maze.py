import argparse
import random


def fold(collection, size, joiner=""):
    result = list(zip(*(iter(collection),)*size))
    return "\n".join(joiner.join(row) for row in result)


def gen_maze(width: int, height: int) -> str:
    def get_neightbors(x: int, y: int) -> tuple[tuple[int, int], ...]:
        result = ((x+2, y), (x-2, y), (x, y+2), (x, y-2))
        return (item for item in result if item[0] in range(height) and item[1] in range(width))

    def count_walls(board, x: int, y: int):
        result = get_neightbors(x, y)
        return len(tuple(item for item in result if board[item[0]][item[1]] == '#'))

    board = [["#"]*width for _ in range(height)]
    current = (random.randrange(height), random.randrange(width))
    # current = (0, 0)
    board[current[0]][current[1]] = "A"
    visited = [current]
    stack = [current]

    while len(stack) > 0:
        current = stack.pop()
        neighbors = get_neightbors(*current)
        # available = tuple(filter(lambda x: count_walls(board, *x) > 1,
        #                          tuple(item for item in neighbors if item not in visited)))
        available = tuple(item for item in neighbors if item not in visited)

        if len(available) <= 0:
            continue

        stack.append(current)
        chosen = random.choice(available)
        current_x, current_y = current
        chosen_x, chosen_y = chosen
        board[chosen_x][chosen_y] = " "

        if chosen_x == current_x:
            for i in range(min(chosen_y, current_y)+1, max(chosen_y, current_y)):
                board[chosen_x][i] = " "

        if chosen_y == current_y:
            for i in range(min(chosen_x, current_x)+1, max(chosen_x, current_x)):
                board[i][chosen_y] = " "

        stack.append(chosen)
        visited.append(chosen)

    last_x, last_y = visited.pop()
    board[last_x][last_y] = "B"
    return "\n".join("".join(line) for line in board)


def main() -> None:
    parser = argparse.ArgumentParser(prog="gen_maze",
                                     description="generate a maze")
    parser.add_argument("-W", "--width", type=int, help="width of the maze", required=True)
    parser.add_argument("-H", "--height", type=int, help="height of the maze", required=False)
    parser.add_argument("-o", "--output", type=str, help="output fuke", required=False)

    args = parser.parse_args()
    if args.height is None:
        args.height = args.width

    if args.output is not None:
        with open(args.output, 'w') as f:
            print(gen_maze(args.width, args.height), file=f)
    else:
        print(gen_maze(args.width, args.height), file=f)


if __name__ == "__main__":
    main()
