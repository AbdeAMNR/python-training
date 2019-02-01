class TableauBlanc(object):
    # private attribute
    __incker = ""

    # constrictor
    def __init__(self, content):
        self.content = content

    def ecrire(self, new_content):
        self.content = new_content
        return True

    def lire(self):
        return self.content

    def effacer(self):
        self.content = ""
        return True

    def static_methde(cls, d):
        pass


tbl1 = TableauBlanc("hello everyone this my first oop program")
print(tbl1.lire())

print("khkdlfds {} ihofd ".format(4))


