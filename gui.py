import PyQt5.QtWidgets as wid

class MainWindow(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finding friends")
        self.setLayout(wid.QVBoxLayout())
        self.resize(1000,500)
        self.dialoguelayout()
        self.show()
        
    def dialoguelayout(self):
        self.container = wid.QWidget()
        self.container.setLayout(wid.QGridLayout())
        
        dialoguebutton_1 = wid.QPushButton("sample text1")
        dialoguebutton_2 = wid.QPushButton("sample text2")
        dialoguebutton_3 = wid.QPushButton("sample text3")
        
        self.container.layout().addWidget(dialoguebutton_1,3,2,1,6)
        self.container.layout().addWidget(dialoguebutton_2,4,2,1,6)
        self.container.layout().addWidget(dialoguebutton_3,5,2,1,6)
        
        self.layout().addWidget(self.container)



app = wid.QApplication([])
mw = MainWindow()
app.exec_()
