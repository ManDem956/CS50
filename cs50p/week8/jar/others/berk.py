import sys


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity can not be negative")

        self.jar_capacity = capacity
        self.jar_size = 0

    def deposit(self, n):
        absolute_n = (n**2)**(1/2)
        if self.size + absolute_n > self.capacity:
            raise ValueError("Given cookies exceeds jar's capacity")
        else:
            self.jar_size += absolute_n

    def withdraw(self, n):
        absolute_n = (n**2)**(1/2)
        if self.size - absolute_n < 0:
            raise ValueError("There is no enough cookies in jar")
        else:
            self.jar_size -= absolute_n

    @property
    def capacity(self):
        return self.jar_capacity

    @property
    def size(self):
        return self.jar_size

    def __str__(self):
        return self.size * "🍪"
