from datetime import datetime
from datetime import date
import inflect


class Birthday:
    date_pattern = "%Y-%m-%d"

    def __init__(self, birthday):
        self.birthday = birthday
        self._date_now = date.today()

    def __str__(self):
        p = inflect.engine()
        delta = self._date_now - self._birthday
        return f"{p.number_to_words(delta.days * 24 * 60).capitalize()} minutes"

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, user_input):
        try:
            self._birthday = datetime.strptime(user_input, self.date_pattern).date()
            print(self.birthday)
        except ValueError:
            raise ValueError("Invalid date format")
            # sys.exit()


def main():
    bday = input("Birthday: ")
    birthday = Birthday(bday)
    print(birthday)


if __name__ == "__main__":
    main()
