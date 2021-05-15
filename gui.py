import PyQt5.QtWidgets as wid
from PyQt5.QtGui import QPixmap 
import sys
class MainWindow(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.setLayout(wid.QVBoxLayout())
        self.resize(1000,500)
        self.playing_layout()
        self.show()
        
    def playing_layout(self):
        dialoguebutton_1 = wid.QPushButton("sample text1")
        dialoguebutton_2 = wid.QPushButton("sample text2")
        dialoguebutton_3 = wid.QPushButton("sample text3")
        


        self.container = wid.QWidget()
        self.container.setLayout(wid.QGridLayout())

        pixmap2 = QPixmap('tester.jpg')
        self.image2 = wid.QLabel(self.container)
        self.image2.setPixmap(pixmap2)



            
        self.top_row = wid.QWidget()
        self.top_row.setLayout(wid.QHBoxLayout())
        self.top_row.layout().addWidget(dialoguebutton_1)
        
        self.container.layout().addWidget(self.top_row)

            
        self.middle_row = wid.QWidget()
        self.middle_row.setLayout(wid.QHBoxLayout())
        self.middle_row.layout().addWidget(dialoguebutton_2)
        
        self.container.layout().addWidget(self.middle_row)
        
        self.bottom_row = wid.QWidget()
        self.bottom_row.setLayout(wid.QHBoxLayout())
        self.bottom_row.layout().addWidget(dialoguebutton_3)
        
        self.container.layout().addWidget(self.bottom_row)
        
        self.layout().addWidget(self.container)



app = wid.QApplication([])
mw = MainWindow()
app.exec_()
