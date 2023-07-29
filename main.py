from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QHBoxLayout,QVBoxLayout
from PySide6.QtCore import Qt
from ui_mainwindow import Ui_MainWindow

import sys

def hello():
    print("a")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.ui.clear_button.clicked.connect(hello)
    window.show()

    sys.exit(app.exec())

