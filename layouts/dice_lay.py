from PyQt5 import QtWidgets, QtGui, QtCore
from engine import number

class DiceLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.font = QtGui.QFont('Segoi Ui', 50)
        self.label = QtWidgets.QLabel('?')
        self.button = QtWidgets.QPushButton()

        self.label.setFont(self.font)

        self.buttonBox = QtWidgets.QHBoxLayout()
        self.buttonBox.addSpacing(100)
        self.buttonBox.addWidget(self.button)
        self.buttonBox.addSpacing(100)

        self.addWidget(self.label, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.buttonBox)

        self.button.clicked.connect(self.dice)

    def dice(self):
        pass
