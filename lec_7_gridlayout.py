# align the widgets horizontally 

from PyQt6.QtWidgets import QApplication as qa , QWidget as qw ,QPushButton as push,QGridLayout as grid
from PyQt6.QtGui import QIcon as ic 



import sys 


class Window(qw) :
    def __init__(self) :
        super().__init__() 


        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(ic('gpt.png'))
        

        gridl = grid() 
        btn1 = push('one')
        btn2 = push('two')
        btn3 = push('three')
        btn4 = push('four')
        btn5 = push('five')
        btn6 = push('six')
        btn7 = push('seven')
        btn8 = push('eight')

        gridl.addWidget(btn1,0,0)
        gridl.addWidget(btn2,0,1)
        gridl.addWidget(btn3,0,2)
        gridl.addWidget(btn4,0,3)
        gridl.addWidget(btn5,1,0)
        gridl.addWidget(btn6,1,1)
        gridl.addWidget(btn7,1,2)
        gridl.addWidget(btn8,1,3)


        self.setLayout(gridl)



  




app = qa(sys.argv)

Window = Window()

Window.show() 


sys.exit(app.exec())