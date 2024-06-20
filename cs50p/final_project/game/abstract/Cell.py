from typing import Any, Protocol


class HasValue(Protocol):
    def value(self) -> Any:
        """Can query the cell value"""

    def is_empty(self) -> bool:  # type: ignore
        """Cen query it's empty status"""
