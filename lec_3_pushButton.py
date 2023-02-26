from PyQt6.QtWidgets import QApplication,QWidget 
import sys 

from PyQt6.QtGui import QIcon 


class Window(QWidget) : 
    def __init__(self) : 
        super().__init__()
        self.setGeometry(200,100,315,500)
        self.setWindowTitle('app design')
        self.setWindowIcon(QIcon('gpt.png'))
        

       
 


app = QApplication(sys.argv) 

win = Window() 
win.show() 
sys.exit(app.exec())

