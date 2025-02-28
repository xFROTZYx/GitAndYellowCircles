import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        x = random.randint(50, 250)
        y = random.randint(50, 250)
        radius = random.randint(10, 100)
        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setBrush(QColor(255, 255, 0))
        for x, y, radius in self.circles:
            qp.drawEllipse(x, y, radius, radius)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
