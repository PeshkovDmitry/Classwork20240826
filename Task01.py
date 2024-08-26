"""
Задание №1
📌 Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании экземпляра.
📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""

from math import pi


class Circle:

    def __init__(self, radius: int):
        self.__radius = radius

    def get_length(self):
        return 2 * pi * self.__radius

    def get_square(self):
        return pi * self.__radius ** 2


c = Circle(1)
print(f"{c.get_length() = } {c.get_square() = }")