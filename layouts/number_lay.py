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

        self.spinBox = QtWidgets.QHBoxLayout()
        self.spinBox.addSpacing(40)
        self.spinBox.addWidget(self.beginSpin)
        self.spinBox.addSpacing(100)
        self.spinBox.addWidget(self.endSpin)
        self.spinBox.addSpacing(40)

        self.buttonBox = QtWidgets.QHBoxLayout()
        self.buttonBox.addSpacing(125)
        self.buttonBox.addWidget(self.numButton)
        self.buttonBox.addSpacing(125)

        self.addSpacing(35)
        self.addLayout(self.spinBox)
        self.addWidget(self.numLabel, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.buttonBox)
        self.addSpacing(15)

        self.numButton.clicked.connect(self.chooseNumber)

    def chooseNumber(self):
        self.beginValue = self.beginSpin.value()
        self.endValue = self.endSpin.value()
        self.choice = number.choose(self.beginValue, self.endValue)
        self.numLabel.setText(str(self.choice))
