from maze import Maze
import pytest


@pytest.fixture
def maze(request):
    result = Maze(request.param)
    return result


@pytest.mark.parametrize(
    "maze, start, end", [
        ("maze_0.txt", (3, 2), (0, 2)),
        ("small.txt", (1, 3), (3, 3)),
        ("maze_1.txt", (20, 39), (1, 0)),
        ("maze_2.txt", (19, 15), (11, 3)),
        ("maze_3.txt", (8, 17), (18, 15)),
    ], indirect=["maze"]
)
def test_maze_init(maze, start, end):
    assert maze.start == start
    assert maze.end == end
    assert maze.solution is None


@pytest.mark.parametrize(
    "maze, expected", [
        ("maze_0.txt", [[False, False, True, False],
                        [False, False, True, False],
                        [False, False, True, False],
                        [False, False, True, False],
                        ]),
        ("small.txt", [
            [False, False, False, False, False],
            [False, True, True, True, False],
            [False, True, False, False, False],
            [False, True, True, True, False],
            [False, False, False, False, False],
        ]),
    ], indirect=["maze"]
)
def test_maze_init_cells(maze, expected):
    assert maze.cells == expected


@pytest.mark.parametrize(
    "maze, input, expected", [
        ("maze_0.txt", (0, 2), [("down", (1, 2))]),
        ("maze_0.txt", (1, 2), [("up", (0, 2)), ("down", (2, 2))]),
        ("maze_0.txt", (2, 2), [("up", (1, 2)), ("down", (3, 2))]),
        ("maze_0.txt", (3, 2), [("up", (2, 2)), ]),
        ("small.txt", (1, 3), [("left", (1, 2)), ]),
        ("small.txt", (1, 2), [("left", (1, 1)), ("right", (1, 3)), ]),
        ("small.txt", (1, 1), [("right", (1, 2)), ("down", (2, 1)),]),
    ], indirect=["maze"]
)
def test_maze_neighbours(maze, input, expected):
    assert sorted(maze.neighbours(input)) == sorted(expected)
