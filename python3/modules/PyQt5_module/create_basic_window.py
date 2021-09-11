#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)
root = QWidget()
root.resize(320,240)
root.setWindowTitle("This is a basic window")


root.show()


# To enter the main loop for the application
sys.exit(app.exec_())