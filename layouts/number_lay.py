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

        self.font = QtGui.QFont('Bahnschrift SemiLight SemiConde', 90)

        self.beginSpin = QtWidgets.QSpinBox()
        self.beginSpin.setStyleSheet('color: white')
        self.endSpin = QtWidgets.QSpinBox()
        self.endSpin.setStyleSheet('color: white')
        self.numLabel = QtWidgets.QLabel('?')
        self.numLabel.setStyleSheet('color: white')
        self.button = QtWidgets.QPushButton(flat = True)
        self.button.setStyleSheet(self.style)

        self.numLabel.setFont(self.font)

        self.upLay = QtWidgets.QHBoxLayout()
        self.upLay.addSpacing(40)
        self.upLay.addWidget(self.beginSpin)
        self.upLay.addSpacing(100)
        self.upLay.addWidget(self.endSpin)
        self.upLay.addSpacing(40)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(125)
        self.bLay.addWidget(self.button)
        self.bLay.addSpacing(125)

        self.addSpacing(35)
        self.addLayout(self.upLay)
        self.addWidget(self.numLabel, alignment = QtCore.Qt.AlignCenter)
        self.addLayout(self.bLay)
        self.addSpacing(30)

        self.button.clicked.connect(self.chooseNumber)
        self.button.clicked.connect(self.animate)

    def chooseNumber(self):
        self.beginValue = self.beginSpin.value()
        self.endValue = self.endSpin.value()
        self.choice = number.choose(self.beginValue, self.endValue + 1)
        self.numLabel.setText(str(self.choice))

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
