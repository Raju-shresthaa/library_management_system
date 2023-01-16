from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType

ui, _ = loadUiType('dashboard.ui')


class MainApp(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
