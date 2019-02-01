class CRobot:
    def __init__(self, robot_type, serial_number):
        self.robot_type = robot_type
        self.serial_number = serial_number
        self.orientation = 0
        self.etat = False

    def get_type(self):
        return self.robot_type

    def get_serial_number(self):
        return self.serial_number

    def get_orientation(self):
        if self.orientation != 0:
            orien = {1: 'NORD', 2: 'EST', 3: 'SUD', 4: 'OUEST'}
            for o in orien.keys():
                if self.orientation.__eq__(o):
                    return orien[o]
        else:
            return 'Orientation not defined'

    # recheck
    # etat
    def get_status(self):
        return 'ONLINE' if self.etat.__eq__(True) else 'OFFLINE'

    # done
    def set_orientation(self, new_Orien):
        authorized = [1, 2, 3, 4]
        if new_Orien in authorized:
            self.orientation = new_Orien
            return True
        else:
            return False

    def set_etat(self, stat):
        if stat in list((True, False)):
            self.etat = stat
            return True
        else:
            return False

    def tourner(self):
        if self.orientation == 1:
            self.orientation = 4
        else:
            self.orientation -= 1
        return self.get_orientation()

    def afficher(self):
        my_str = "Status: {}\nOrientation: {}\nType: {}\nSerial Number: {}\n".format(self.get_status(),
                                                                                     self.get_orientation(),
                                                                                     self.robot_type,
                                                                                     self.serial_number)
        return my_str


# main run
if __name__ == '__main__':
    print("================TEST 1=================")
    print("###### CRobot program starting ######")
    print("=====================================")
    my_Robots = [CRobot('cleaner', 10001), CRobot('washer', 10002), CRobot('detecter', 10003), CRobot('helper', 10004)]
    my_Robots[0].set_etat(True)
    print('Etat: ', my_Robots[0].get_status())
    my_Robots[0].set_orientation(1)
    print('Orientation: ', my_Robots[0].get_orientation())
    print('change orientation to: ', my_Robots[0].tourner())
    print('===Robot description===\n{}'.format(my_Robots[0].afficher()))

    print("================TEST 2=================")
    print("###### CRobot program starting ######")
    print("=====================================")
    my_Robots[1].set_etat(True)
    print('Etat: ', my_Robots[0].get_status())
    my_Robots[1].set_orientation(3)
    print('Orientation: ', my_Robots[1].get_orientation())
    print('change orientation to: ', my_Robots[1].tourner())
    print('===Robot description===\n{}'.format(my_Robots[1].afficher()))




