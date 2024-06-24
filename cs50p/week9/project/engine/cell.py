from dataclasses import dataclass
from typing import Any

from engine.abstracts import Valuable


@dataclass
class Cell(Valuable):
    value: Any = None

    def is_empty(self) -> bool:
        return self.value is None
