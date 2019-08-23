from PyQt5 import QtWidgets, QtGui, QtCore
from layouts import yesorno_lay
from layouts import number_lay
from layouts import name_lay
from engine import name
from widgets import combobox


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Random')
        self.resize(800, 450)

        self.icon = QtGui.QIcon('appIcon.png')
        self.setWindowIcon(self.icon)

        self.font = QtGui.QFont('Segoi Ui', 20)

        self.label = QtWidgets.QLabel('              Welcome!\nChoose a mode to get started')
        self.label.setFont(self.font)

        self.combo = combobox.ComboBox()

        self.combobox = QtWidgets.QHBoxLayout()
        self.combobox.addSpacing(275)
        self.combobox.addWidget(self.combo)
        self.combobox.addSpacing(275)

        self.box = QtWidgets.QVBoxLayout(self)
        self.box.addWidget(self.label, alignment = QtCore.Qt.AlignCenter)
        self.box.addLayout(self.combobox)
        self.box.addSpacing(30)

        self.combo.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        if self.combo.currentIndex() == 1:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.choiceBox = yesorno_lay.YesOrNo_Layout()
            self.box.insertLayout(1, self.choiceBox)

        elif self.combo.currentIndex() == 2:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.numLayout = number_lay.NumberLayout()
            self.box.insertLayout(1, self.numLayout)

        elif self.combo.currentIndex() == 3:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.nameLayout = name_lay.NameLayout()
            self.box.insertLayout(-1, self.nameLayout)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
