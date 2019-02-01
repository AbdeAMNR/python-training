class Person(object):
    """
    this is a static var
    it can be changed depends on how you access it
    p1.gender='Male' ==> static variable accessed via instance, change will affect to instance Object
    Person.gender='Male' ==> change will affect all the Instance Objects
    """
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
        return "{}, {}".format(self.full_name, self.gender)

    def __eq__(self, other):
        return True if self.full_name.__eq__(other.full_name) else False


p1 = Person('abde', 'AMANAR', 22)
p2 = Person('grechen', 'SEA', 20)

print(p1.__eq__(p2))

p1.gender = 'Male'
Person.gender = 'df'
print(p1.gender)

"""
print(p1.full_name)
p1.full_name = 'Yassine AMANAR'
print(p1.full_name)
del p1.full_name
print(p1.__str__())

print(p1.__eq__(p2))
"""
