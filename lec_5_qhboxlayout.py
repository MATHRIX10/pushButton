# align the widgets horizontally 

from PyQt6.QtWidgets import QApplication as qa , QWidget as qw ,QPushButton as push,QHBoxLayout as hboxl
from PyQt6.QtGui import QIcon as ic 



import sys 


class Window(qw) :
    def __init__(self) :
        super().__init__() 


        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(ic('gpt.png'))
        
        hbox = hboxl()
        btn1 = push('btn1')
        
        btn2 = push('btn2')

        btn3 = push('btn3')

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        self.setLayout(hbox)
        hbox.addSpacing(200)





app = qa(sys.argv)

Window = Window()

Window.show() 


sys.exit(app.exec())