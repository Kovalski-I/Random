from PyQt5 import QtWidgets

class button(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setFlat(True)
        self.setStyleSheet('color: white')
        self.clicked.connect(self.choose)

    def choose(self):
        print('yesorno')
        self.choiceLabel.setText(name.choose('YES', 'NO'))
