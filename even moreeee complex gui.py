from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow): # Class that will create UI, will inhertant all the methods from QMainWindow
    def __init__(self): # The constructor for this class that will always be called when first created
        super().__init__() # Call the constructor of the parent clas and return a object of the parent
        self.setGeometry(0, 0, 1000, 1000) # Set spawn position of window and inital size
        self.setWindowTitle("INSIGHT")
        self.createWindow() # In constructor call another method
        
    def createWindow(self):
        # region Window Widget and Layout Creation
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.canvas = QWidget() # a blank widget that will only hold the main layout for widgets, gets color from stylesheet     
        self.mainLayout = QHBoxLayout() # As we add stuff it will be placed horizatonally
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window Content
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # region Main Force Section
        #========================================
        # region Main Force Section Widget and Layout Creation
        #----------------------------------------
        # The Second Main Struture
        self.forceContainer = QGroupBox("Forces") # Contains all force related things, will contain the forceLayout
        self.forceContainer.setFixedWidth(550) # Has same coloring as MainWindow Widget
        
        # The Second Main Layout
        self.forceLayout = QVBoxLayout()  # Every Primary Widget will be added here, goes downwards, three Primaries Note and Response
        self.forceLayout.setSpacing(4) # The space inbetween widgets in the force layout
        self.forceLayout.setContentsMargins(6,0,6,6) # The space inbetween the ends of the groupbox and the widgets inside
        #----------------------------------------
        # endregion
        
        # region Main Force Section Content
        #----------------------------------------
        # region Primary Force Note
        #****************************************
        self.createInfoLabel("Enter a force as magnitude,angle.") # Creates a widget called noteCotainer 
        #****************************************
        # endregion
            
        # region Primary Force Response
        #****************************************
        # region Primary Force Response Widget and Layout Creation
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # The Force Response Main Struture
        self.forceResponseContainer = QFrame() # Contains all the reponses and heading, will contain the forceResponseLayout
        # QFrame has black as background coloring with layout having no color

        # The Force Response Main Layout
        self.forceResponseLayout = QVBoxLayout() # Every Major Widget will be added here, goes downwards, three Major Widgets Label, Input Area, and Next button
        self.forceResponseLayout.setSpacing(0)
        self.forceResponseLayout.setContentsMargins(0,0,0,6)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Force Response Content
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # region Major Force Label 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Force Label Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Force Label Main Struture
        self.forceLabelContainer = QWidget() # Contains all the info labels, will contain the forceLabelLayout
        self.forceLabelContainer.setStyleSheet("background-color: rgba(0,0,0,0);")
        
        # The Force Label Main Layout
        self.forceLabelLayout = QHBoxLayout() # Every Minor Widget will be added here, goes sideways, two Minor Widgets Force and Symmetric, formatting
        self.forceLabelLayout.setSpacing(0) 
        self.forceLabelLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Label Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Minor Widgets
        self.forceLabel = QLabel("Force")
        self.forceLabel.setStyleSheet("""
                                       min-width: 3.8em;
                                       max-width: 3.8em;
                                       
                                       background-color: rgba(0,0,0,0);""")
        
        self.forceSymmetricLabel = QLabel("Symmetric")
        self.forceSymmetricLabel.setStyleSheet("""
                                       min-width: 4em;
                                       max-width: 4em;
                                    
                                       background-color: rgba(0,0,0,0);""")
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Label Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Force Label Main Layout
        self.forceLabelLayout.addWidget(self.forceLabel)
        self.forceLabelLayout.addWidget(self.forceSymmetricLabel)
        
        self.forceLabelLayout.setAlignment(self.forceLabel, Qt.AlignLeft)
        self.forceLabelLayout.setAlignment(self.forceSymmetricLabel, Qt.AlignCenter)

        # Setting the Force Label Main Layout to the Force Label Main Struture
        self.forceLabelContainer.setLayout(self.forceLabelLayout)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
        
        # region Major Force Input Area 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Force Input Area Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # The Force Input Area Main Struture
        self.forceInputScorllArea = QScrollArea() # Controls the Scroll Area for the Widget that contains all the inputs
        self.forceInputScorllArea.setWidgetResizable(True)
        self.forceInputScorllArea.setMinimumHeight(45)
        self.forceInputScorllArea.setStyleSheet("""background-color: black;
                                                border-color: rgba(0,0,0,0);""")
        
        # The Force Input Area Main Sub-Struture
        self.forceInputScrollAreaWidget = QWidget() # Widget that will hold all inputs, will be the central widget for forceInputScrollArea, will contain the forceInputScrollAreaWidgetLayout
        self.forceInputScrollAreaWidget.setContentsMargins(0,0,0,0)
        self.forceInputScrollAreaWidget.setStyleSheet("""background-color: rgba(0,0,0,0);
                                   border: none;""")
        
        # The Force Input Area Main Sub-Layout
        self.forceInputScrollAreaWidgetLayout = QVBoxLayout() # Every addition input will be added here, Minor Widget will be added here, goes downwards, one Minor Widget Input, non formatting
        self.forceInputScrollAreaWidgetLayout.setSpacing(0)
        self.forceInputScrollAreaWidgetLayout.setContentsMargins(0,0,0,0)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Input Area Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # region Minor Force Input 
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # region Minor Force Input Widget and Layout Creation
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # The Force Input Main Struture
        self.forceInputContainer = QWidget() # Contains input, will contain the forceInputLayout, add to forceInputScrollAreaWidgetLayout once done

        #The Force Input Main Layout
        self.forceInputLayout = QHBoxLayout() # Every Tiny Widget will be added here, goes sideways, formatting
        self.forceInputLayout.setSpacing(0)
        self.forceInputLayout.setContentsMargins(0,0,0,3)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Force Input Content
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Tiny Widgets
        self.genericInput = QLineEdit()
        self.genericInput.setAlignment(Qt.AlignCenter)
        self.genericInput.setStyleSheet("background-color: white;")
        
        self.symmetric = QCheckBox()
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        
        # region Minor Force Input addition and layout
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Adding Tiny to The Force Input Main Layout
        self.forceInputLayout.addWidget(self.genericInput)
        self.forceInputLayout.addWidget(self.symmetric)
        
        self.forceInputLayout.setAlignment(self.genericInput, Qt.AlignCenter)
        self.forceInputLayout.setAlignment(self.symmetric, Qt.AlignCenter)

        # Setting the Force Input Main Layout to the Force Input Main Struture
        self.forceInputContainer.setLayout(self.forceInputLayout)
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # endregion
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # endregion
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Force Input Area Content addition and layout
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # Adding Minor to Force Input Area Main Sub-Layout
        self.forceInputScrollAreaWidgetLayout.addWidget(self.forceInputContainer)
        
        # Setting the Force Input Area Main Sub-Layout to the Force Input Area Main Sub-Struture
        self.forceInputScrollAreaWidget.setLayout(self.forceInputScrollAreaWidgetLayout)
        
        # Setting the Force Input Area Main Sub-Struture to the Force Input Area Main Struture
        self.forceInputScorllArea.setWidget(self.forceInputScrollAreaWidget)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion
              
        # region Major Next Force Button 
        #++++++++++++++++++++++++++++++++++++++++
        # region Major Next Force Button Widget and Layout Creation
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # None needed since it will be added to bottom and centered 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Next Force Button Content
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.nextForceButton = QPushButton()
        self.nextForceButton.setText("Next >>>")
        self.nextForceButton.clicked.connect(lambda: onClickNext(self))
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        
        # region Major Add Force Button addition and actualization
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # none needed since already widget and so will be added directly to forceResponseLayout 
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # endregion
        #++++++++++++++++++++++++++++++++++++++++
        # endregion     
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion 
        
        # region Primary Force Response Content addition and Actualization
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Adding Major to Force Response Main Layout
        self.forceResponseLayout.addWidget(self.forceLabelContainer)
        self.forceResponseLayout.addWidget(self.forceInputScorllArea)
        self.forceResponseLayout.addWidget(self.nextForceButton)
        
        self.forceResponseLayout.setAlignment(self.nextForceButton, Qt.AlignCenter)
        
        # Setting the Force Response Main Layout to the Force Response Main Struture
        self.forceResponseContainer.setLayout(self.forceResponseLayout) 
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # endregion
        #****************************************
        # endregion 
        #----------------------------------------
        # endregion
        
        # region Main Force Section addition and layout
        #----------------------------------------
        # Adding Primary to Second Main Layout
        self.forceLayout.addWidget(self.noteContainer) 
        self.forceLayout.addWidget(self.forceResponseContainer)
        
        # Setting the Second Main Layout to the Second Main Struture
        self.forceContainer.setLayout(self.forceLayout) 
        #----------------------------------------
        # endregion
        #========================================
        # endregion 
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
        
        # region Window addition, layout, and Actualization
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.mainLayout.addWidget(self.forceContainer)
        
        self.canvas.setLayout(self.mainLayout) 
        
        self.setCentralWidget(self.canvas)
        #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # endregion
             
    def createInfoLabel(self, message):
        self.noteContainer = QFrame() # To get outline of note
        self.noteContainer.setFixedHeight(100) # On frame min and max
        self.noteLayout = QVBoxLayout() # Add things up to down
        self.noteLayout.setSpacing(0)

        self.note = QLabel("Note:") # look at master style sheet
        self.note.setStyleSheet("qproperty-alignment: AlignLeft;")
        
        self.genericInfo = QLabel(message) # look at master style sheet
        # by default Q label text is centered in master style sheet
        
        self.noteLayout.addWidget(self.note)
        self.noteLayout.addWidget(self.genericInfo)
        
        self.noteContainer.setLayout(self.noteLayout) # returns this, to be added to layout
        
    def createMinorForceResponse(self, number):
        print(number)        
        
def onClickNext(self):    
    # call method
    self.createMinorForceResponse(len(self.list_of_widgets))
       
    self.list_of_widgets.append(1)
    
    self.repaint()
                
class UI(): # This class will hold the method that will be called in a different file to start UI
    def start():
        App = QApplication([]) # Start up the UI system
        
        # This will set the default style for all widgets created in this window QCheckBox::indicator:checked{background-color: lightgreen; color : black;}
        App.setStyleSheet("""
                        QWidget {font-family: Times New Roman;
                        font-size: 50px;
                        color: black;}
                        
                        QMainWindow{background-color: #161219;}
                        
                        QCheckBox::indicator:unchecked:hover{background-color: rgba(0,255,0, 75);}
                        
                        QCheckBox::indicator:checked:hover{background-color: rgba(255,0,0,100);}
                        
                        QCheckBox::indicator:checked:pressed{background-color: rgba(255,0,0,100);}
                        
                        QRadioButton::indicator:unchecked:hover{background-color: rgba(255,0,0,100);}
                        
                        QFrame{border: 1px;
                        border-radius: 25px;
                        border-color: white;
                        border-style: solid;
                        background-color: black;
                        min-width: 8.75em;}
                        
                        QLabel {color: white;
                        font-size: 35px;
                        padding: 0px;
                        spacing: 0px;
                        border: none;
                        background-color: black;
                        selection-color: black;
                        selection-background-color: white;
                        min-width: 7em;
                        max-height: 1em;
                        min-height: 1em;
                        
                        qproperty-alignment: AlignCenter;}
                        
                        QLineEdit{font-size: 35px;
                        max-width: 5em;
                        max-height: 1em;
                        min-height: 1em;}
                        
                        
                        QPushButton{background-color: black;
                        border-color: #a868d9;
                        border-style: outset;
                        border-width: 1px;
                        border-radius: 10px;
                        font: bold 35px;
                        color: white;
                        min-width: 6em;
                        max-height: 0.7em;
                        min-height: 0.7em;}
                      
                        QPushButton::hover{background-color: #734c91;
                        color: white;}
                        
                        QTextEdit{color: white;
                        font-size: 35px;
                        padding: 10px;
                        border-color: white; 
                        border-style: solid;
                        border-width: 1px;
                        border-radius: 20px;
                        background-color: black;
                        selection-color: black;
                        selection-background-color: white;
                        min-width: 7em;}
                        
                        QGroupBox{color: white;}
                        
                        QScrollBar {color: white;}
                        """)
        
        window = MainWindow() # Create a instance of the MainWindow Class
        window.show()
        
        sys.exit(App.exec())
        
ex = UI.start()