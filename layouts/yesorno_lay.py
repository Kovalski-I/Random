from PyQt5 import QtWidgets, QtCore, QtGui
from engine import yesorno

class YesOrNo_Layout(QtWidgets.QVBoxLayout):
    def __init__(self):
        QtWidgets.QVBoxLayout.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        ''' Creating elemets '''
        self.upLay = QtWidgets.QVBoxLayout() # Empty box to avoid AttibuteError

        self.font = QtGui.QFont('Bahnschrift SemiLight SemiConde', 90)

        self.choiceLabel = QtWidgets.QLabel('?')
        self.choiceLabel.setFont(self.font)
        self.choiceLabel.setStyleSheet('color: white')

        self.button = QtWidgets.QPushButton(flat = True)
        self.button.setStyleSheet(self.style)
        self.button.clicked.connect(self.animate)
        self.button.clicked.connect(self.yesOrNo)

        self.bLay = QtWidgets.QHBoxLayout()
        self.bLay.addSpacing(125)
        self.bLay.addWidget(self.button)
        self.bLay.addSpacing(125)

        self.addWidget(self.choiceLabel, alignment = QtCore.Qt.AlignCenter)
        self.addSpacing(10)
        self.addLayout(self.bLay)
        self.addSpacing(30)

    def yesOrNo(self):
        ''' Function 'choose' returns 'YES' or 'NO' value '''
        self.choiceLabel.setText(yesorno.choose())

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
        self.anim = QtCore.QPropertyAnimation(self.button, b'geometry') # Setting property which is getting to be animated
        self.anim.setStartValue(self.rect)
        self.anim.setEndValue(self.rect)
        self.anim.setKeyValueAt(0.5, self.keyRect) # Making calculated rectangle be a half of animation
        self.anim.setDuration(150)

        self.anim.start()
