from .QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout , QHBoxLayout, QMessageBox , QRadioButton , QLineEdit, Qt, QTimer, QTime

class TestWin(QWidget):
	def __init__(self):
    super().__init__()
	self.set_appear():
    	self.set.Window.Title(txt_title)
        self.resize(Win_width,Win_height)
        self.move(win_x, win_y)
    self.initUI():
    	self.h_line = QHBoxLayout()
	    self.r_line = QVBoxLayout()
	    self.l_line = QVBoxLayout()
	    initials = QLabel('txt_opt1')
	    years = QLabel('txt_opt2')
	    instruction1 = QLabel('txt_instruction2')
	    instruction2 = QLabel('txt_instruction3')
	    instruction3 = QLabel('txt_instruction4')
	    btn_test1 = QPushButton('txt_test1')
	    btn_test2= QPushButton('txt_test2')
	    btn_test3 = QPushButton('txt_test3')
	    button4 = QPushButton('txt_next2')
	    inpuT1 = QLineEdit()
	    line_age= QLineEdit()
	    line_test1= QLineEdit()
	    line_test2= QLineEdit()
	    line_test3= QLineEdit()

	    self.l_line.addWidget(initials, alignment = Qt.AlignCenter)
	    self.l_line.addWidget(inpuT1, alignment = Qt.AlignCenter)
	    self.l_line.addWidget(years, alignment = Qt.AlignCenter)
	    self.l_line.addWidget(line_age, alignment = Qt.AlignCenter)
	    self.r_line.addWidget(instruction1, alignment = Qt.AlignCenter)
	    self.r_line.addWidget(btn_test1, alignment = Qt.AlignCenter)
	    self.l_line.addWidget(line_test1, alignment = Qt.AlignCenter)
	    self.r_line.addWidget(instruction2, alignment = Qt.AlignCenter)
	    self.r_line.addWidget(btn_test2, alignment = Qt.AlignCenter)
	    self.r_line.addWidget(instruction3, alignment = Qt.AlignCenter)
	    self.r_line.addWidget(btn_test3, alignment = Qt.AlignCenter)
	    self.l_line.addWidget(line_test2, alignment = Qt.AlignCenter)
	    self.l_line.addWidget(line_test3, alignment = Qt.AlignCenter)
	  	self.h_line.addWidget(button4, alignment = Qt.AlignCenter)
	    self.h_line.addLayout(self.l_line)
	    self.h_line.addLayout(self.r_line)
	    main_win.setLayout(self.h_line)
#первый таймер
    def timer_test(self):
	global time
	time = QTime(0, 1, 0)
	self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
    	global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)

#второй таймер
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
   def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
          self.timer.stop()
    def connects(self):
        self.btn_test1.clicked.connect(self.timer_sits)
#третий таймер
    def timer_final(self):
        global time
        self.timer.timeout.connect(self.timer3Event)	
        self.timer = QTimer()
        self.timer.start(1000)
    def timer3Event(self):
    	if int(time.toString("hh:mm:ss")[6:8]) >= 45:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
       elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
           self.text_timer.setStyleSheet("color: rgb(0,255,0)")
       else:
           self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)       





    self.connects():
    	 self.btn_next.clicked.connect(self,next_click)

   	def next_click(self):
        self.hide
        self.tw=FinalWin()
    
