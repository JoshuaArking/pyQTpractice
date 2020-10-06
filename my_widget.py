import sys
from PySide2 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.num = 0

        self.button = QtWidgets.QPushButton("Button text")
        self.text = QtWidgets.QLabel("Label text")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.inc_counter)

    def inc_counter(self):
        self.num = self.num + 1
        self.text.setText("Button clicked " + str(self.num) + " times.")