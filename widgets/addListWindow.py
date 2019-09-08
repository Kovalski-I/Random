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

        ''' Creating elements '''
        self.editStyle = 'color: white'

        self.setWindowFlags(QtCore.Qt.SubWindow)
        self.setWindowTitle('Adding List')
        self.resize(350, 480)

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
        self.lineEdit.setDisabled(True) # Setting edits disabled
        self.lineEdit2.setDisabled(True)

        self.value = self.lineEdit.text()
        ''' Adding value of lineEdit to list because line edit's name will be given to new lineEdit '''
        self.text += [self.value]
        self.lineEdit = QtWidgets.QLineEdit() # giving a name to already created linEdit
        self.lineBox.addSpacing(37.5)
        self.lineBox.addWidget(self.lineEdit)

    def go(self):
        self.value = self.lineEdit.text()
        self.value2 = self.lineEdit2.text()
        ''' Adding values of lineEdits to list so we have all the values in there '''
        self.text += [self.value, self.value2]
        ''' Pickling a list to list.pic '''
        self.file = 'list.pic'
        f = open(self.file, 'wb')
        pickle.dump(self.text, f)
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = AddWindow()
    win.show()
    sys.exit(app.exec_())
