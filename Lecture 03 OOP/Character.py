class Character(object):
    __reViveTime = 0

    def __init__(self, name, health, wapeans, damage):
        self.name = name
        self.health = health
        self.wapeans = wapeans
        self.damage = damage

    def reVive(self):
        pass

    def __str__(self):
        return "Character: {}\nHealth: {}\nWapeans{}\nDamage:{}".format(self.name, self.health, self.wapeans,
                                                                        self.damage)

    def boostLife(self, boost):
        self.__reViveTime += boost
        return "wow my life is boosted and i have now:" + str(self.__reViveTime)


class Archer(Character):
    def __init__(self, name, health, wapeans, damage):
        super(Archer, self).__init__(name, health, wapeans, damage)  # Method1 to call super attributes
        # Employee.__init__(self, salary) # Method2 to call super attributs

    def reVive(self):
        self.__reViveTime = 8


class Barbarian(Character):
    def __init__(self, name, health, wapeans, damage):
        super(Barbarian, self).__init__(name, health, wapeans, damage)

    def fight(self):
        return "i kill with {} damage per second".format(self.damage)

    def reVive(self):
        self.__reViveTime = 10
        return "my life is now " + str(self.__reViveTime)


class WallBraeker(Character):
    def __init__(self, name, health, wapeans, damage):
        super(WallBraeker, self).__init__(name, health, wapeans, damage)

    def reVive(self):
        self.__reViveTime = 2


class Wizard(Character):
    def __init__(self, name, health, wapeans, damage):
        super(Wizard, self).__init__(name, health, wapeans, damage)

    def reVive(self):
        self.__reViveTime = 15

    def createNewFormilla(self, ingredients) -> str:
        chain = ""
        for item in ingredients:
            chain += item + "\n"
        return "new formella created using:\n" + chain

    def kill(self):
        return "i killed the enemy"


barbarianOne = Barbarian("Barbarian", 100, "sword", 90)
barbarianTwo = Barbarian("Barbarian", 500, "sword", 90)
print(isinstance(barbarianOne, Wizard))

print(barbarianOne.fight())
print(barbarianOne.reVive())
print(barbarianOne.boostLife(100))

wizardOne = Wizard("Wizard", 150, "magic", 1000)

print(wizardOne.createNewFormilla(["clay", "dog Hair", "water", "blod", "oil"]))
print(wizardOne.kill())

print(Character.__subclasses__())
