class Jar:
    def __init__(self, capacity: int = 12) -> None:
        if capacity < 0:
            raise ValueError("Capacity can not be less than 0")
        self.__capacity: int = capacity
        self.__count: int = 0

    def __str__(self) -> str:
        return "🍪" * self.__count

    def deposit(self, n: int) -> None:
        if not (0 <= self.__count + n <= self.__capacity):
            raise ValueError("Can not deposit {n} cookies, jar is full")

        self.__count += n

    def withdraw(self, n: int) -> None:
        if not (0 <= self.__count - n <= self.__capacity):
            raise ValueError("Can not withdraw {n} cookies, jar is empty")

        self.__count -= n

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def size(self) -> int:
        return self.__count
