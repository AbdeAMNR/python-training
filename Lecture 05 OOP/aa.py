class Compte(object):
    def __init__(self, numero, nom_titulaire, solde):
        self.__numero = numero
        self.__nomTitulaire = nom_titulaire
        self.__solde = solde

    def getSolde(self):
        return self.__solde

    def _retirer(self, rMontant):
        if self.__solde >= rMontant:
            self.__solde -= rMontant
            print("bien retirer")


class CompteCourant(Compte):
    def __init__(self, numero, nom_titulaire, solde):
        super().__init__(numero, nom_titulaire, solde)
        self.__decouvert_autorise = 0

    def setDecouvertAutorise(self, decouvert_autorise):
        self.__decouvert_autorise = decouvert_autorise

    def _retirer(self, m):
        print(str(self.__decouvert_autorise))
        if m >= self.__decouvert_autorise:
            return "plus que le solde autorisé"
        else:
            if self.getSolde() >= m:
                super()._retirer(m)
                return "ok bien retirer"
            else:
                return "pas de solde"


p = CompteCourant(1425, "azer", 8000)
p.setDecouvertAutorise(1000)
print(p._retirer(500))
