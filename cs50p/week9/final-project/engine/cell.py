from dataclasses import dataclass
from typing import Any


@dataclass
class Cell:
    value: Any = None

    def is_empty(self) -> bool:
        return self.value is None
