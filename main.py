import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)

class Calclator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.btn1 = QPushButton("Message", self)
        self.btn1.clicked.connect(self.activateMessage)
        self.setWindowTitle("Calculator")
        self.resize(2**8, 2**8)
        self.show()
        
    def activateMessage(self):
        QMessageBox.information(self,"information", "Button clicked!")
        

if __name__ =="__main__":
    app=QApplication(sys.argv)
    view=Calclator()
    sys.exit(app.exec_())