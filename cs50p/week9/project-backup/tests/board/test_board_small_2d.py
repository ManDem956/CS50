import random
import pytest
from contextlib import nullcontext as does_not_raise


class TestBoardSmall2d:

    @pytest.fixture(autouse=True)
    def seed(self):
        random.seed(4242)

    @pytest.mark.parametrize(
        "board",
        [
            {"size": 2, "dimensions": 2, "inception": 0},
        ],
        indirect=["board"],
    )
    def test_board_default(self, board):
        assert board.available_moves == tuple(range(4))

    @pytest.mark.parametrize(
        "board, moves, expected, expectation",
        [
            (
                {"size": 2, "dimensions": 2, "inception": 0},
                (1, 2),
                tuple(move for move in range(4) if move not in (1, 2)),
                does_not_raise(),
            ),
            (
                {"size": 2, "dimensions": 2, "inception": 0},
                (0, 1, 2, 3),
                tuple(move for move in range(4) if move not in (0, 1, 2, 3)),
                does_not_raise(),
            ),
            (
                {"size": 2, "dimensions": 2, "inception": 0},
                (1, 2, 2),
                None,
                pytest.raises(ValueError),
            ),
        ],
        indirect=["board"],
    )
    def test_board_default_moves(self, players, board, moves, expected, expectation):
        with expectation:
            for move in moves:
                board.make_move(move, next(players))
            assert board.available_moves == expected

    @pytest.mark.parametrize(
        "board, expected",
        [
            (
                {"size": 2, "dimensions": 2, "inception": 0},
                tuple(move for move in range(4) if move not in (1, 2)),
            ),
        ],
        indirect=["board"],
    )
    def test_board_default_random_moves(self, random_players, board, expected):
        next_player = next(random_players)
        next_move = next_player.choose_move(board.available_moves)
        board.make_move(next_move, next_player)
        # assert board.available_moves == expected

    @pytest.mark.parametrize(
        "board, expected",
        [
            (
                {"size": 2, "dimensions": 2, "inception": 1},
                tuple(tuple(range(2 * 2)) for idx in range(2**2)),
            ),
        ],
        indirect=["board"],
    )
    def test_board_inception1(self, board, expected):
        actual = board.available_moves
        assert len(actual) == len(expected)
        assert actual == expected

    @pytest.mark.parametrize(
        "board, expected",
        [
            (
                {"size": 2, "dimensions": 2, "inception": 1},
                tuple(move for move in range(4) if move not in (1, 2)),
            ),
            (
                {"size": 2, "dimensions": 2, "inception": 2},
                tuple(move for move in range(4) if move not in (1, 2)),
            ),
        ],
        indirect=["board"],
    )
    def test_board_inception1_moves(self, random_players, board, expected):
        current_player = next(random_players)
        player_move = current_player.choose_move(board.available_moves)
        board.make_move(player_move, current_player)
        assert board.available_moves == expected
