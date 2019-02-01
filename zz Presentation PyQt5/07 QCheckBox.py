"""
Author: Abderrahim AMANAR
"""

import sys
from PyQt5.QtWidgets import *


class Checkdemo(QWidget):
    def __init__(self, parent=None):
        super(Checkdemo, self).__init__(parent)
        layout = QHBoxLayout()
        self.b1 = QCheckBox("Button1")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        layout.addWidget(self.b1)
        self.b2 = QCheckBox("Button2")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        layout.addWidget(self.b2)
        self.setLayout(layout)
        self.setWindowTitle("checkbox demo")

    def btnstate(self, b):
        if b.text() == "Button1":
            print(b.text() + " is selected") if b.isChecked() else print(b.text() + " is deselected")
        if b.text() == "Button2":
            print(b.text() + " is selected") if b.isChecked() else  print(b.text() + " is deselected")


def main():
    app = QApplication(sys.argv)
    ex = Checkdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
