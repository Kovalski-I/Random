from PyQt5 import QtWidgets, QtCore

class ComboBox(QtWidgets.QComboBox):
    def __init__(self):
        QtWidgets.QComboBox.__init__(self)

        self.list = ['', 'Yes or No', 'Number', 'Name', 'Letter']

        self.comboModel = QtCore.QStringListModel(self.list)
        self.setModel(self.comboModel)
