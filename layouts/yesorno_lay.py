from PyQt5 import QtWidgets, QtCore, QtGui
from engine import name

class YesOrNo_Layout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        self.font = QtGui.QFont('Segoi Ui', 50)

        self.upLay = QtWidgets.QHBoxLayout()

        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.font)
        self.choiceLabel.setStyleSheet('color: white')

        self.button = QtWidgets.QPushButton(flat = True)
        self.button.setStyleSheet(self.style)
        self.button.clicked.connect(self.yesOrNo)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(100)
        self.bLay.addWidget(self.button)
        self.bLay.addSpacing(100)

        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.bLay)
        self.addSpacing(30)

    def yesOrNo(self):
        self.choiceLabel.setText(name.choose('Yes', 'No'))
