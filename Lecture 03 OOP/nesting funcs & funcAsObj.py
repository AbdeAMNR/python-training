def firstNameFunc(myFunc):
    def inSideFunc():
        return myFunc()

    return inSideFunc


def lastNameFunc():
    return "amanar"


# asign func to variable
# use func a s arg
lastFunc = firstNameFunc(lastNameFunc)

print("Abde " + lastFunc())
