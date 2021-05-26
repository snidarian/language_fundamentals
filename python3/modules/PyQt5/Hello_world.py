#!/usr/bin/python3
# hello world GUI


from PyQt5.QtWidgets import QApplication, QLabel


app = QApplication([])

QT_QPA_PLATFORM="wayland"

label = QLabel('Hello World')
label.show()
app.exec_()







