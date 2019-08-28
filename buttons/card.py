from PyQt5 import QtWidgets
import images
import pickle

class button(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)

        self.clicked.connect(self.show_card)

    def show_card(self):
        self.f = open('image.pic', 'rb')
        self.image_name = pickle.load(self.f)
        self.f.close()
        self.pixmap = QtGui.QPixmap('card10.png')
        self.label.setPixmap(self.pixmap)
