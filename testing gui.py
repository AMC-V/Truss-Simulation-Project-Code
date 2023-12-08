from PyQt5 import QtGui
import sys

def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    w.setText("Hello bitch")
    w.setGeometry(100,100,200,50)
    b.move(50,20)
    w.setWindowTitle("BAD BITCH")
    w.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    window()
    