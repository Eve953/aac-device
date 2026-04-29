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
 

    hi_button = QPushButton("Hi")
    hi_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    hi_button.setFixedSize(400, 200)

    bye_button = QPushButton("Bye")
    bye_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    bye_button.setFixedSize(400, 200)

    help_button = QPushButton("Help")
    help_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    help_button.setFixedSize(400, 200)

    bathroom_button = QPushButton("Bathroom")
    bathroom_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    bathroom_button.setFixedSize(400, 200)

    hungry_button = QPushButton("Hungry")
    hungry_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    hungry_button.setFixedSize(400, 200)

    thirsty_button = QPushButton("Thirsty")
    thirsty_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    thirsty_button.setFixedSize(400, 200)

    i_button = QPushButton("I")
    i_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    i_button.setFixedSize(400, 200)

    need_button = QPushButton("Need")
    need_button.setStyleSheet("""
    background-color: #ffd9cc;
    color: black;
    font-size: 36px;
    border-radius: 10px;
                            
                        
""")
    
    need_button.setFixedSize(400, 200)
   
    layout.setContentsMargins(10, 10, 10, 10)
    

    layout.addWidget(no_button, 0, 0)
    layout.addWidget(yes_button, 0, 1)
    layout.addWidget(hi_button, 1, 0)
    layout.addWidget(bye_button, 1, 1)
    layout.addWidget(help_button, 2, 0)
    layout.addWidget(bathroom_button, 2, 1)
    layout.addWidget(hungry_button, 3, 0)
    layout.addWidget(thirsty_button, 3, 1)
    layout.addWidget(i_button, 3, 2)
    layout.addWidget(need_button, 3, 3)

    layout.setSpacing(10)






    window.showMaximized()
    sys.exit(app.exec_())

App()