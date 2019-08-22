from PyQt5 import QtWidgets, QtGui, QtCore

from engine import name
from layouts import yesorno_lay
import combobox

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

        self.combo.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        if self.combo.currentIndex() == 1:

            self.label.setText('')              # Something funky here
            self.box.removeWidget(self.label)

            self.choiceBox = yesorno_lay.YesOrNo_Layout()

            self.box.insertLayout(1, self.choiceBox)

            self.button.clicked.connect(self.yesOrNo)

        elif self.combo.currentIndex() == 2:

            pass

    def yesOrNo(self):
        self.choiceLabel.setText(name.choose('Yes', 'No'))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
