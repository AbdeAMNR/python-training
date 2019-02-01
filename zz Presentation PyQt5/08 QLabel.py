"""
Author: Abderrahim AMANAR
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)

    win = QWidget()

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    l1.setText("Hello World")
    l4.setText("<A href='#'>LP_SIBD.COM</a>")
    url_link = " <a href=\"http://www.google.com\"> <font face=verdana size=10 color=black> This is a link</font> </a>"
    l2.setText(url_link)

    l1.setAlignment(Qt.AlignCenter)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)

    l3.setPixmap(QPixmap("python2.png"))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l4.linkActivated.connect(lambda: clicked())
    l2.linkHovered.connect(lambda: hovered())
    win.setLayout(vbox)

    win.setWindowTitle("QLabel Demo")
    l2.setOpenExternalLinks(True)

    win.show()
    sys.exit(app.exec_())


def hovered():
    print("hovering")


def clicked():
    print("clicked")


if __name__ == '__main__':
    window()
