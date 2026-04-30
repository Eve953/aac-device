from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
import pyttsx3
import os
import pygame
import time

# FUNCTION FOR THE PICTURE AND TEXT LAYOUT
def create_stacked_button(button, text, icon_path):
    layout = QVBoxLayout(button)
    layout.setContentsMargins(5, 10, 5, 10)
    layout.setSpacing(5)

    # AAC WORD LABEL
    label = QLabel(text)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet("font-size: 30px; font-weight: bold; border: none; background: transparent; color: black;")
    
    # 2. ICON 
    icon_label = QLabel()
    pixmap = QPixmap(icon_path).scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    icon_label.setPixmap(pixmap)
    icon_label.setAlignment(QtCore.Qt.AlignCenter)
    icon_label.setStyleSheet("border: none; background: transparent;")
    
    layout.addWidget(label)
    layout.addWidget(icon_label)

pygame.mixer.init()
# TEXT TO SPEECH FUNCTION
def text_to_speech(text):
    temp_file = "speech.wav"  # -uses .wav files to prevent bad stream
    
    # 1. sound file
    temp_engine = pyttsx3.init()
    temp_engine.save_to_file(text, temp_file)
    temp_engine.runAndWait()
    temp_engine.stop()
    
  
    try:
        time.sleep(0.1) 
        
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        pygame.mixer.music.unload() 
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
    except Exception as e:
        print(f"Error playing sound: {e}")

def App():
    app = QApplication(sys.argv)
    window = QMainWindow()

    central_widget = QWidget()
    grid_layout = QGridLayout()
    central_widget.setLayout(grid_layout)
    window.setCentralWidget(central_widget)              
    window.setStyleSheet("background-color: black;")
    window.setWindowTitle("AAC Device")

    # STYLES FOR THE BUTTONS
    social_style = "background-color: #add8e6; border-radius: 18px;"
    needs_style = "background-color: #b1e4b1; border-radius: 18px;"

    # SOCIAL BUTTONS, FIRST ROW
    yes_btn = QPushButton()
    yes_btn.setStyleSheet(social_style)
    yes_btn.setFixedSize(400, 200)
    create_stacked_button(yes_btn, "Yes", "pictures/yes.png")
    yes_btn.clicked.connect(lambda: text_to_speech("Yes"))

    no_btn = QPushButton()
    no_btn.setStyleSheet(social_style)
    no_btn.setFixedSize(400, 200)
    create_stacked_button(no_btn, "No", "pictures/no.png")
    no_btn.clicked.connect(lambda: text_to_speech("No"))

    help_btn = QPushButton()
    help_btn.setStyleSheet(social_style)
    help_btn.setFixedSize(400, 200)
    create_stacked_button(help_btn, "Help", "pictures/help.png")
    help_btn.clicked.connect(lambda: text_to_speech("I need help"))

    # NEEDS BUTTONS, SECOND ROW
    hungry_btn = QPushButton()
    hungry_btn.setStyleSheet(needs_style)
    hungry_btn.setFixedSize(400, 200)
    create_stacked_button(hungry_btn, "Hungry", "pictures/hungry.png")
    hungry_btn.clicked.connect(lambda: text_to_speech("I am hungry"))

    thirsty_btn = QPushButton()
    thirsty_btn.setStyleSheet(needs_style)
    thirsty_btn.setFixedSize(400, 200)
    create_stacked_button(thirsty_btn, "Thirsty", "pictures/thirsty.png")
    thirsty_btn.clicked.connect(lambda: text_to_speech("I am thirsty"))

    bathroom_btn = QPushButton()
    bathroom_btn.setStyleSheet(needs_style)
    bathroom_btn.setFixedSize(400, 200)
    create_stacked_button(bathroom_btn, "Bathroom", "pictures/bathroom.png")
    bathroom_btn.clicked.connect(lambda: text_to_speech("I need to go to the bathroom"))

    # GRID LAYOUT SECTION 
    grid_layout.setContentsMargins(20, 20, 20, 20)
    grid_layout.setSpacing(15)

    grid_layout.addWidget(yes_btn, 0, 0)
    grid_layout.addWidget(no_btn, 0, 1)
    grid_layout.addWidget(help_btn, 0, 2)

    grid_layout.addWidget(hungry_btn, 1, 0)
    grid_layout.addWidget(thirsty_btn, 1, 1)
    grid_layout.addWidget(bathroom_btn, 1, 2)

    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    App()