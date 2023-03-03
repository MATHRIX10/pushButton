from PyQt6.QtWidgets import QPushButton,QApplication, QWidget,QLabel  ,QVBoxLayout,QHBoxLayout,QDialog,QInputDialog,QLineEdit
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize ,QTime,Qt

import sys 
from random import randint 

class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,500,200)
        self.setWindowTitle('Dialog')
        self.setWindowIcon(QIcon('gpt.png'))
        self.create_dialog() 

    def create_dialog(self) :
        font = QFont("Times New Roman",14)
        hbox = QHBoxLayout()
        label = QLabel('choose country')
        label.setFont(font)
        self.input = QLineEdit() 
        btn = QPushButton('set country ')
        btn.clicked.connect(self.show_dialog)
        btn1 = QPushButton('set text ')
        btn1.clicked.connect(self.get_text)
        btn2 = QPushButton('set int ')
        btn2.clicked.connect(self.get_int)
        
        self.input.setFont(font)
        hbox.addWidget(label)
        hbox.addWidget(self.input)
        hbox.addWidget(btn)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)



        self.setLayout(hbox)


    def show_dialog(self) : 
        countries = ['Maroc','Canada','USA','Germany','UK']

        country, ok = QInputDialog.getItem(self,'Input Dialog','list of countries',countries,0,False)

        if ok and country : 
            self.input.setText(country)


    def get_text(self) : 
        text,ok = QInputDialog.getText(self,'get username','enter your name')
        if ok and text : 
            self.input.setText(text)


    def get_int(self) : 
        mynumber , ok = QInputDialog.getInt(self,'Quantity','enter number')
        if mynumber and ok : 
            self.input.setText(str(mynumber))

app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())