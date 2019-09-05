from PyQt5 import QtWidgets, QtGui, QtCore
from engine import number

class NumberLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        self.font = QtGui.QFont('Segoi Ui', 50)

        self.beginSpin = QtWidgets.QSpinBox()
        self.beginSpin.setStyleSheet('color: white')
        self.endSpin = QtWidgets.QSpinBox()
        self.endSpin.setStyleSheet('color: white')
        self.numLabel = QtWidgets.QLabel('?')
        self.numLabel.setStyleSheet('color: white')
        self.numButton = QtWidgets.QPushButton(flat = True)
        self.numButton.setStyleSheet(self.style)

        self.numLabel.setFont(self.font)

        self.upLay = QtWidgets.QHBoxLayout()
        self.upLay.addSpacing(40)
        self.upLay.addWidget(self.beginSpin)
        self.upLay.addSpacing(100)
        self.upLay.addWidget(self.endSpin)
        self.upLay.addSpacing(40)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(125)
        self.bLay.addWidget(self.numButton)
        self.bLay.addSpacing(125)

        self.addSpacing(35)
        self.addLayout(self.upLay)
        self.addWidget(self.numLabel, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.bLay)
        self.addSpacing(15)

        self.numButton.clicked.connect(self.chooseNumber)

    def chooseNumber(self):
        self.beginValue = self.beginSpin.value()
        self.endValue = self.endSpin.value()
        self.choice = number.choose(self.beginValue, self.endValue)
        self.numLabel.setText(str(self.choice))
