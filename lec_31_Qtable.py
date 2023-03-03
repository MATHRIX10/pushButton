from PyQt6.QtWidgets import QApplication, QWidget,QLabel  ,QVBoxLayout,QHBoxLayout,QTableWidgetItem,QTableView,QTableWidget
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize ,QTime,Qt

import sys 
from random import randint 

class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,500,200)
        self.setWindowTitle('radio button ')
        self.setWindowIcon(QIcon('gpt.png'))
        vbox = QVBoxLayout() 
        table = QTableWidget() 
        table.setRowCount(3)
        table.setColumnCount(3)

        table.setItem(0,0,QTableWidgetItem("Name"))
        table.setItem(0,1,QTableWidgetItem('email'))
        table.setItem(0,2,QTableWidgetItem('Phone'))

        table.setItem(1,0,QTableWidgetItem("Rachid"))
        table.setItem(1,1,QTableWidgetItem('rachid@outlook.com'))
        table.setItem(1,2,QTableWidgetItem('+14383571667'))

        table.setItem(2,0,QTableWidgetItem("Med"))
        table.setItem(2,1,QTableWidgetItem('med@outlook.com'))
        table.setItem(2,2,QTableWidgetItem('+1437656453'))
        vbox.addWidget(table)
        self.setLayout(vbox)











app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())