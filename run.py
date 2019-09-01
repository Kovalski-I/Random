from PyQt5 import QtWidgets, QtGui, QtCore
from engine import name
from widgets import combobox
from buttons import card, yesorno
from layouts import (yesorno_lay, name_lay, number_lay, letter_layout)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Random')
        self.resize(800, 450)
        self.setStyleSheet('background-color: #000000')

        self.buttonStyle = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        self.icon = QtGui.QIcon('appIcon.png')
        self.setWindowIcon(self.icon)

        self.font = QtGui.QFont('Segoi Ui', 20)

        self.label = QtWidgets.QLabel('Welcome!\nChoose a mode to get started')
        self.label.setFont(self.font)
        self.label.setStyleSheet('color: white')
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.combo = combobox.ComboBox()
        self.combo.setStyleSheet('color: white')

        self.combobox = QtWidgets.QHBoxLayout()
        self.combobox.addSpacing(275)
        self.combobox.addWidget(self.combo)
        self.combobox.addSpacing(275)

        self.beginSpin = QtWidgets.QSpinBox()
        self.endSpin = QtWidgets.QSpinBox()

        self.spinBox = QtWidgets.QHBoxLayout()
        self.spinBox.addWidget(self.beginSpin)
        self.spinBox.addWidget(self.endSpin)

        self.box = QtWidgets.QVBoxLayout(self)
        self.box.addWidget(self.label, alignment = QtCore.Qt.AlignCenter)
        self.box.addLayout(self.combobox)

        self.combo.currentTextChanged.connect(self.combo_changed)
        self.combo.currentTextChanged.connect(self.remove_objects)

    def remove_objects(self):
        for i in reversed(range(self.box.count())):
            if self.box.itemAt(i).__class__.__name__ == 'QWidgetItem':
                self.box.itemAt(i).widget().setParent(None)

    def combo_changed(self):
        if self.combo.currentIndex() == 1:

            self.yesLay = yesorno_lay.YesOrNo_Layout()
            self.box.addLayout(self.yesLay)

        elif self.combo.currentIndex() == 2:

            self.numberLay = number_lay.NumberLayout()
            self.box.addLayout(self.numberLay)

        elif self.combo.currentIndex() == 3:

            self.nameLay = name_lay.NameLayout()
            self.box.addLayout(self.nameLay)

        elif self.combo.currentIndex() == 4:

            self.letterLay = letter_layout.LetterLayout()
            self.box.addLayout(self.letterLay)

    def yes_or_no(self):
        self.label.setText(name.choose('YES', 'NO'))

    def chooseNumber(self):
        self.beginValue = self.beginSpin.value()
        self.endValue = self.endSpin.value()
        self.choice = number.choose(self.beginValue, self.endValue)
        self.numLabel.setText(str(self.choice))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
