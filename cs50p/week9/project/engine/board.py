from typing import Any

from engine.abstracts import Valuable


class Board(Valuable):
    @property
    def value(self) -> Any:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError
