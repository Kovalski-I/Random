from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Random')
        self.resize(800, 450)
        self.setStyleSheet('background-color: white')

        self.font = QtGui.QFont('Segoi Ui', 20)

        self.label = QtWidgets.QLabel('              Welcome!\nChoose a mode to get started')
        self.label.setFont(self.font)

        self.combo = QtWidgets.QComboBox()

        self.combobox = QtWidgets.QHBoxLayout()
        self.combobox.addSpacing(275)
        self.combobox.addWidget(self.combo)
        self.combobox.addSpacing(275)

        self.box = QtWidgets.QVBoxLayout(self)
        self.box.addWidget(self.label, alignment = QtCore.Qt.AlignCenter)
        self.box.addLayout(self.combobox)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
