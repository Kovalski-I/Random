from PyQt5 import QtWidgets, QtGui, QtCore

class lay(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.font = QtGui.QFont('Segoi Ui', 50)

        self.emptyLabel = QtWidgets.QLabel()
        self.beginSpin = QtWidgets.QSpinBox()
        self.endSpin = QtWidgets.QSpinBox()
        self.statusLabel = QtWidgets.QLabel('There is no list the program can take names from')
        self.addListBtn = QtWidgets.QPushButton('Add List', flat = True)

        self.stackLay = QtWidgets.QStackedLayout()
        self.stackLay.addWidget(self.addListBtn)
        self.stackLay.addWidget(self.endSpin)

        self.addLayout(self.stackLay)
