"""
Задание №3
📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения возраста на год,
full_name для вывода полного ФИО и т.п. на ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого изменения,
но есть возможность получить текущий возраст.
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


p = Person("Иван", 33, "1-234-567-8901")
print(f"{p.get_full_name()} / {p.get_age()} / {p.get_phone()}")
p.birthday()
print(f"{p.get_full_name()} / {p.get_age()} / {p.get_phone()}")
