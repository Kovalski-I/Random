from PyQt5 import QtWidgets, QtCore, QtGui
from engine import name

class YesOrNo_Layout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.font = QtGui.QFont('Segoi Ui', 50)

        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.font)

        self.button = QtWidgets.QPushButton()

        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter)
        self.addWidget(self.button)

        self.button.clicked.connect(self.yesOrNo)

    def yesOrNo(self):
        self.choiceLabel.setText(name.choose('Yes', 'No'))
