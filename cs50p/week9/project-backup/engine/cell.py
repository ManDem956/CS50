from dataclasses import dataclass
from engine.abstracts import Movable, Valuable


@dataclass
class Cell(Valuable):
    value: Movable | None = None

    @property
    def is_empty(self) -> bool:
        return self.value is None
