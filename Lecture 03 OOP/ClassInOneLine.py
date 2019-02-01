# create a class in one single line.
# pros:
#   less lines of code
#   dynamic class creation
# cons: the code cold be be missy: not recommended for long classes

BaseClass = type("BaseClass", (object,), {"att": 2, "att2": 5})
C1 = type("C1", (BaseClass,), {"firstAtt": "hello", "SecAtt": 52})
C2 = type("C2", (BaseClass,), {"a": 5, "b": 88})


def myFactury(Bool_isTrue):
    return C1 if Bool_isTrue else C2


newClass = myFactury(False)

print(str(newClass.a) + " this is a factory class")
print("===================")

ClassInOneLine = type("ClassInOneLine", (object,), {"attribute": 154})
c = ClassInOneLine()
print(c.attribute)


def list(*args):
    ls = []
    for arg in args:
        ls.append(arg)
    return ls


l = list("44", "zds", "ss", 5)

print(l)


