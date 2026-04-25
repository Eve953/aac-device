import sys
from PyQt5 import QtWidgets as w
from PyQt5.QtWidgets import QApplication, QMainWindow


def App():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("AAC Device")

    window.showMaximized()
    sys.exit(app.exec_())

App()