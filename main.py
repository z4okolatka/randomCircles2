import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
from UI import Ui_MainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn.clicked.connect(self.draw_circles)
        self.do_paint = False

    def draw_circles(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def draw(self, qp):
        for _ in range(randint(1, 5)):
            qp.setBrush(
                QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            )
            x, y = randint(10, 440), randint(10, 350)
            r = randint(10, 50)
            qp.drawEllipse(x - r, y - r, x + r, y + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
