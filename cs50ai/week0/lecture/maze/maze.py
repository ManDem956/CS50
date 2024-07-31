
from abc import ABC, abstractmethod
import argparse
from typing import Any, Protocol, Sequence


class BaseNode(Protocol):
    state: tuple[int, int]
    parent: Any
    position: str | None


class Node(BaseNode):
    def __init__(self, state: tuple[int, int], parent: BaseNode | None, position: str | None = None) -> None:
        self.state = state
        self.parent = parent
        self.position = position


class Frontier(ABC):
    def __init__(self) -> None:
        self.items: list[Node] = []

    def add(self, node: Node):
        self.items.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.items)

    def is_empty(self):
        return len(self.items) == 0

    @abstractmethod
    def remove(self) -> Node:
        ...


class DFSFrontier(Frontier):
    def remove(self) -> Node:
        return self.items.pop()


class BFSFrontier(Frontier):
    def remove(self) -> Node:
        return self.items.pop(0)


class Maze():
    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        rows = contents.splitlines()
        self.height = len(rows)
        self.width = max(len(row) for row in rows)

        self.cells = []
        for idx_row, row in enumerate(rows):
            cell_row = []
            for idx_cell, cell in enumerate(row):
                try:
                    if cell == 'A':
                        self.start = (idx_row, idx_cell)
                        cell_row.append(True)
                    elif cell == 'B':
                        self.end = (idx_row, idx_cell)
                        cell_row.append(True)
                    elif cell == ' ':
                        cell_row.append(True)
                    else:
                        cell_row.append(False)
                except IndexError:
                    cell_row.append(False)
            self.cells.append(cell_row)

        self.solution = []

    def neighbours(self, coords):
        row, col = coords
        candidates = [
            ("up", (row-1, col)),
            ("down", (row+1, col)),
            ("left", (row, col-1)),
            ("right", (row, col+1)),
        ]
        result = [(action, (row, col))
                  for action, (row, col) in candidates
                  if row in range(self.height)
                  and col in range(self.width)
                  and self.cells[row][col]]
        return result

    def print(self):
        print()
        for idx_row, row in enumerate(self.cells):
            for idx_col, col in enumerate(row):
                if not col:
                    print("█", end="")
                elif (idx_row, idx_col) == self.start:
                    print("A", end="")
                elif (idx_row, idx_col) == self.end:
                    print("B", end="")
                elif self.solution is not None and (idx_row, idx_col) in self.solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def solve(self):
        self.steps_counter = 0
        start = Node(self.start, None, None)
        tracker = DFSFrontier()
        tracker.add(start)

        self.visited = set()

        while True:
            if tracker.is_empty():
                raise Exception("Can not solve maze")

            current = tracker.remove()
            self.steps_counter += 1

            if current.state == self.end:
                while current.parent is not None:
                    self.solution.append(current.state)
                    current = current.parent
                self.solution.reverse()
                return

            self.visited.add(current.state)

            for action, state in self.neighbours(current.state):
                if not tracker.contains_state(state) and state not in self.visited:
                    child = Node(state, current, action)
                    tracker.add(child)


def main(argv: Sequence | None = None) -> int:
    parser = argparse.ArgumentParser(prog="gen_maze",
                                     description="generate a maze")
    parser.add_argument("filename", help="file containing maze definition")

    args = parser.parse_args(argv)
    maze = Maze(args.filename)
    maze.solve()
    maze.print()
    return 0


if __name__ == "__main__":
    exit(main())
