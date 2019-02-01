def firstNameFunc(myFunc):
    def inSideFunc():
        return myFunc() + " welcome back "

    return inSideFunc


@firstNameFunc
def lastNameFunc():
    return "amanar"


print("Abde " + lastNameFunc())
