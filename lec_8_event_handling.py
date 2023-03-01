

from PyQt6.QtWidgets import QApplication as qa , QWidget as qw ,QPushButton as push,QLabel as label,QHBoxLayout as hboxl  

from PyQt6.QtGui import QIcon as ic ,QFont as font



import sys 


class Window(qw) :
    def __init__(self) :
        super().__init__() 


        self.setGeometry(200,200,700,400)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(ic('gpt.png'))
        pushb = push('add btn',self)
        pushb.clicked.connect(self.create_widget)
        







    def create_widget(self) :
        hbox = hboxl() 
        btn = push('change text')
        btn.clicked.connect(self.clicked_btn)
        self.label1 = label('label name') 
        hbox.addWidget(btn)
        hbox.addWidget(self.label1)

        self.setLayout(hbox)


    def clicked_btn(self) : 
        self.label1.setText('another text')
        self.label1.setFont(font('Times',15))
        self.label1.setStyleSheet('color : red ')

        
       



  




app = qa(sys.argv)

Window = Window()

Window.show() 


sys.exit(app.exec())