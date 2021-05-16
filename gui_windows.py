import PyQt5.QtWidgets as wid
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from file_interactions import *

from time_counter import *
import sys




class Menu_Screen(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.resize(1000,500)
        
        HEADING_FONT = QFont('Ariel', 36)
        
        win = wid.QWidget()
        grid = wid.QGridLayout()
        win.setLayout(grid)
        
        title = wid.QLabel("Finding friends")
        title.setFont(HEADING_FONT)
        grid.addWidget(title,1,1,1,1)
        
        starting_button = wid.QPushButton('Start')
        starting_button.clicked.connect(self.start_game)
        grid.addWidget(starting_button,2,1,1,1)

        click_me_button = wid.QPushButton("Click me!")
        click_me_button.clicked.connect(self.information)
        grid.addWidget(click_me_button,2,2,1,1,)

        self.setLayout(grid)   
        self.show()
    
    def start_game(self):
        self.start = Game_screen()
        self.start.show()
        self.close()

    def information(self):
        self.start = information()
        self.start.show()
        



class Game_screen(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.resize(1000,500)
        self.conversation_counter = 0
        self.playing_layout()
        
        self.show()
        
    def playing_layout(self):

        dialoguebutton_1 = wid.QPushButton(current_dialogue[0])
        dialoguebutton_2 = wid.QPushButton(current_dialogue[1])
        dialoguebutton_3 = wid.QPushButton(current_dialogue[2])
        


        self.container = wid.QGridLayout()
        
        self.picture_raw = QPixmap('tester.jpg')
        self.picture_resized = self.picture_raw.scaled(500, 450, Qt.KeepAspectRatio)
        self.picture_final = wid.QLabel()
        self.picture_final.setPixmap(self.picture_resized)
        self.container.layout().addWidget(self.picture_final)


        self.character_dialogue = wid.QLabel(chosen_question)
        self.container.layout().addWidget(self.character_dialogue) 



        self.dialogue_container = wid.QWidget()
        self.dialogue_container.setLayout(wid.QVBoxLayout())
        
        self.top_row = wid.QWidget()
        self.top_row.setLayout(wid.QGridLayout())
        self.top_row.layout().addWidget(dialoguebutton_1,1,1,1,1)
        
        self.dialogue_container.layout().addWidget(self.top_row)

            
        self.middle_row = wid.QWidget()
        self.middle_row.setLayout(wid.QGridLayout())
        self.middle_row.layout().addWidget(dialoguebutton_2,1,1,1,1)
        
        self.dialogue_container.layout().addWidget(self.middle_row)
        
        self.bottom_row = wid.QWidget()
        self.bottom_row.setLayout(wid.QGridLayout())
        self.bottom_row.layout().addWidget(dialoguebutton_3,1,1,1,1)
        
        self.dialogue_container.layout().addWidget(self.bottom_row)

        self.container.layout().addWidget(self.dialogue_container)
        self.setLayout(self.container)


        
    

class information(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Information")
        
        layout = wid.QVBoxLayout()

        with open("inprogramdoc.txt", "r") as document_text:
            content = wid.QLabel(document_text.read())
        layout.addWidget(content)

        self.setLayout(layout)
        self.show()



app = wid.QApplication([])
mw = Menu_Screen()
app.exec_()
