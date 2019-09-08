from PyQt5 import QtWidgets, QtCore

class ComboBox(QtWidgets.QComboBox):
    def __init__(self):
        QtWidgets.QComboBox.__init__(self)

        ''' Creating a list for a model '''
        self.list = ['', 'Yes or No', 'Number', 'List', 'Letter']

        self.comboModel = QtCore.QStringListModel(self.list)
        ''' Setting a model to combobox '''
        self.setModel(self.comboModel)

    def focusInEvent(self, ev):
        self.clearFocus() # clearFocus() in order to get rid of blue color
