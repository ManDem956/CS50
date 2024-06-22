from engine.cell import ABCCell


class Cell(ABCCell):
    def is_empty(self) -> bool:
        return self.value is None
