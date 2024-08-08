class Jar:
    def __init__(self, capacity: int = 12) -> None:
        if capacity < 0:
            raise ValueError("Capacity can not be less than 0")
        self.__capacity: int = capacity
        self.__count: int = 0

    def __str__(self) -> str:
        return "🍪" * self.__count

    def deposit(self, n: int) -> None:
        if not self.__check_bounds(n):
            raise ValueError("Can not deposit {n} cookies, jar is full")

        self.__count += n

    def withdraw(self, n: int) -> None:
        if not self.__check_bounds(-1*n):
            raise ValueError("Can not withdraw {n} cookies, jar is empty")

        self.__count -= n

    def __check_bounds(self, n: int) -> bool:
        return (0 <= self.__count + n <= self.__capacity)

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def size(self) -> int:
        return self.__count
