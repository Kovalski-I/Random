from PyQt5 import QtWidgets, QtGui, QtCore
from engine import letter

class LetterLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        self.font = QtGui.QFont('Bahnschrift SemiLight SemiConde', 90)

        self.upLay = QtWidgets.QVBoxLayout()

        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.font)
        self.choiceLabel.setStyleSheet('color: white')

        self.button = QtWidgets.QPushButton(flat = True)
        self.button.setStyleSheet(self.style)
        self.button.clicked.connect(self.choose_letter)
        self.button.clicked.connect(self.animate)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(125)
        self.bLay.addWidget(self.button)
        self.bLay.addSpacing(125)

        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.bLay)
        self.addSpacing(30)

    def choose_letter(self):
        self.choiceLabel.setText(letter.choose())

    def animate(self):
        self.x = self.button.x()
        self.y = self.button.y()
        self.w = self.button.width()
        self.h = self.button.height()

        self.move_x = self.w / 4
        self.move_y = self.h / 4
        self.new_x = self.x + self.move_x
        self.new_y = self.y + self.move_y
        self.new_w = self.w / 2
        self.new_h = self.h / 2

        self.rect = QtCore.QRect(self.x, self.y, self.w, self.h)
        self.keyRect = QtCore.QRect(self.new_x, self.new_y, self.new_w, self.new_h)

        self.anim = QtCore.QPropertyAnimation(self.button, b'geometry')
        self.anim.setStartValue(self.rect)
        self.anim.setEndValue(self.rect)
        self.anim.setKeyValueAt(0.5, self.keyRect)
        self.anim.setDuration(100)

        self.anim.start()
