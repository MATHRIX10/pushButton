from PyQt6.QtWidgets import QApplication,QLabel,QHBoxLayout,QRadioButton,QVBoxLayout , QWidget 
from PyQt6.QtGui import QIcon ,QFont
from PyQt6.QtCore import QSize 
import sys 


class Window(QWidget) : 
    def __init__(self) :
        super().__init__() 

        self.setGeometry(200,200,300,200)
        self.setWindowTitle('radio button ')
        self.setWindowIcon(QIcon('gpt.png'))
        self.radio() 
    def radio(self) : 

        hbox = QHBoxLayout() 
        rad1 = QRadioButton('python')
        rad1.setIcon(QIcon('gpt.png'))
        rad1.setIconSize(QSize(40,40))
        rad1.setFont(QFont('Times',24))


        rad2 = QRadioButton('java')
        rad2.setIcon(QIcon('gpt.png'))
        rad2.setIconSize(QSize(40,40))
        rad2.setFont(QFont('Times',24))
        
        rad1.toggled.connect(self.radio_selcted)
        rad2.toggled.connect(self.radio_selcted)
        vbox   = QVBoxLayout()
        self.label = QLabel('hello')
        self.setFont(QFont('times',14))
        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def radio_selcted(self) : 
        radio_btn = self.sender() 
        if radio_btn.isChecked() : 
            self.label.setText('you have selected {}'.format(radio_btn.text()))

app = QApplication(sys.argv) 

window = Window() 

window.show() 


sys.exit(app.exec())
