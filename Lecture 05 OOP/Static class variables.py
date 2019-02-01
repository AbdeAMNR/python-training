class Test:
    i = 0


t = Test()
print(str(t.i) + " # static variable accessed via instance")

t.i = 5  # but if we assign to the instance ...
print(str(Test.i) + " # we have not changed the static variable")

print(str(t.i) + " # we have overwritten Test.i on t by creating a new attribute t.i")

Test.i = 6  # to change the static variable we do it by assigning to the class
print(str(t.i) + " instance var")

print(str(Test.i) + " static var")

u = Test()

print(str(u.i) + " # changes to t do not affect new instances of Test")

# Namespaces are one honking great idea -- let's do more of those!
print(Test.__dict__)

print(t.__dict__)

print(u.__dict__)
