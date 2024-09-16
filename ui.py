from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QMessageBox,
                             QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1 = QPushButton("Message", self)
        # self.btn1.clicked.connect(self.activateMessage)
        self.btn2 = QPushButton("clear", self)
        # self.btn2.clicked.connect(self.clearMessage)
        
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.te1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        # self.setLayout(hbox)
        
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(2**8, 2**8)
        self.show()
        
    def activateMessage(self):
        #QMessageBox.information(self,"information", "Button clicked!")
        self.te1.appendPlainText("Button clicked")
        
    def clearMessage(self):
        self.te1.clear()
        