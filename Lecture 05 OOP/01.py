class Telephone(object):
    def __init__(self):
        self.__numeroSerie = "45f4d54fd"
        self.__modele = "Sam"
        self._codePine = "1234"
        self.__numero = "0123456789"

    def _callLise(self):
        print("liste")

    def _message(self):
        print("messages....")

    def _getNumSerie(self):
        return self.__numeroSerie


class TelephonePhoto(Telephone):
    def __init__(self):
        super(TelephonePhoto, self).__init__()
        #  Telephone.__init__(self)

    def allumer(self, givenPin):
        if givenPin == self._codePine:
            print("pin ok")
            self._callLise()
            self._message()
        else:
            print("pin incorrect")

    def testEnc(self):
        #  self.__numeroSerie
        print(self._codePine)
        print(self._getNumSerie())


SB = TelephonePhoto()
SB.allumer("1234")
SB.testEnc()
