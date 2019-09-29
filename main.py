from PyQt5 import QtWidgets, QtGui, QtCore

#Local imports
from widgets import combobox
from layouts import (yesorno_lay, name_lay, number_lay, letter_layout, zero_layout)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Random')
        self.resize(735, 425)
        self.setStyleSheet('background-color: #000000')

        self.buttonStyle = """
        QPushButton[flat="true"]{
            background-color: white;
            border-style: outset;
        }
        """
        ''' Creating elements for greeting window '''

        self.icon = QtGui.QIcon('appIcon.png')
        self.setWindowIcon(self.icon)

        self.font = QtGui.QFont('Bahnschrift SemiLight SemiConde', 50)

        self.label = QtWidgets.QLabel('Choose a Mode')
        self.label.setFont(self.font)
        self.label.setStyleSheet('color: white')
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.combo = combobox.ComboBox()
        self.combo.setStyleSheet('color: white')

        self.combobox = QtWidgets.QHBoxLayout()
        self.combobox.addSpacing(275)
        self.combobox.addWidget(self.combo)
        self.combobox.addSpacing(275)

        self.box = QtWidgets.QVBoxLayout(self)
        self.box.addWidget(self.label, alignment = QtCore.Qt.AlignCenter)
        self.box.addLayout(self.combobox)

        ''' Setting handlers '''
        self.combo.currentTextChanged.connect(self.remove_widgets)
        self.combo.currentTextChanged.connect(self.remove_layouts)
        self.combo.currentTextChanged.connect(self.combo_changed) # occures when the value of combobox changed

        self.lay = QtWidgets.QVBoxLayout()

    def remove_widgets(self):
        ''' Setting parent of the widgets to 'None' in order to get rid of them while
        page switching '''
        try:
            for i in reversed(range(self.lay.count())): # every layout has the same name "lay"
                if self.lay.itemAt(i).__class__.__name__ == 'QWidgetItem': # getting type of the object by __name__
                    self.lay.itemAt(i).widget().setParent(None)

                if self.lay.itemAt(i).__class__.__name__ == 'QHBoxLayout':
                    for n in reversed(range(self.lay.bLay.count())):
                        if self.lay.bLay.itemAt(n).__class__.__name__ == 'QWidgetItem':
                            self.lay.bLay.itemAt(n).widget().setParent(None)

                for r in reversed(range(self.lay.upLay.count())):
                    if self.lay.upLay.itemAt(r).__class__.__name__ == 'QWidgetItem':
                        self.lay.upLay.itemAt(r).widget().setParent(None)
        except AttributeError:
            pass # Does absolutely nothing


    def remove_layouts(self):
        ''' Setting layout's parent to 'None' to free space for another one '''
        for i in reversed(range(self.box.count())):
            if self.box.itemAt(i).__class__.__name__ == 'QWidgetItem':
                self.box.itemAt(i).widget().setParent(None)

            elif self.box.itemAt(i).__class__.__name__ == 'QVBoxLayout':
                self.box.itemAt(i).layout().setParent(None)

            elif self.box.itemAt(i).__class__.__name__ == 'YesOrNo_Layout':
                self.box.itemAt(i).layout().setParent(None)

            elif self.box.itemAt(i).__class__.__name__ == 'NumberLayout':
                self.box.itemAt(i).layout().setParent(None)

            elif self.box.itemAt(i).__class__.__name__ == 'NameLayout':
                self.box.itemAt(i).layout().setParent(None)

            elif self.box.itemAt(i).__class__.__name__ == 'LetterLayout':
                self.box.itemAt(i).layout().setParent(None)


    def combo_changed(self):
        self.combo.clearFocus() # blue color doesn't fit the program's style

        ''' Setting different layouts with their own widgets '''
        if self.combo.currentIndex() == 0:

            self.lay = zero_layout.ZeroLay()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 1:

            self.lay = yesorno_lay.YesOrNo_Layout()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 2:

            self.lay = number_lay.NumberLayout()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 3:

            self.lay = name_lay.NameLayout()
            self.box.addLayout(self.lay)

        elif self.combo.currentIndex() == 4:

            self.lay = letter_layout.LetterLayout()
            self.box.addLayout(self.lay)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
