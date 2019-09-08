from PyQt5 import QtWidgets, QtGui

class MessageBox(QtWidgets.QMessageBox):
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)

        ''' Setting text and icons of message box '''

        self.icon = QtGui.QIcon('appIcon.png')

        self.setIcon(QtWidgets.QMessageBox.Information)
        self.setWindowTitle('No List')
        self.setWindowIcon(self.icon)
        self.setText('There is no list the program can take names from!')
        self.setInformativeText('Click "New List" to create one')
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)
