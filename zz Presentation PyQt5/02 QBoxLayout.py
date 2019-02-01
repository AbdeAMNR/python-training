"""
Author: Abderrahim AMANAR
"""

import sys
from PyQt5.QtWidgets import *


# Resized window. Position and size changes dynamically
def call():
    print('ghbjk')


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    b1 = QPushButton("Button1")
    b1.clicked.connect(lambda: call())
    b2 = QPushButton("Button2")
    vbox = QHBoxLayout()
    vbox.addWidget(b1)
    vbox.addStretch()
    vbox.addWidget(b2)
    win.setLayout(vbox)
    win.setWindowTitle("PyQt")

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
