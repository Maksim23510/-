from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import* # нужен файл! 
from second_win import* # нужен файл!



class MainWin(QWidget):
    def set_appear(self):# внешний вид
        self.set.Window.Title(txt_title)
        self.resize(Win_width,Win_height)
        self.move(win_x, win_y)
    def initUI(self):# элементы интерфейса
        self.hellow_text = QLabel(txt_hellow)
        self.instruction = QLabel(txt_instruction)
        self.button = PushButton(txt_next)
        self.hellow_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWidget(self.layout)
    def connects(self):# обработка событий
        self.btn_next.clicked.connect(self,next_click)
    def next_click(self):
        self.hide
        self.tw=TestWin()



app = QApplication([])
mw = MainWin()
app.exec_()
