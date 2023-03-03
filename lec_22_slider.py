from PyQt6.QtWidgets import QApplication, QWidget,QLabel  ,QVBoxLayout,QHBoxLayout,QSlider
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
        hbox= QHBoxLayout() 
        self.slider = QSlider()
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow) 
        self.slider.setOrientation(Qt.Orientations.Horizontal)
        self.slider.setTickInterval(5)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.label = QLabel('0')
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.slider.valueChanged.connect(self.slider_value)
        

    def slider_value(self) : 
        value = self.slider.value() 
        self.label.setText(str(value))

        



            
app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())
