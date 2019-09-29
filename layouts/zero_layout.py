from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ZeroLay(QVBoxLayout):
    def __init__(self):
        QVBoxLayout.__init__(self)

        self.upLay = QVBoxLayout() # Avoiding AttributeError while page swithcing

        self.font = QFont('Bahnschrift SemiLight SemiConde', 50)

        self.href = '''<a href='https://sourceforge.net/projects/random-proj/'>sourceforge</a>'''

        self.label = QLabel('Leave your review on')
        self.link = QLabel(self.href)

        self.label.setFont(self.font)
        self.link.setFont(self.font)

        self.label.setStyleSheet('color: white')
        self.label.setAlignment(Qt.AlignCenter)
        self.link.setAlignment(Qt.AlignCenter)

        self.addWidget(self.label)
        self.addWidget(self.link)
