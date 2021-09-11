#!/usr/bin/python3


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title='hello, world'
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button=QPushButton('Click me', self)
        button.setToolTip('Thanks for thinking about me')
        button.move(100, 70)
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




