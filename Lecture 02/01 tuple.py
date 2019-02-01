# EX2
import math


def racinespoly2(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (math.sqrt(delta) - b) / 2 * a
        x2 = (math.sqrt(delta) - b) / 2 * a
        return tuple(x1, x2)
    elif delta == 0:
        x = (-b) / (2 * a)
        return tuple(x, )
    else:
        return tuple()


print(racinespoly2(56, 9, 4))

'''
#EX3
def ex2Func():
    Reg = {1: "rabat-sale", 12: "casablanca", 18: "marrakeche", 46: "fez", 89: "Tanger"}
    for i in reg:
'''
