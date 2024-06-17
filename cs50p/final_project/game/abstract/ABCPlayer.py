from abc import ABC
from dataclasses import dataclass
from typing import Any, Tuple


@dataclass
class ABCPlayer(ABC):
    __name: str
    __token: Any

    def get_move(self, available_moves: Tuple[int]) -> int: ...

    @property
    def name(
        self,
    ) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def token(self) -> Any:
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token

    def __str__(self) -> str:
        return self.token
