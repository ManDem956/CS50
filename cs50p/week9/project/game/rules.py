from game.abstracts import Movable, Valuable


class ClassicRules(Movable):
    def get_available_moves(self) -> tuple[int]:
        raise NotImplementedError

    def check_winner(self) -> Valuable | None:
        raise NotImplementedError

