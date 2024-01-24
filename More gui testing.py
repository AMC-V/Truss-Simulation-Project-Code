from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

# REMEBER TO ALWAYS TEST ON SIMPLY THINGS BEFORE GOING TO THE VERY COMPLICATED

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mainWidget = QWidget() # The placeholder for the mainLayout
        # remember to modifiy the mainWidget
        
        self.mainHorizationalLayout = QHBoxLayout() # mainLayout, when adding things to it, they will 
                                                    # be added horizationally
        self.mainHorizationalLayout.setSpacing(0)
        self.mainHorizationalLayout.setContentsMargins(5,5,5,5) # look at chatgpt for explaination
        print(self.mainHorizationalLayout.getContentsMargins())
        # Might have to modifty layout here for correct spacing
        
        # first main feature, will appear on leftside
        self.welcomeMessage = QLabel("HELLO") # created
        self.welcomeMessage.setMaximumSize(408,50)
        self.welcomeMessage.setMinimumSize(408,50)
        self.welcomeMessage.setStyleSheet("border-color: yellow;")
        
        self.mainHorizationalLayout.addWidget(self.welcomeMessage) # added to mainLayout, DONE HERE  !!!!!!!!!!!
        
        # second main feature, will appear on leftside
        self.welcomeMessage1 = QLabel("HELLO A SECOND TIME") # created
        self.welcomeMessage1.setMaximumSize(408,50) # also min
        self.welcomeMessage1.setMinimumSize(408,50) # by doing this we overwrite the og SizeHint
        self.welcomeMessage1.setStyleSheet("border-color: blue;")
        
        self.mainHorizationalLayout.addWidget(self.welcomeMessage1) # added to mainLayout, DONE HERE  !!!!!!!!!!!
        print(self.welcomeMessage1.minimumSizeHint()) # intreseting changes
        
        # end of first two main features
        self.mainHorizationalLayout.setAlignment(self.welcomeMessage, Qt.AlignCenter)
        self.mainHorizationalLayout.setAlignment(self.welcomeMessage1, Qt.AlignCenter)
        
        # third main feature, will appear on middle
        self.scroll = QScrollArea() # Scroll Area which contains the button widgets
        self.scroll.setStyleSheet("border-color:white;") # both widget and scroll have there own independent borders
        # scroll is like a mini canvas, and when you setWigdet it's the same effect as setCentralWidget
        
        self.widget = QWidget()     # The placeholder for the vbox
        
        
        self.vbox = QVBoxLayout()   # vbox, when adding things to it, they will 
                                    # be added vertically, should be able to add things afterthefact
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0,0,0,0)                            
        # Might have to modifty layout here for correct spacing
                                    
        for i in range(1,5):
            object = QPushButton(f"TextLabel {i}") # create generic labels NOT stored in self
            object.setMinimumHeight(50)
            
            #min-width: 6em;
            #max-height: 0.7em;
            
            self.vbox.addWidget(object) # added label to layout
            self.vbox.setAlignment(object, Qt.AlignCenter)

        self.widget.setLayout(self.vbox) # when done add layout to a widget, completed everything we wanted

        #Scroll Area Properties
        #self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        
        self.scroll.setWidget(self.widget) # add widget to the scrollArea
        self.mainHorizationalLayout.addWidget(self.scroll) # added to mainLayout, DONE HERE !!!!!!!!!!!
        
        # Finishing up
        self.mainWidget.setLayout(self.mainHorizationalLayout)
        
        self.setCentralWidget(self.mainWidget) # make mainWidget the centerpiece, YAHHHHHHHHHHHHH
        
        self.widget.setStyleSheet("border-color: red;") # -color: yellow
        
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()
        return

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.setStyleSheet("""
                        QWidget {font-family: Times New Roman;
                        font-size: 50px;
                        color: white;
                        background-color: #161219;
                        border-color: #a868d9;
                        border-style: outset;
                        border-width: 5px;
                        border-radius: 10px;}
                        
                        QScrollBar {
                            color: red;}
                        
                        QLabel {font-size: 35px;
                        padding: 0px;
                        spacing: 0px;
                        background-color: darkgreen;
                        selection-color: black;
                        selection-background-color: white;}
                                                
                        QPushButton{background-color: black;
                        font: bold 35px;}
                      
                        QPushButton::hover{background-color: #734c91;}
                        """)
    
    print(main.welcomeMessage1.minimumSizeHint()) # correct
    print(main.mainHorizationalLayout.getContentsMargins())
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()