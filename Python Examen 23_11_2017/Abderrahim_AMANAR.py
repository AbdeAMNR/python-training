class CRobot:
    def __init__(self, Type, NS):
        self.Type= Type
        self.NS= NS
        self.Orientation=1
        self.Etat=False

    def getType(self):
        return self.Type

    def getSN(self):
        return self.NS

    def getOrientation(self):
        '''
        z=0
        orien={1:'NORD', 2:'EST', 3:'SUD', 4:'OUEST'}
        for a in orien.keys():
            if a==self.Orientation:
                z = orien[a]
        return z
        '''
        return self.Orientation

    # recheck
    # etat
    def getStatus(self):
        if self.Etat.__eq__(True):
            return True
        else:
            return False

    # done
    def setOrientation(self, Orientation):
        orien=[1,2,3,4]
        if Orientation in orien:
            self.Orientation = Orientation

    

    def setEtat(self, stat):
        s=[True,False]
        if stat in s:
            self.Etat=stat

    
    def tourner(self):
        if self.Orientation == 1:
            self.Orientation = 4
        else:
            self.Orientation -= 1
        return self.getOrientation()

    def afficher(self):
        my_str="Status: {}\nOrientation: {}\nType: {}\nSN: {}\n".format(str(self.getStatus), str(self.getOrientation), self.Type, str(self.NS))
        return my_str

#------------------------------------------------
class CRobotMobile(CRobot):
    def __init__(self,Type=None, SN=None, ABS=None, ORD=None):
        CRobot.__init__(Type, SN)
        self.abs= ABS
        self.ORD= ORD

    def avancer(self, x):
        orien=self.getOrientation
        

    def afficherPosition(self):
        return "{}\n{}\n".format(self.ABS,self.ORD)

    def afficher(self):
        new_str = super().afficher()
        mly_str += self.afficherPosition()
        return new_str
        


# main run
if __name__=='__main__':
    my_Robots = [CRobot('cleaner',104),CRobot('washer',100645),CRobot('detecter',45645),CRobot('helper',87898)]
    my_Robots[0].setEtat(True)
    print('etat',my_Robots[0].getStatus())
    my_Robots[0].setOrientation(2)
    print('postion',my_Robots[0].getOrientation())
    
    
    my_Robots[0].tourner()
    print(my_Robots[0].afficher())
    

    my_Robots[1].setEtat(True)
    my_Robots[1].setOrientation(4)
    my_Robots[1].tourner()
    print(my_Robots[1].afficher())
    
    '''
    r=CRobotMobile()
    r.tourner()
    '''





    
