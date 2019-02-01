class Person:
    gender = 'female'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        pass

    @full_name.getter
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, str):
        given_str = str.split()
        self.first_name = given_str[0]
        self.last_name = given_str[1]

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.age, self.gender)


p1 = Person('abde', 'AMANAR', 22)
p2 = Person('grechen', 'SEA', 20)

print(p1.full_name)
p1.full_name = 'Yassine AMANAR'
print(p1.full_name)
del p1.full_name
print(p1.full_name)
