from PyQt5 import QtGui
from engine import number
import sys
import pickle

app = QtGui.QGuiApplication(sys.argv)
num = number.choose(1, 52)
name = 'card{0}'.format(num)
f = open('image.pic', 'wb')
pickle.dump(name, f)
f.close()
