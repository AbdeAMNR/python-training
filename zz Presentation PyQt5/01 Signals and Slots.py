"""
Author: Abderrahim AMANAR
"""

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    txt = None
    button = None
    lbl = None

    def __init__(self, title):
        super().__init__()
        self.title = title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, 400, 200)

        self.txt = QLineEdit(self)
        self.txt.setGeometry(100, 50, 200, 20)
        self.txt.setFont(QFont("Lucida", weight=QFont.Bold))
        self.txt.setInputMask("54564646")

        button = QPushButton('Puissance', self)
        button.setToolTip('Hello Big Data Class')
        button.move(150, 80)
        button.clicked.connect(self.on_click)

        self.lbl = QLabel(self)
        self.lbl.setText("Result her")
        self.lbl.setFont(QFont("Times", weight=QFont.Bold))

        self.lbl.move(150, 150)
        self.show()

    @pyqtSlot()
    def on_click(self):
        my_input = self.txt.text()
        res = pow(int(my_input), 2)
        self.lbl.setText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App("PyQt5 button by AMANAR")
    sys.exit(app.exec_())
