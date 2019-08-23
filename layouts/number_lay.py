from PyQt5 import QtWidgets, QtGui, QtCore
from engine import number

class NumberLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.font = QtGui.QFont('Segoi Ui', 50)

        self.beginSpin = QtWidgets.QSpinBox()
        self.endSpin = QtWidgets.QSpinBox()
        self.numLabel = QtWidgets.QLabel('?')
        self.numButton = QtWidgets.QPushButton()

        self.numLabel.setFont(self.font)

        self.spinBox = QtWidgets.QHBoxLayout()
        self.spinBox.addWidget(self.beginSpin)
        self.spinBox.addWidget(self.endSpin)

        self.addLayout(self.spinBox)
        self.addWidget(self.numLabel, alignment = QtCore.Qt.AlignCenter)
        self.addWidget(self.numButton)

        self.numButton.clicked.connect(self.chooseNumber)

    def chooseNumber(self):
        self.beginValue = self.beginSpin.value()
        self.endValue = self.endSpin.value()
        self.choice = number.choose(self.beginValue, self.endValue)
        self.numLabel.setText(str(self.choice))
