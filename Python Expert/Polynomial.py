class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        my_coeffs = list()
        for x, y in zip(self.coeffs, other.coeffs):
            my_coeffs.append(x + y)

        my_coeffs = tuple(my_coeffs)
        return Polynomial(*my_coeffs)
        # easy way
        # return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

        #  return tuple(x + y for x, y in zip(self.coeffs, other.coeffs), )

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(2, 3, 3)
print(p1)
print(p1 + p2)

print(p1.__len__())


def add(*a):
    return sum(a)


print(add(1, 5, 6, 9, 85))

print(add.__code__.co_varnames)
