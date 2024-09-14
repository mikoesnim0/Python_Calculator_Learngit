import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Calclator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculator")
        self.resize(2**8, 2**8)
        self.show()
        

if __name__ =="__main__":
    app=QApplication(sys.argv)
    view=Calclator()
    sys.exit(app.exec_())