import sys

from mainwindow import MainWindow
from PySide6.QtWidgets import QApplication, QStyleFactory


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Windows"))
    window = MainWindow()
    window.show()
    app.exec()
