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

        self.lay = QtWidgets.QVBoxLayout()
        self.lay.bLay = QtWidgets.QHBoxLayout()
        self.lay.upLay = QtWidgets.QHBoxLayout()

        self.combo.currentTextChanged.connect(self.remove_widgets)
        self.combo.currentTextChanged.connect(self.remove_objects)
        self.combo.currentTextChanged.connect(self.combo_changed)

    def remove_widgets(self):
        for i in reversed(range(self.lay.count())):
            if self.lay.itemAt(i).__class__.__name__ == 'QWidgetItem':
                self.lay.itemAt(i).widget().setParent(None)
            elif self.lay.itemAt(i).__class__.__name__ == 'QHBoxLayout':
                for n in reversed(range(self.lay.bLay.count())):
                    if self.lay.bLay.itemAt(n).__class__.__name__ == 'QWidgetItem':
                        self.lay.bLay.itemAt(n).widget().setParent(None)
            for r in reversed(range(self.lay.upLay.count())):
                if self.lay.upLay.itemAt(r).__class__.__name__ == 'QWidgetItem':
                    self.lay.upLay.itemAt(r).widget().setParent(None)

    def remove_objects(self):
        for i in reversed(range(self.box.count())):
            if self.box.itemAt(i).__class__.__name__ == 'QWidgetItem':
                self.box.itemAt(i).widget().setParent(None)
            elif self.box.itemAt(i).__class__.__name__ == 'QVBoxLayout':
                self.box.itemAt(i).layout().setParent(None)
            elif self.box.itemAt(i).__class__.__name__ == 'YesOrNo_Layout':
                self.box.itemAt(i).layout().setParent(None)
            elif self.box.itemAt(i).__class__.__name__ == 'NumberLayout':
                self.box.itemAt(i).layout().setParent(None)
            elif self.box.itemAt(i).__class__.__name__ == 'NameLayout':
                self.box.itemAt(i).layout().setParent(None)
            elif self.box.itemAt(i).__class__.__name__ == 'LetterLayout':
                self.box.itemAt(i).layout().setParent(None)


    def combo_changed(self):
        if self.combo.currentIndex() == 1:

            self.lay = yesorno_lay.YesOrNo_Layout()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 2:

            self.lay = number_lay.NumberLayout()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 3:

            self.lay = name_lay.NameLayout()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 4:

            self.lay = letter_layout.LetterLayout()
            self.box.addLayout(self.lay)

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
