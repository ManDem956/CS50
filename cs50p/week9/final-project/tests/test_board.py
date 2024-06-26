import itertools
import random
import pytest

from engine.board import Board


class TestBoard:

    @pytest.fixture
    def board(self, request) -> Board:
        size = request.param["size"]
        dimensions = request.param["dimensions"]
        inception = request.param["inception"]
        win_combinations = request.param["wins"]
        return Board(size, dimensions, inception, win_combinations)

    @pytest.mark.parametrize(
        "board, expected",
        [
            ({"size": 2, "dimensions": 2, "inception": 0, "wins": {(0, 2)}}, 2**2),
            ({"size": 2, "dimensions": 2, "inception": 1, "wins": {(0, 2)}}, 2**2),
            ({"size": 2, "dimensions": 2, "inception": 2, "wins": {(0, 2)}}, 2**2),
            ({"size": 3, "dimensions": 2, "inception": 0, "wins": {(0, 4, 8)}}, 3**2),
            ({"size": 3, "dimensions": 2, "inception": 1, "wins": {(0, 4, 8)}}, 3**2),
            ({"size": 3, "dimensions": 2, "inception": 2, "wins": {(0, 4, 8)}}, 3**2),
            ({"size": 3, "dimensions": 3, "inception": 0, "wins": {(0, 13, 26)}}, 3**3),
            ({"size": 3, "dimensions": 3, "inception": 1, "wins": {(0, 13, 26)}}, 3**3),
            ({"size": 3, "dimensions": 3, "inception": 2, "wins": {(0, 13, 26)}}, 3**3),
            ({"size": 4, "dimensions": 3, "inception": 0, "wins": {(0, 5, 10, 15)}}, 4**3),
            ({"size": 4, "dimensions": 3, "inception": 1, "wins": {(0, 5, 10, 15)}}, 4**3),
            ({"size": 4, "dimensions": 3, "inception": 2, "wins": {(0, 5, 10, 15)}}, 4**3),
        ],
        indirect=["board"],
    )
    def test_board_available_moves(self, board, expected):
        assert len(board.get_available_moves()) == expected
        assert board.value is None

    @pytest.mark.parametrize(
        "board, expected",
        [
            ({"size": 2, "dimensions": 2, "inception": 0, "wins": {(0, 2)}}, True),
            ({"size": 3, "dimensions": 2, "inception": 0, "wins": {(0, 4, 8)}}, True),
            ({"size": 3, "dimensions": 3, "inception": 0, "wins": {(0, 13, 26)}}, True),
            ({"size": 4, "dimensions": 3, "inception": 0, "wins": {(0, 5, 10, 15)}}, True),
        ],
        indirect=["board"],
    )
    def test_board_is_empty(self, board, expected):
        assert board.is_empty() == expected

    @pytest.mark.parametrize(
        "board, moves, expected",
        [
            (
                {"size": 2, "dimensions": 2, "inception": 0, "wins": {(0, 2)}},
                ([0], [2]),
                False,
            ),
            (
                {"size": 2, "dimensions": 2, "inception": 0, "wins": {(0, 2)}},
                ([0], [1]),
                True,
            ),
        ],
        indirect=["board"],
    )
    def test_board_make_move(self, board, moves, expected):
        for move in moves:
            board.place_move(move, 1)
        assert board.is_empty() == expected
        if not expected:
            assert board.value == 1

    @pytest.mark.parametrize(
        "board, seed, expected",
        [
            (
                {
                    "size": 3,
                    "dimensions": 2,
                    "inception": 0,
                    "wins": {
                        (0, 1, 2),
                        (3, 4, 5),
                        (6, 7, 8),
                        (0, 3, 6),
                        (1, 4, 7),
                        (2, 5, 8),
                        (0, 4, 8),
                        (2, 4, 6)
                    },
                },
                4242,
                0,
            ),
            (
                {
                    "size": 3,
                    "dimensions": 2,
                    "inception": 0,
                    "wins": {
                        (0, 1, 2),
                        (3, 4, 5),
                        (6, 7, 8),
                        (0, 3, 6),
                        (1, 4, 7),
                        (2, 5, 8),
                        (0, 4, 8),
                        (2, 4, 6)
                    },
                },
                424242,
                1,
            ),
        ],
        indirect=["board"],
    )
    def test_board_make_move_players(self, board, random_players, seed, expected):
        random.seed(seed)
        players_cycle = itertools.cycle(random_players)
        while not board.value:
            current_player = next(players_cycle)
            board.place_move(
                current_player.calculate_move(board.get_available_moves()), current_player
            )

        assert board.value == random_players[expected]
