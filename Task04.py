"""
Задание №4
📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""


class Person:

    def __init__(self, name: str, age: int, phone: str):
        self.__name = name
        self.__age = age
        self.__phone = phone

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


class Employee(Person):

    def __init__(self, name: str, age: int, phone: str, id: int):
        super().__init__(name, age, phone)
        self.__id = id
        self.__level = id % 7

    def info(self):
        return f"{self.__id} : ({self.__level}) {self.get_full_name()} / {self.get_age()} / {self.get_phone()}"


e = Employee("Иван", 33, "1-234-567-8901", 123456)
print(e.info())