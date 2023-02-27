from PyQt6.QtWidgets import QPushButton,QApplication,QWidget,QMenu 
import sys 
from PyQt6.QtCore import QSize

from PyQt6.QtGui import QIcon ,QFont


class Window(QWidget) : 
    def __init__(self) : 
        super().__init__()
        self.setGeometry(200,100,315,500)
        self.setWindowTitle('app design')
        self.setWindowIcon(QIcon('gpt.png'))
        self.createButton()
    def createButton(self) : 
        btn = QPushButton('Click',self)
        btn.setGeometry(100,100,105,40)
        btn.setFont(QFont("Times",14))
        btn.setIcon(QIcon('gpt.png'))
        btn.setIconSize(QSize(36,36))

        menu = QMenu() 
        menu.setFont(QFont("Times",14))
        menu.setStyleSheet("background-color : green;width:100px;")
        
        menu.addAction('Copy')
        menu.addAction('Cut')
        menu.addAction('Past')
        btn.setMenu(menu)

       
 


app = QApplication(sys.argv) 

win = Window() 
win.show() 
sys.exit(app.exec())

