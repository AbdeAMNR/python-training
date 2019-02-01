class adn:
    def __init__(self, chaine):
        self.chaine = chaine

    def valider(self):
        # a t g c
        bool = True
        for i in self.chaine:
            if i not in "atgc":
                bool = False
        return bool

    def saisie(self, ch):
        self.chaine = ch

    def proportion(self, chaine, test):
        a = chaine.count(test)
        return a / int(len(chaine)) * 100


ad = adn("acaaca")
print(ad.valider())
print(ad.proportion(ad.chaine, "aca"))
