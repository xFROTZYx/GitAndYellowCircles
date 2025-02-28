import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("PyQt6 Circles")

        self.button = QPushButton("Нарисовать круг", self)
        self.button.setGeometry(150, 250, 100, 30)


class MainApp(UI):
    def __init__(self):
        super().__init__()
        self.button.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        x = random.randint(50, 300)
        y = random.randint(50, 200)
        radius = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        for x, y, radius, color in self.circles:
            qp.setBrush(color)
            qp.setPen(Qt.PenStyle.NoPen)
            qp.drawEllipse(x, y, radius, radius)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
