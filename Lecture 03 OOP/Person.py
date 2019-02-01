class Person(object):
    __first_name = ""
    __last_name = ""
    __age = ""

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def full_name(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name


class Salary(Person):
    __salary = ""

    def __init__(self, first, last, age, salaire):
        Person.__init__(self, first, last, age)
        self.__salary = salaire

    def cmpSalaire(self, other):
        if self.__salary > other:
            return 1
        elif self.__salary < other:
            return -1
        elif self.__salary == other:
            return 0

    def __eq__(self, other):
        return self.__salary == other.__salary and other.__salary == self.__salary

    def get_salaire(self):
        return self.__salary


import time

salarie1 = Salary("abdo", "amanar", 52, 18255)
salarie2 = Salary("med", "aitHammou", 14, 1255)

print(salarie1.cmpSalaire(salarie2.get_salaire()))

print("================================")

print(salarie1.__eq__(salarie2))

ticks = time.time()

print("Number of ticks since 12:00am, January 1, 1970:", ticks)
