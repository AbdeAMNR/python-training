"""
Author: Abderrahim AMANAR
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 300, 400)
    b.move(50, 50)
    w.setWindowTitle("PyQt 5")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
