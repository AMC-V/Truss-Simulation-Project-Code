from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

if __name__ == "__main__":
    print("we are runnning the simply gui currently")


class MyWindow(QMainWindow): # Here we are creating our own class and inheriting from the QMainWindow Class so getting all its methods for use to use
    def __init__(self): # here we create the constructor for the class, where self represents the class, so an attriubles added to the self are bascially added to the class, each clas gets a unique self
        super().__init__() # here we call the constructor of the parent cass, which returns a object from the class
        self.setGeometry(500, 500, 100, 300)
        self.setWindowTitle("Testing title")
        self.startMainWindow() # call the method that actaully does cool stuff
        
    def startMainWindow(self):
        self.primaryWidget = QWidget() # a blank widget that will only hold the primary layout for widgets        
        self.primaryLayout = QHBoxLayout() # As we add stuff it will be placed horizatonally
        
        self.label_1 = QLabel("label 1")
        self.label_1.setStyleSheet("background-image: none")
        
        self.primaryLayout.addWidget(self.label_1)
        
        self.secondaryWidget_1 = QWidget() # a blank widget that will only hold the secondary layout for widgets
        self.secondaryLayout_1 = QVBoxLayout() # As we add stuff it will be placed veritally
        
        self.label_2 = QLabel("label 2")
        self.label_2.setStyleSheet("background-image: url(anime1.jpg);")
        self.label_2.setAlignment(Qt.AlignCenter)
        
        self.label_3 = QLabel("label 3")
        self.label_3.setStyleSheet("background-image: url(anime2.jpg);")
        
        self.button = QPushButton("Press")
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.textbox = QTextEdit()
        
        self.secondaryLayout_1.addWidget(self.label_2)
        self.secondaryLayout_1.addWidget(self.label_3)
        self.secondaryLayout_1.addWidget(self.button)
        self.secondaryLayout_1.addWidget(self.textbox)
        
        self.secondaryWidget_1.setLayout(self.secondaryLayout_1)
        
        self.primaryLayout.addWidget(self.secondaryWidget_1)
        
        self.primaryWidget.setLayout(self.primaryLayout) # holder
        self.setCentralWidget(self.primaryWidget)

def window(): # function to create content
    app = QApplication([]); # initialize 
    app.setStyleSheet("""
                      QWidget {font-family: Times New Roman;
                      font-size: 100px;
                      color: black;}
                      
                      QMainWindow{background-image: url(satsuki.jpg);
                      background-color: #161219;}
                      
                      QLabel {background-color:red;
                      
                      qproperty-alignment: AlignCenter;}
                      
                      QPushButton{background-color: #BC006C;
                      border-color: #7581a1;
                      border-style: outset;
                      border-width: 1px;
                      border-radius: 10px;
                      font: bold 100px;
                      min-width: 5em;
                      max-width: 7em;}
                      
                      QPushButton::hover{background-color: #7581a1;}
                      
                      QTextBox{color: white;
                      padding: 50px;
                      border-color: white; 
                      border-style: outset;
                      border-width: 1px;
                      border-radius: 10px;
                      background-color: black;
                      selection-color: black;
                      selection-background-color: white;
                      max-width: 7em;}
                      """)
    
    mainWindow = MyWindow()
    
    mainWindow.show()
    
    sys.exit(app.exec())
    
window()