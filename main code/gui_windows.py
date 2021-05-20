import PyQt5.QtWidgets as wid
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from file_interactions import *
from character_interaction import *
import sys



#The class for the main menu screen of the game. Is called on by default 
class Menu_Screen(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.setFixedSize(850,650)
        self.heading_font_size = 36
        self.subheading_font_size = 20
        self.normal_font_size = 11
        
        #Basic functions
        HEADING_FONT = QFont('Ariel', self.heading_font_size)
        SUBHEADING_FONT = QFont('Ariel', self.subheading_font_size)
        NORMAL_FONT = QFont('Ariel', self.normal_font_size)
        win = wid.QWidget()
        grid = wid.QGridLayout()
        win.setLayout(grid)
        
        #Title label
        self.title = wid.QLabel("Finding friends")
        self.title.setFont(HEADING_FONT)
        grid.addWidget(self.title,0,1,1,3)

        #Font size increase button
        self.font_up = wid.QPushButton("Larger font")
        self.font_up.setFont(NORMAL_FONT)  
        self.font_up.clicked.connect(self.font_big)
        grid.addWidget(self.font_up,0,4,1,1)

        #Font size decrease button
        self.font_down = wid.QPushButton("Smaller font")
        self.font_down.setFont(NORMAL_FONT)  
        self.font_down.clicked.connect(self.font_small)
        grid.addWidget(self.font_down,0,5,1,1)

        #Subheading 
        self.subtext = wid.QLabel("Before starting, please click the information button")
        self.subtext.setFont(SUBHEADING_FONT)
        grid.addWidget(self.subtext,3,1,1,4)
        

        #Button to start the main game interface
        self.starting_button = wid.QPushButton('Start')
        self.starting_button.setFont(NORMAL_FONT)
        self.starting_button.clicked.connect(self.start_game)        
        grid.addWidget(self.starting_button,4,1,1,1)

        #Button to display information about the software and the EULA
        self.click_me_button = wid.QPushButton("Information")
        self.click_me_button.setFont(NORMAL_FONT)
        self.click_me_button.clicked.connect(self.information)
        grid.addWidget(self.click_me_button,4,2,1,1)
        
        #Initiates the software 
        self.setLayout(grid)   
        self.show()
    
    #Function to start the game window
    def start_game(self):
        self.start = Game_screen(self.normal_font_size)
        self.start.show()
        self.close()
    
    #Function to open the information window
    def information(self):
        self.start = information()
        self.start.show()
    
    #Function to increase font size 
    def font_big(self):
        if self.heading_font_size >= 60:
            pass
        if self.subheading_font_size >= 48:
            pass
        if self.normal_font_size >= 36:
            pass
        else:
            self.heading_font_size = self.heading_font_size + 5
            self.subheading_font_size = self.subheading_font_size + 5 
            self.normal_font_size = self.normal_font_size + 5
            self.click_me_button.setFont(QFont('Ariel', self.normal_font_size))
            self.starting_button.setFont(QFont("Ariel", self.normal_font_size))
            self.title.setFont(QFont('Ariel', self.heading_font_size))
            self.font_up.setFont(QFont('Ariel', self.normal_font_size))
            self.font_down.setFont(QFont('Ariel', self.normal_font_size))
            self.subtext.setFont(QFont('Ariel', self.subheading_font_size))
    
    #Function to decrease font size 
    def font_small(self):
        if self.heading_font_size <= 20:
            pass
        if self.subheading_font_size <= 8:
            pass
        if self.normal_font_size <= 2:
            pass
        else:
            self.heading_font_size = self.heading_font_size - 3
            self.subheading_font_size = self.subheading_font_size - 3 
            self.normal_font_size = self.normal_font_size - 3 
            self.click_me_button.setFont(QFont('Ariel', self.normal_font_size))
            self.starting_button.setFont(QFont("Ariel", self.normal_font_size))
            self.title.setFont(QFont('Ariel', self.heading_font_size))
            self.font_up.setFont(QFont('Ariel', self.normal_font_size))
            self.font_down.setFont(QFont('Ariel', self.normal_font_size))
            self.subtext.setFont(QFont('Ariel', self.subheading_font_size))

        


#The main game interaction screen 
class Game_screen(wid.QWidget):
    def __init__(self, normal_size):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.resize(1000,500)
        self.conversation_counter = 0
        self.font_size = normal_size


        self.container = wid.QGridLayout()

        #Processing the image for the character
        self.picture_raw = QPixmap('tester.jpg')
        self.picture_resized = self.picture_raw.scaled(500, 450, Qt.KeepAspectRatio)
        self.picture_final = wid.QLabel()
        self.picture_final.setPixmap(self.picture_resized)
        self.container.layout().addWidget(self.picture_final,0,1,1,1)
        

        self.used_questions = []
        self.button_setup()
        
        
        self.setLayout(self.container)
    
        
        self.show()
        

        
    def button_setup(self):    
        
        
        self.dialogue_object = Questions(self.used_questions)
        
        #Using the file interaction functions to use the text labels
        self.dialogue_questions =  self.dialogue_object.question_list #These variables need to be interated throuhg a for loop        
        self.chosen_question = self.dialogue_object.selected_question
        self.current_dialogue = self.dialogue_object.dialogue_options
        self.used_questions.append(self.chosen_question)

        
        #Establishing the buttons 
        dialoguebutton_1 = wid.QPushButton(self.current_dialogue[0])
        dialoguebutton_2 = wid.QPushButton(self.current_dialogue[1])
        dialoguebutton_3 = wid.QPushButton(self.current_dialogue[2])

        #Button fonts 
        dialoguebutton_1.setFont(QFont("Ariel", self.font_size))
        dialoguebutton_2.setFont(QFont("Ariel", self.font_size))
        dialoguebutton_3.setFont(QFont("Ariel", self.font_size))

        dialoguebutton_1.clicked.connect(self.button_press)
        dialoguebutton_2.clicked.connect(self.button_press)
        dialoguebutton_3.clicked.connect(self.button_press)

        #Displaying the dialogue button 
        self.character_dialogue = wid.QLabel(self.chosen_question)
        self.character_dialogue.setFont(QFont("Ariel", self.font_size))
        self.container.layout().addWidget(self.character_dialogue,1,1,3,3) 

        self.dialogue_container = wid.QWidget()
        self.dialogue_container.setLayout(wid.QVBoxLayout())
        
        #Placing the buttons in their correct layout position
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

        self.container.layout().addWidget(self.dialogue_container,2,2,1,1)
        
    #Function that removes the buttons and replaces with pure dialogue
    def button_press(self):

        self.conversation_counter = self.conversation_counter + 1
        if self.conversation_counter%2 == 1:
            self.dialogue_container.deleteLater()
            self.character_dialogue.setText("Thats cool")
            self.next_button = wid.QPushButton("Next")
            self.next_button.setFont(QFont("Ariel", self.font_size))
            self.next_button.clicked.connect(self.moveon)
            self.container.layout().addWidget(self.next_button,4,1,1,1)


    #Changes the interface back to the dialogue options, ends if the conversation limit was reached
    def moveon(self):
        self.conversation_counter = self.conversation_counter + 1
        print(self.conversation_counter)
        if self.conversation_counter == 8:
            self.used_questions.clear()
            self.close()
        if self.conversation_counter%2 == 0:
            self.next_button.deleteLater()
            self.character_dialogue.deleteLater()
            self.button_setup()

#Information class
class information(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Information")
        self.setFixedSize(800, 800)

        
        layout = wid.QVBoxLayout()
        #Reading the text file containing the content
        with open("inprogramdoc.txt", "r") as document_text:
            content = wid.QLabel(document_text.read())
        layout.addWidget(content)

        self.setLayout(layout)
        self.show()



