import datetime
import sys
from typing import NoReturn
import inflect


class TimeCalculator:

    def __init__(self, birthdate: str) -> None:
        self.birthdate = datetime.date.fromisoformat(birthdate)

    def humanize(self) -> str:
        p = inflect.engine()
        return f"{p.number_to_words(self._calculate(), andword="")} minutes".capitalize()
        

    def _calculate(self) -> int:
        delta: datetime.timedelta = datetime.date.today() - self.birthdate
        minutes = delta.days * 24 * 60
        return minutes


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    p = inflect.engine()
    try:
        calc = TimeCalculator(get_user_input("Birthday 🍪"))
        minutes = calc.humanize()
    except ValueError:
        print("invalid birthdate value {birthdate}")
        sys.exit(1)
    else:
        print(f"{minutes}")


if __name__ == "__main__":
    main()
