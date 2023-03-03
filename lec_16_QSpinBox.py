from PyQt6.QtWidgets import QApplication, QWidget,QLabel ,QSpinBox , QLineEdit,QHBoxLayout
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize 
import sys 


class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,300,200)
        self.setWindowTitle('radio button ')
        self.setWindowIcon(QIcon('gpt.png'))

        hbox = QHBoxLayout() 
        self.label = QLabel('label') 

        hbox.addWidget(self.label)
        
        self.lineedit = QLineEdit()
        self.spine = QSpinBox() 
        self.spine.valueChanged.connect(self.spin)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spine)
        self.setLayout(hbox)




    def spin(self) : 
        if self.lineedit.text() != 0 : 
            price = int(self.lineedit.text())
            totalPrice = self.spine.value()*price 
            self.label.setText(str(totalPrice))

        else : 
            print('wrong value')



app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())
