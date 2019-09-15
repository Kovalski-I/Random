from PyQt5 import QtWidgets, QtCore, QtGui
# Local imports
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
        self.resize(290, 375)

        self.text = []

        self.icon = QtGui.QIcon('appIcon.png')
        self.setWindowIcon(self.icon)

        self.lineEdit = QtWidgets.QLineEdit()

        self.addButton = QtWidgets.QPushButton('Add Item', flat = True)
        self.goButton = QtWidgets.QPushButton('Done', flat = True)
        self.addButton.setStyleSheet(self.style)
        self.goButton.setStyleSheet(self.style)

        self.lineBox = QtWidgets.QVBoxLayout()
        self.lineBox.addWidget(self.lineEdit)

        self.buttonBox = QtWidgets.QVBoxLayout()
        self.buttonBox.addWidget(self.addButton)
        self.buttonBox.addWidget(self.goButton)

        self.addBox = QtWidgets.QVBoxLayout(self)
        self.addBox.addLayout(self.lineBox, stretch = 30)
        self.addBox.addLayout(self.buttonBox)

        self.addButton.clicked.connect(self.addString)
        self.goButton.clicked.connect(self.go)

    def addString(self):
        if self.lineEdit.text() == '': # When there is no text in lineEdit
            return
        if self.lineBox.count() == 17: # When there is 10 lineEdits
            return
        self.lineEdit.setDisabled(True)
        self.value = self.lineEdit.text()
        self.text += [self.value]
        self.lineEdit = QtWidgets.QLineEdit() # creating new lineEdit and adding it to layout
        self.lineBox.addSpacing(37.5)
        self.lineBox.addWidget(self.lineEdit)

    def go(self):
        if self.lineEdit.text() == '':
            return
        self.value = self.lineEdit.text()
        ''' Adding values of lineEdits to list so we have all the values in there '''
        self.text += [self.value]
        ''' Pickling a list to list.pic '''
        self.file = 'list.pic'
        f = open(self.file, 'wb')
        pickle.dump(self.text, f)
        f.close()
        self.close()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = AddWindow()
    win.show()
    sys.exit(app.exec_())
