from dataclasses import dataclass
from typing import Hashable

from engine.abstracts import CanBeEmpty


@dataclass
class Cell(CanBeEmpty):
    value: Hashable = None

    def is_empty(self) -> bool:
        return self.value is None
