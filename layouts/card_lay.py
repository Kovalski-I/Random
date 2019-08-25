from PyQt5 import QtWidgets, QtGui, QtCore
from engine import card
from engine import number

class CardLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.font = QtGui.QFont('Segoi Ui', 50)

        self.label = QtWidgets.QLabel('?')
        self.label.setFont(self.font)

        self.button = QtWidgets.QPushButton()

        self.buttonLay = QtWidgets.QHBoxLayout()
        self.buttonLay.addSpacing(100)
        self.buttonLay.addWidget(self.button)
        self.buttonLay.addSpacing(100)

        self.addWidget(self.label, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.buttonLay)

        self.button.clicked.connect(self.show_card)

    def show_card(self):
        import images
        import pickle
        self.f = open('image.pic', 'rb')
        self.image_name = pickle.load(self.f)
        self.f.close()
        self.pixmap = QtGui.QPixmap(self.image_name)
        self.label.setPixmap(self.pixmap)
