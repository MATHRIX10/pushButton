from PyQt6.QtWidgets import QApplication, QWidget,QLabel  ,QVBoxLayout,QComboBox,QHBoxLayout
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize ,QTime,QTimer
import sys 
from random import randint 

class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,500,200)
        self.setWindowTitle('radio button ')
        self.setWindowIcon(QIcon('gpt.png'))
        self.create_combo() 
    def create_combo(self) : 
        hbox = QHBoxLayout() 
        label = QLabel('selct a count type')
        label.setFont(QFont("Times",15))
        self.combo = QComboBox() 
        hbox.addWidget(label)
        hbox.addWidget(self.combo)
        
        self.combo.addItem('login')
        self.combo.addItem('regiter')
        self.combo.addItem('create account')
        self.combo.addItem('profile')
        self.combo.currentIndexChanged.connect(self.combo_changed)
        vbox = QVBoxLayout() 
        self.label_resutl = QLabel('result ')
        vbox.addWidget(self.label_resutl)
        vbox.addLayout(hbox)
        self.setLayout(vbox)    



    def combo_changed(self) : 
        item = self.combo.currentText() 
        self.label_resutl.setText('{}'.format(item))
            
app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())
