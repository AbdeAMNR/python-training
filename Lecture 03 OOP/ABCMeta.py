from abc import ABCMeta, abstractmethod


class BaseClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def hay(self):
        pass


class SubClass(BaseClass):
    def sayHay(self):
        print("hello word")


x = BaseClass()
x.hay()
