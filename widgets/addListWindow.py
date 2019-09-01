from PyQt5 import QtWidgets, QtCore, QtGui
from layouts import name_lay
import pickle

class AddWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.style = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """

        self.setWindowFlags(QtCore.Qt.SubWindow)
        self.setWindowTitle('Adding List')
        self.resize(350, 480)
        self.setStyleSheet('background-color: black')

        self.text = []

        self.icon = QtGui.QIcon('appIcon.png')
        self.setWindowIcon(self.icon)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit2 = QtWidgets.QLineEdit()
        self.addButton = QtWidgets.QPushButton('Add String', flat = True)
        self.goButton = QtWidgets.QPushButton('Go', flat = True)
        self.addButton.setStyleSheet(self.style)
        self.goButton.setStyleSheet(self.style)

        self.lineBox = QtWidgets.QVBoxLayout()
        self.lineBox.addWidget(self.lineEdit)
        self.lineBox.addSpacing(37.5)
        self.lineBox.addWidget(self.lineEdit2)

        self.buttonBox = QtWidgets.QVBoxLayout()
        self.buttonBox.addWidget(self.addButton)
        self.buttonBox.addWidget(self.goButton)

        self.addBox = QtWidgets.QVBoxLayout(self)
        self.addBox.addLayout(self.lineBox, stretch = 30)
        self.addBox.addLayout(self.buttonBox)

        self.addButton.clicked.connect(self.addString)
        self.goButton.clicked.connect(self.go)

    def addString(self):
        self.value = self.lineEdit.text()
        self.text += [self.value]
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineBox.addSpacing(37.5)
        self.lineBox.addWidget(self.lineEdit)
        print(self.text)

    def go(self):
        self.value = self.lineEdit.text()
        self.value2 = self.lineEdit2.text()
        self.text += [self.value, self.value2]
        self.file = 'list.pic'
        f = open(self.file, 'wb')
        pickle.dump(self.text, f)
        self.close()
        print(self.text)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = AddWindow()
    win.show()
    sys.exit(app.exec_())
