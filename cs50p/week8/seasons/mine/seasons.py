from datetime import date, timedelta
import sys

import inflect


class TimeCalculator:

    def __init__(self, birthdate: str) -> None:
        self.birthdate = date.fromisoformat(birthdate)

    def __str__(self) -> str:
        return self.humanize()

    def humanize(self) -> str:
        p = inflect.engine()
        return f"{p.number_to_words(self._calculate(),
                                    andword="")} minutes".capitalize()

    def _calculate(self) -> int:
        delta: timedelta = date.today() - self.birthdate
        minutes = delta.days * 24 * 60
        return minutes


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> None:
    try:
        calc = TimeCalculator(get_user_input("Birthday 🍪"))
        minutes = calc.humanize()
    except ValueError:
        sys.exit("invalid birthdate value {birthdate}")
    else:
        print(f"{minutes}")


if __name__ == "__main__":
    main()
