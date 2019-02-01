from CRobot import CRobot


class CRobotMobile(CRobot):
    # Question (a) et (b)
    def __init__(self, Type='cleaner', SN='1202', ABS=1, ORD=2):
        CRobot.__init__(self, Type, SN)
        self.abs = ABS
        self.ord = ORD

    def avancer(self, x, orien):
        self.set_orientation(orien)
        if orien == 2:
            self.abs += x
        elif orien == 4:
            self.abs -= x
        elif orien == 1:
            self.ord += x
        elif orien == 3:
            self.ord -= x

    def afficher_position(self):
        return "abs:{} , ord:{}\n".format(self.abs, self.ord)

    # Question (c)
    def afficher(self):
        r_desc = super().afficher() + " \n{}".format(self.afficherPosition())
        return r_desc


# Question (d)
if __name__ == '__main__':
    print("================TEST 1=================")
    print("###### CRobot program starting ######")
    print("=====================================")

    r_mobile1 = CRobotMobile('cleaner', 2002, 1, 2)
    r_mobile = CRobotMobile()

    # tourner ver l'Est
    r_mobile.set_orientation(2)

    r_mobile.avancer(4, 4)
    print('Avancer vers Ouest ==> ', r_mobile.afficher_position())

    r_mobile.avancer(6, 1)
    print('Avancer vers Nord==> ', r_mobile.afficher_position())

    r_mobile.avancer(14, 2)
    print('Avancer vers l\'Est ==> ', r_mobile.afficher_position())

    r_mobile.avancer(8, 3)
    print('Reculer vers Sud ==> ', r_mobile.afficher_position())
