import PyQt5.QtWidgets as wid

class MainWindow(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(wid.QVBoxLayout())
        self.dialoguelayout()
        self.show()
        
    def dialoguelayout(self):
        container = wid.QWidget()
        container.setLayout(wid.QGridLayout())
        
        dialoguebutton_1 = wid.QPushButton("sample text1")
        dialoguebutton_2 = wid.QPushButton("sample text2")
        dialoguebutton_3 = wid.QPushButton("sample text3")
        
        container.layout().addWidget(dialoguebutton_1,3,2,1,6)
        container.layout().addWidget(dialoguebutton_2,4,2,1,6)
        container.layout().addWidget(dialoguebutton_3,5,2,1,6)
        
        self.layout().addWidget(container)
        

app = wid.QApplication([])
mw = MainWindow()
app.exec_()
