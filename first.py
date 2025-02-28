import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor


class CircleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 400, 400)
        self.button = QPushButton("Draw Circle", self)
        self.button.setGeometry(150, 350, 100, 30)
        self.button.clicked.connect(self.update)
        self.circles = []

    def paintEvent(self, event):
        qp = QPainter(self)
        for x, y, size, color in self.circles:
            qp.setBrush(QColor(*color))
            qp.drawEllipse(x, y, size, size)

    def update(self):
        x, y = random.randint(50, 300), random.randint(50, 300)
        size = random.randint(20, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, size, color))
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec())
