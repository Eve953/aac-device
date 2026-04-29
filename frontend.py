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

    # button styling (may change later)
    # Blue for Social/General
    social_style = """
    background-color: #add8e6; 
    color: black;
    font-size: 36px;
    border-radius: 15px;
        """

# Green for Physical Needs
    needs_style = """
    background-color: #b1e4b1;
    color: black;
    font-size: 36px;
    border-radius: 15px;
        """
    # Button Creation
        # social buttons
    yes_button = QPushButton("Yes")
    yes_button.setStyleSheet(social_style)
    yes_button.setFixedSize(400, 200)

    no_button = QPushButton("No")
    no_button.setStyleSheet(social_style)
    no_button.setFixedSize(400, 200)

    help_button = QPushButton("Help")
    help_button.setStyleSheet(social_style)
    help_button.setFixedSize(400, 200)

    # needs buttons 
    hungry_button = QPushButton("Hungry")
    hungry_button.setStyleSheet(needs_style)
    hungry_button.setFixedSize(400, 200)

    thirsty_button = QPushButton("Thirsty")
    thirsty_button.setStyleSheet(needs_style)
    thirsty_button.setFixedSize(400, 200)

    bathroom_button = QPushButton("Bathroom")
    bathroom_button.setStyleSheet(needs_style)
    bathroom_button.setFixedSize(400, 200)

    # Layout Management
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)

    # General/Social Needs
    layout.addWidget(yes_button, 0, 0)
    layout.addWidget(no_button, 0, 1)
    layout.addWidget(help_button, 0, 2)

    # Physical Needs
    layout.addWidget(hungry_button, 1, 0)
    layout.addWidget(thirsty_button, 1, 1)
    layout.addWidget(bathroom_button, 1, 2)

    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    App()