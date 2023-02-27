from PyQt6.QtWidgets import QPushButton,QApplication,QWidget,QLineEdit 
import sys 
from PyQt6.QtCore import QSize

from PyQt6.QtGui import QIcon ,QFont


class Window(QWidget) : 
    def __init__(self) : 
        super().__init__()
        self.setGeometry(200,100,315,500)
        self.setWindowTitle('app design')
        self.setWindowIcon(QIcon('gpt.png'))
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Times",14))
        #line_edit.setText('default text')
        line_edit.setPlaceholderText("username")
        
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

app = QApplication(sys.argv) 

win = Window() 
win.show() 
sys.exit(app.exec())

