from PyQt5 import QtWidgets, QtGui, QtCore
from layouts import layout
from engine import name
from widgets import combobox
from buttons import card, yesorno


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

        self.yesButton = QtWidgets.QPushButton(flat = True)
        self.yesButton.setStyleSheet(self.buttonStyle)
        self.numberButton = QtWidgets.QPushButton(flat = True)
        self.numberButton.setStyleSheet(self.buttonStyle)

        self.stackedLay = QtWidgets.QStackedLayout()
        self.stackedLay.addWidget(self.yesButton)
        self.stackedLay.addWidget(self.numberButton)

        self.HButtonLay = QtWidgets.QHBoxLayout()
        self.HButtonLay.addSpacing(100)
        self.HButtonLay.addLayout(self.stackedLay)
        self.HButtonLay.addSpacing(100)

        self.combo.currentTextChanged.connect(self.combo_changed)
        self.yesButton.clicked.connect(self.yes_or_no)
        self.numberButton.clicked.connect(self.chooseNumber)

    def combo_changed(self):
        if self.combo.currentIndex() == 1:

            self.label.setText('?')              # Something funky here
            self.box.removeWidget(self.label)

            self.Layout = layout.lay()
            self.box.insertLayout(-1, self.Layout, stretch = 1)
            self.box.addLayout(self.HButtonLay)

            self.stackedLay.setCurrentIndex(0)

        elif self.combo.currentIndex() == 2:

            self.label.setText('?')              # Something funky here
            self.box.removeWidget(self.label)

            self.Layout = layout.lay()
            self.Layout.insertLayout(2, self.spinBox)
            self.box.insertLayout(1, self.Layout, stretch = 1)
            self.box.addLayout(self.HButtonLay)

            self.stackedLay.setCurrentIndex(1)

        elif self.combo.currentIndex() == 3:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.Layout = layout.lay()
            self.box.insertLayout(1, self.Layout)

        elif self.combo.currentIndex() == 4:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.Layout = layout.lay()
            self.box.insertLayout(1, self.Layout)

        elif self.combo.currentIndex() == 5:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.Layout = layout.lay()
            self.box.insertLayout(1, self.Layout)

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
