"""
la durée en jours en annee
I=(C*t*d)/100

C   ➜ le montant du capital emprunté
t   ➜ le taux d'intérêt (ou taux de placement) exprimé en pourcentage pour une période donnée
d   ➜ la durée de l'emprunt (exprimé dans l'unité de référence)
I   ➜ le montant des intérêts obtenus


la différence est dans la méthode retirer
"""
from datetime import date
import datetime


class Compte(object):
    def __init__(self, numero, nom_titulaire, solde):
        self.__numero = numero
        self.__nomTitulaire = nom_titulaire
        self.__solde = solde

    def get_solde(self):
        return self.__solde

    def set_solde(self, solde):
        self.__solde = solde

    def _deposer(self, dMontant):
        self.__solde += dMontant
        print("bien deposer")

    def _retirer(self, rMontant):
        if self.__solde >= rMontant:
            self.__solde -= rMontant
            print("bien retirer")

    def _etat_comptes(self):
        return self.__solde

    def __str__(self):
        row = "titulaire: " + self.__nomTitulaire + "\n"
        row += "numéro de compte: " + str(self.__numero) + "\n"
        row += "solde: " + str(self.__solde) + "\n"
        return row


"""
la durée en jours
    I=(C*t*d)/(100*360)
la durée en mois
    I=(C*t*d)/(100*12)

C   ➜ le montant du capital emprunté
t   ➜ le taux d'intérêt (ou taux de placement) exprimé en pourcentage pour une période donnée
d   ➜ la durée de l'emprunt (exprimé dans l'unité de référence)
I   ➜ le montant des intérêts obtenus
"""


class CompteEpargne(Compte):  # حساب ادخار
    def __init__(self, numero, nom_titulaire, solde):
        super().__init__(numero, nom_titulaire, solde)
        # self.dt = datetime.datetime.now().strftime("%Y/%M/%D %H:%M")
        self.dt = date(2013, 12, 25)

    def dateDiffDays(self, date_one, date_two):
        d1 = date(date_one.year, date_one.month, date_one.day)
        d2 = date(date_two.year, date_two.month, date_two.day)
        date_diff = d2 - d1
        return int(date_diff.days)

    def calc_interet(self, taux_interet):
        c = self.get_solde()
        # print(" ==> le solde courant= " + str(c))
        t = taux_interet
        d = self.dateDiffDays(self.dt, datetime.datetime.now())
        # print(" ==> la durée= " + str(d) + " jours")
        interet = (c * t * d) / (100 * 360)
        # print(" ==> le montant des intérêts obtenus= " + str(interet) + " MAD")
        self.set_solde(self.get_solde() + interet)
        return self.get_solde()

    def __str__(self):
        return super().__str__() + "Date de création: " + "%s/%s/%s" % (self.dt.year, self.dt.month, self.dt.day)


class CompteCourant(Compte):
    def __init__(self, numero, nom_titulaire, solde):
        super().__init__(numero, nom_titulaire, solde)
        self.__decouvert_autorise = 0

    def setDecouvertAutorise(self, decouvert_autorise):
        self.__decouvert_autorise = decouvert_autorise

    def _retirer(self, m):
        if m >= self.__decouvert_autorise:
            return "plus que le solde autorisé"
        else:
            if self.get_solde() >= m:
                self.set_solde(self.get_solde() - m)
                return "solde-" + str(m) + " ok bien retirer"
            else:
                return "pas de solde"

    def __str__(self):
        return super().__str__() + "vous ne pouvez que retirer moins de " + str(self.__decouvert_autorise)


account1 = CompteEpargne(1425, "CE-azer", 5000)
print(account1.__str__())
print("===========================================")
print("+ interet ==> " + str(account1.calc_interet(8)))
print("===========================================")
print("toString() \n" + account1.__str__())
print("===========================================")

p = CompteCourant(1425, "CC6-azer", 3000)
p.setDecouvertAutorise(1000)
print("toString() \n" + p.__str__())
print(p._retirer(500))
print("votre solde maintenent est: " + str(p.get_solde()))

print(10 ** 5)
