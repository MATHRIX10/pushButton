from PyQt6.QtWidgets import QApplication, QWidget,QLabel  ,QVBoxLayout,QHBoxLayout,QListWidget,QPushButton,QLineEdit
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize ,QTime,QTimer,Qt

import sys 
from random import randint 

class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,500,200)
        self.setWindowTitle('radio button ')
        self.setWindowIcon(QIcon('gpt.png'))
        vbox = QVBoxLayout()
        self.list_widgets = QListWidget() 
        self.list_widgets.insertItem(0,"Pyhton")
        self.list_widgets.insertItem(1,"Java")
        self.list_widgets.insertItem(2,"C++")
        self.list_widgets.insertItem(3,"Rust")
        self.list_widgets.setFont(QFont("Times New Roman",15))
        self.list_widgets.setStyleSheet('background : #323232;color:#eee')
        self.list_widgets.itemSelectionChanged.connect(self.items_list)
        self.label = QLabel('')
        self.label.setFont(QFont('Times New Roman',15))
        self.button = QPushButton('add',self) 
        self.button.clicked.connect(self.add)
        self.ipt = QLineEdit() 
        hbox = QHBoxLayout() 
        hbox.addWidget(self.ipt)
        hbox.addWidget(self.button)


        vbox.addWidget(self.list_widgets)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def items_list(self) : 
        item = self.list_widgets.currentItem() 
        self.label.setText(str(item.text()))
    def add(self) : 
        item = self.ipt.text() 
        self.list_widgets.addItem(item)
        self.ipt.setText('')

            
app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())
