# align the widgets horizontally 

from PyQt6.QtWidgets import QApplication as qa , QWidget as qw ,QPushButton as push,QVBoxLayout as vboxl
from PyQt6.QtGui import QIcon as ic 



import sys 


class Window(qw) :
    def __init__(self) :
        super().__init__() 


        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(ic('gpt.png'))
        
        vbox = vboxl()
        btn1 = push('btn1')
        
        btn2 = push('btn2')

        btn3 = push('btn3')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        vbox.addSpacing(200)





app = qa(sys.argv)

Window = Window()

Window.show() 


sys.exit(app.exec())