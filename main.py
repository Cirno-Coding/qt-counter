import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Счётчик нажатий")

        self.btn = QPushButton("Нажатие", self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)

        self.lbl = QLabel(str(self.count), self)
        self.lbl.resize(100, 100)
        self.lbl.move(150, 25)
        self.btn.clicked.connect(self.click)

    def click(self):
        self.count += 5
        self.lbl.setText(f"{int(self.count) + 1}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
