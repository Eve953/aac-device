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

    no_button = QPushButton("No")
    no_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    no_button.setFixedSize(400, 200)
    
    yes_button = QPushButton("Yes")
    yes_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    yes_button.setFixedSize(400, 200)
 

    i_button = QPushButton("I")
    i_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    i_button.setFixedSize(400, 200)
   
    layout.setContentsMargins(10, 10, 10, 10)
    

    layout.addWidget(no_button, 0, 0)
    layout.addWidget(yes_button, 0, 1)
    layout.addWidget(i_button, 1, 0)
    layout.setSpacing(5)




    window.showMaximized()
    sys.exit(app.exec_())

App()