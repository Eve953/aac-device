from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys


def App():
    app = QApplication(sys.argv)
    window = QMainWindow()

    central_widget = QWidget()
    layout = QGridLayout()

    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)              
    window.setStyleSheet("background-color: black;")
    window.setWindowTitle("AAC Device")

    hi_button = QPushButton("Hi")
    hi_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    border-radius: 10px;
""")
    hi_button.setFixedSize(120, 120)
 


   
    layout.setContentsMargins(10, 10, 10, 10)
    

    layout.addWidget(hi_button, 0, 0)
    layout.setSpacing(10)




    window.showMaximized()
    sys.exit(app.exec_())

App()