import pytest

from engine.board import Board


class TestBoard:

    @pytest.fixture
    def board(self, request) -> Board:
        size = request.param["size"]
        dimensions = request.param["dimensions"]
        inception = request.param["inception"]
        win_combinations = request.param["win_combinations"]
        return Board(size, dimensions, inception, win_combinations)

    @pytest.mark.parametrize(
        "board, expected",
        [
            ({"size": 2, "dimensions": 2, "inception": 0, "win_combinations": {(3, 4, 5)}}, 2**2),
            ({"size": 2, "dimensions": 2, "inception": 1, "win_combinations": {(3, 4, 5)}}, 2**2),
            ({"size": 2, "dimensions": 2, "inception": 2, "win_combinations": {(3, 4, 5)}}, 2**2),
            ({"size": 3, "dimensions": 2, "inception": 0, "win_combinations": {(3, 4, 5)}}, 3**2),
            ({"size": 3, "dimensions": 2, "inception": 1, "win_combinations": {(3, 4, 5)}}, 3**2),
            ({"size": 3, "dimensions": 2, "inception": 2, "win_combinations": {(3, 4, 5)}}, 3**2),
            ({"size": 3, "dimensions": 3, "inception": 0, "win_combinations": {(3, 4, 5)}}, 3**3),
            ({"size": 3, "dimensions": 3, "inception": 1, "win_combinations": {(3, 4, 5)}}, 3**3),
            ({"size": 3, "dimensions": 3, "inception": 2, "win_combinations": {(3, 4, 5)}}, 3**3),
            ({"size": 4, "dimensions": 3, "inception": 0, "win_combinations": {(3, 4, 5)}}, 4**3),
            ({"size": 4, "dimensions": 3, "inception": 1, "win_combinations": {(3, 4, 5)}}, 4**3),
            ({"size": 4, "dimensions": 3, "inception": 2, "win_combinations": {(3, 4, 5)}}, 4**3),
        ],
        indirect=["board"],
    )
    def test_board_available_moves(self, board, expected):
        assert len(board.get_available_moves()) == expected
        pass

    @pytest.mark.parametrize(
        "board, expected",
        [
            ({"size": 2, "dimensions": 2, "inception": 0, "win_combinations": {(3, 4, 5)}}, True),
        ],
        indirect=["board"],
    )
    def test_board_is_empty(self, board, expected):
        assert board.is_empty() == expected
        pass
