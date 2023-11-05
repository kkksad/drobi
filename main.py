import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Цепные дроби")
        self.setGeometry(100, 100, 200, 300)
        layout = QVBoxLayout(self)

        
       
    


        self.title1=QLabel(self)
        self.title1.setText("Введите\n дробь")
        self.title1.move(10, 10)
        self.title2=QLabel(self)
        self.title2.move(80,10)
        self.title2.setText("Погрешность")

        

        
        self.input1 = QLineEdit(self)
        self.input1.move(10, 60)
        self.input1.setFixedSize(30,22)
        self.label1 = QLabel(self)
        self.label1.setText("____")
        self.label1.move(10, 65)
        self.input2 = QLineEdit(self)
        self.input2.move(10, 90)
        self.input2.setFixedSize(30,22)

        self.input3 = QLineEdit(self)
        self.input3.move(80, 60)
        self.input3.setFixedSize(60,22)


        


        



        self.button = QPushButton("Посчитать", self)
        self.button.move(80, 80)
        self.button.clicked.connect(self.button_clicked)

        self.visual=QLabel(self) 
        self.visual.setText("========================")
        self.visual.move(0,110) 

        self.ans1 = QLabel(self)
        self.ans1.move(0, 140)
        layout.addWidget(self.ans1)
        self.ans2 = QLabel(self)
        self.ans2.move(0, 170)
        layout.addWidget(self.ans2)
        self.ch=QLabel()
        self.ch.move(0,185)
        self.ch.setText("______")
        self.ans3 = QLabel(self)
        self.ans3.move(0, 200)
        layout.addWidget(self.ans3)

        


    def zepn(self,a, b, toch): # трансформация в цепную
        itog_list=[]
        while len(itog_list) != toch :
            if b>0:
                q=a // b
                c=b
                b=a - b * q
                a=c
                itog_list.append(int(q))
            else:
                break
        return itog_list
    
    def appr_fraction(self,input_list): # преобразование в похожую(не ебу какую дробь
        col=len(input_list)
        n=input_list[col-1]
        d=1
        while(col>1):
            r,d=d,n
            col-=1
            n=input_list[col-1]*n+r
        return n, d
    def error(self, chisl1, znam1, chisl2, znam2): # погрешность
        a=chisl1*znam2-znam1*chisl2
        b=znam1*znam2
        return round(math.fabs(a/b), 4)


       

    def button_clicked(self):
        a = int(self.input1.text())
        b = int(self.input2.text())
        toch=int(self.input3.text())
        itog_list=self.zepn(a,b,toch)
        self.ans1.setText(str(itog_list))
        chisl, znam=self.appr_fraction(itog_list)
        ans=str(chisl)+"/"+str(znam)
        self.ans2.setText(ans)
        self.ans3.setText(str(self.error(a,b,chisl,znam)))
        
        

        
        


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())

