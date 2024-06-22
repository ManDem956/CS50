from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Hashable


@dataclass
class ABCCell(ABC):
    value: Hashable = None

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError()
