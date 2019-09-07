from PyQt5.QtCore import (QPropertyAnimation, QRect)

class animation(QPropertyAnimation):
    def __init__(self, object, type, x, y, width, height):
        super().__init__(self, object, type, x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.move_x = 4 / self.width
        self.move_y = self.height / 4

        self.new_x = self.x + self.move_x
        self.new_y = self.y + self.move_y

        self.new_width = self.width / 2
        self.new_height = self.height / 2

        self.rect = QRect(self.x, self.y, self.width, self.height)
        self.keyRect = QRect(self.new_x, self.new_y, self.new_width, self.new_height)

    def animate(self):
        self.setStartValue(self.rect)
        self.setEndValue(self.rect)
        self.setKeyValueAt(0.5, self.keyRect)
        self.setDuration(100)
