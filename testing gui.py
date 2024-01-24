from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import qdarkstyle
import sys

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    our_layout = QVBoxLayout() # Layout for the main window
    
    window = QWidget()
    window.setWindowTitle("Satsuki!!!!!")
    window.setWindowIcon(QIcon("satsuki.jpg")) #4c658f #636c7a
    window.setGeometry(100, 100, 1200, 300)
    #window.setStyleSheet("background-color: black;")
    window.setStyleSheet("""
                         background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                         stop: 0.2 black, stop: 1 #919fc6);
                         """)
        
    label = QLabel("Enter Data Below")
    label.setFont(QFont("Times New Roman", 20))
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("""
                        background-color: rgba(255, 255, 255, 0); 
                        color: white;
                        max-width: 15em;
                        """)
    
    textbox = QTextEdit()
    textbox.setStyleSheet("""
                          color: white;
                          padding: 50px;
                          font-family: Times New Roman;
                          font-size: 40px;
                          border-color: white; 
                          border-style: outset;
                          border-width: 1px;
                          border-radius: 10px;
                          background-color: black;
                          selection-color: black;
                          selection-background-color: white;
                          max-width: 7em;
                          """)
    
    button = QPushButton("Calculate") #334a7c #7581a1
    button.clicked.connect(lambda: onClick(textbox.toPlainText()))
    button.setStyleSheet("""
                         background-color: #7581a1;
                         border-color: black;
                         border-style: outset;
                         border-width: 1px;
                         border-radius: 10px;
                         color: black;
                         font-family: Times New Roman;
                         font-size: 50px;
                         font: bold 50px;
                         min-width: 5em;
                         max-width: 7em;
                         """)
    
    our_layout.addWidget(label)
    our_layout.addWidget(textbox)
    our_layout.addWidget(button)
    
    window.setLayout(our_layout)
    
    window.show()
    app.exec_()

def onClick(msg):
    onClick_message = QMessageBox()
    onClick_message.setText(msg)
    onClick_message.exec_()

if __name__ == '__main__':
    main()