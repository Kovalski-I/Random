from PyQt5 import QtWidgets, QtGui, QtCore
# Local imports
from engine import number
from widgets import spinbox

class NumberLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        ''' Creating elements '''
        self.font = QtGui.QFont('Bahnschrift SemiLight SemiConde', 90)

        self.beginSpin = spinbox.SpinBox()
        self.endSpin = spinbox.SpinBox()
        self.numLabel = QtWidgets.QLabel('?')
        self.numLabel.setStyleSheet('color: white')
        self.button = QtWidgets.QPushButton(flat = True)
        self.button.setStyleSheet(self.style)

        self.numLabel.setFont(self.font)

        self.upLay = QtWidgets.QHBoxLayout()
        self.upLay.addSpacing(60)
        self.upLay.addWidget(self.beginSpin)
        self.upLay.addSpacing(100)
        self.upLay.addWidget(self.endSpin)
        self.upLay.addSpacing(60)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(125)
        self.bLay.addWidget(self.button)
        self.bLay.addSpacing(125)

        self.addSpacing(20)
        self.addLayout(self.upLay)
        self.addWidget(self.numLabel, alignment = QtCore.Qt.AlignCenter)
        self.addSpacing(12)
        self.addLayout(self.bLay)
        self.addSpacing(30)

        self.button.clicked.connect(self.chooseNumber)
        self.button.clicked.connect(self.animate)

    def chooseNumber(self):
        ''' Getting a values of spin boxes '''
        self.beginValue = self.beginSpin.value()
        self.endValue = self.endSpin.value()
        ''' Sending values to "choose" fucntion which returns a randomly chosen number
        in range '''
        try:
            self.choice = number.choose(self.beginValue, self.endValue + 1)
            self.numLabel.setText(str(self.choice))
        except ValueError:
            ''' Switching varible's values to prevent an error '''
            self.choice = number.choose(self.endValue, self.beginValue + 1)
            self.numLabel.setText(str(self.choice))

    def animate(self):
        ''' Getting cordinates and size of the animated button '''
        self.x = self.button.x()
        self.y = self.button.y()
        self.w = self.button.width()
        self.h = self.button.height()

        ''' Calculating a coordinates of diminished button '''
        self.move_x = self.w / 4
        self.move_y = self.h / 4
        self.new_x = self.x + self.move_x
        self.new_y = self.y + self.move_y
        self.new_w = self.w / 2
        self.new_h = self.h / 2

        self.rect = QtCore.QRect(self.x, self.y, self.w, self.h) # Creating QRect with got coordinates
        self.keyRect = QtCore.QRect(self.new_x, self.new_y, self.new_w, self.new_h)#Creating QRect with calculated corrds

        ''' Creating animation  '''
        self.anim = QtCore.QPropertyAnimation(self.button, b'geometry') #Setting property which is getting to be animated
        self.anim.setStartValue(self.rect)
        self.anim.setEndValue(self.rect)
        self.anim.setKeyValueAt(0.5, self.keyRect) # Making calculated rectangle be a half of animation
        self.anim.setDuration(150)

        self.anim.start()
