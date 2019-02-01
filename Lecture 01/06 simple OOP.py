class Animal:
    def make_sound(self):
        return "animal sound: "


class Dog(Animal):
    def bark(self):
        return super(Dog, self).make_sound() + "barking...!"


class Cat(Animal):
    def cat(self):
        return super(Cat, self).make_sound() + "miow...!"


my_dog = Dog()
my_cat = Cat()
print(my_dog.bark())
print(my_cat.cat())

'''Defined to support iteration over container.'''
