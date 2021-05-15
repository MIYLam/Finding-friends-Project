import PyQt5.QtWidgets as wid
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import sys
class MainWindow(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.resize(1000,500)
        self.playing_layout()
        self.show()
        
    def playing_layout(self):
        dialoguebutton_1 = wid.QPushButton("sample text1")
        dialoguebutton_2 = wid.QPushButton("sample text2")
        dialoguebutton_3 = wid.QPushButton("sample text3")
        
        self.container = wid.QGridLayout()
        
        self.picture_raw = QPixmap('tester.jpg')
        self.picture_resized = self.picture_raw.scaled(500, 450, Qt.KeepAspectRatio)
        self.picture_final = wid.QLabel()
        self.picture_final.setPixmap(self.picture_resized)

        self.container.layout().addWidget(self.picture_final)

        self.character_dialogue = wid.QLabel("please work")
        self.container.layout().addWidget(self.character_dialogue) 

      
        self.top_row = wid.QWidget()
        self.top_row.setLayout(wid.QGridLayout())
        self.top_row.layout().addWidget(dialoguebutton_1,1,1,1,1)
        
        self.container.layout().addWidget(self.top_row)

            
        self.middle_row = wid.QWidget()
        self.middle_row.setLayout(wid.QGridLayout())
        self.middle_row.layout().addWidget(dialoguebutton_2,1,1,1,1)
        
        self.container.layout().addWidget(self.middle_row)
        
        self.bottom_row = wid.QWidget()
        self.bottom_row.setLayout(wid.QGridLayout())
        self.bottom_row.layout().addWidget(dialoguebutton_3,1,1,1,1)
        
        self.container.layout().addWidget(self.bottom_row)

        self.setLayout(self.container)
        




app = wid.QApplication([])
mw = MainWindow()
app.exec_()
