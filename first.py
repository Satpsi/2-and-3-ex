import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.repaint)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter(self)
        for circle in self.circles:
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(*circle)

    def repaint(self):
        x = random.randint(50, 350)
        y = random.randint(50, 250)
        d = random.randint(20, 100)
        self.circles.append((x, y, d, d))
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
