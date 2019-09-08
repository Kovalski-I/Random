from PyQt5 import QtWidgets

class SpinBox(QtWidgets.QSpinBox):
    def __init__(self):
        QtWidgets.QSpinBox.__init__(self)
        ''' Creating elements '''
        self.setStyleSheet('color: white')
        self.setMaximum(1000) # setting maximum spin value
