from PyQt5 import QtWidgets, QtCore, QtGui
from widgets import addListWindow
import random
import pickle

class NameLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """
        self.styleSheet = 'color: white'

        self.choiceFont = QtGui.QFont('Segoi Ui', 50)
        self.addFont = QtGui.QFont('Segoi Ui', 12)

        self.statusLabel = QtWidgets.QLabel('There is no list the program can take names from')
        self.addLabel = QtWidgets.QPushButton('Add list')
        self.addLabel.setFlat(True)
        self.addLabel.setFont(self.addFont)
        self.statusLabel.setFont(self.addFont)
        self.addLabel.setStyleSheet(self.styleSheet)
        self.statusLabel.setStyleSheet(self.styleSheet)
        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.choiceFont)
        self.choiceLabel.setStyleSheet(self.styleSheet)
        self.goButton = QtWidgets.QPushButton(flat = True)
        self.goButton.setStyleSheet(self.style)

        self.labelBox = QtWidgets.QVBoxLayout()
        self.labelBox.addWidget(self.statusLabel, alignment = QtCore.Qt.AlignCenter)
        self.labelBox.addWidget(self.addLabel, alignment = QtCore.Qt.AlignCenter)

        self.buttonBox = QtWidgets.QHBoxLayout()
        self.buttonBox.addSpacing(125)
        self.buttonBox.addWidget(self.goButton)
        self.buttonBox.addSpacing(125)

        self.addSpacing(20)
        self.addLayout(self.labelBox)
        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter, stretch = 10)
        self.addLayout(self.buttonBox)
        self.addSpacing(15)

        self.addLabel.clicked.connect(self.show_win)
        self.goButton.clicked.connect(self.do_random)

    def show_win(self):
        self.addWin = addListWindow.AddWindow()
        self.addWin.show()

    def do_random(self):
        self.file_name = 'list.pic'
        self.f = open(self.file_name, 'rb')
        self.list = pickle.load(self.f)
        self.choiceLabel.setText(random.choice(self.list))
