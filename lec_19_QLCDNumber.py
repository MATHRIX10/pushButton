from PyQt6.QtWidgets import QApplication, QWidget,QLabel  ,QVBoxLayout,QLCDNumber,QPushButton
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize ,QTime,QTimer
import sys 
from random import randint 

class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,300,200)
        self.setWindowTitle('radio button ')
        self.setWindowIcon(QIcon('gpt.png'))
        timer = QTimer() 
        timer.timeout.connect(self.show_lcd)
        timer.start(100)
        self.show_lcd() 
        self.btn = QPushButton('click',self) 
        self.btn.clicked.connect(self.randm)
        self.lcd2 = QLCDNumber() 
        self.lcd2.setStyleSheet('background-color:#A8C64E')
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.btn)
        vbox2.addWidget(self.lcd2)
        self.setLayout(vbox2)


    def show_lcd(self) : 
        vbox = QVBoxLayout() 
       
        lcd = QLCDNumber() 
        lcd.setStyleSheet('background-color:#A8C64E')
        
        vbox.addWidget(lcd)
        
        time = QTime.currentTime() 
        text = time.toString('hh:mm')

        lcd.display(text)
        
        

    def randm(self) :
        num = randint(1,20) 
        self.lcd2.display(num)
        
        







    



app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())
