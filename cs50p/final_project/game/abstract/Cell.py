from typing import Any, Protocol


class HasValue(Protocol):
    def value(self) -> Any:
        """Can query the cell value"""

    def is_empty(self) -> bool:
        """Cen query it's empty status"""
