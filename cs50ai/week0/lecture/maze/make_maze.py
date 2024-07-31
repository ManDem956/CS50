from random import shuffle, randrange




def make_maze(w=16, h=8):
    vis = []
    board = [["#"] * w for _ in range(h)]

    def get_neightbors(x: int, y: int) -> tuple[tuple[int, int], ...]:
        result = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        return (item for item in result if item[0] in range(w) and item[1] in range(h))

    def walk(x, y):
        vis.append((x, y))

        d = list(get_neightbors(x, y))
        shuffle(d)
        for (xx, yy) in d:
            if (xx, yy) in vis:
                continue
            board[yy][xx] = " "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    return "\n".join("".join(line) for line in board)


if __name__ == '__main__':
    print(make_maze())
