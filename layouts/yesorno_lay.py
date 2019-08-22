from PyQt5 import QtWidgets

class YesOrNo_Layout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.font)

        self.button = QtWidgets.QPushButton()

        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter)
        self.addWidget(self.button)
