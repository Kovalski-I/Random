from PyQt5 import QtGui
from engine import name
import sys


def choose_card():
    app = QtGui.QGuiApplication(sys.argv)
    images = {}
    for track in range(1, 53):
        card = QtGui.QPixmap('card{0}.png'.format(track))
        images['{0}'.format(track)] = card
    name.choose(images[i] for i in range(1, 53))
