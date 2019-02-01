def add(*args):
    res = 0
    for ar in args:
        res += ar
    return res


print("{}".format(add(1, 2, 3, 6, 8, 9, 55, 2, 5, 15, 85)))

ls = [1, 2, 3, 6, 8, 9, 55, 2, 5, 15, 85]

print(str(add(*ls)))
