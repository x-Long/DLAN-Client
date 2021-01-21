#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX

# from ui import Ui_Form
from dlan import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys

class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.is_ture=[]
        self.is_hide=[]


        # self.pushButton_0.clicked.connect(lambda: self.on_button(["self.frame_0_0","self.frame_0_1"])) 
        # self.frame_0_0.setVisible(False)
        # self.frame_0_1.setVisible(False)
        # self.pushButton_0_0.clicked.connect(lambda: self.on_button2("self.frame_0_0_0")) 
        # self.pushButton_0_1.clicked.connect(lambda: self.on_button2("self.frame_0_1_1")) 

        # self.pushButton_1.clicked.connect(lambda: self.on_button(["self.frame_1_0","self.frame_1_1"])) 
        # self.frame_1_0.setVisible(False)
        # self.frame_1_1.setVisible(False)
        # self.pushButton_1_0.clicked.connect(lambda: self.on_button2("self.frame_1_0_0")) 
        # self.pushButton_1_1.clicked.connect(lambda: self.on_button2("self.frame_1_1_1")) 
        self.all=[]

        for i in range(len(self.aa)):

            one_pushButton=""
            two_pushButton=[]
            two_frame=[]
            three_frame=[]

            for key in self.aa[i]:
   
                print(key,i)
                self.item_flag=0
                one_pushButton="self.pushButton"+"_"+str(i)

                for j in range(len(self.aa[i][key])):
                    for key1 in self.aa[i][key][j]:
                        
                        print(key1,str(i),j)
                        two_frame.append("self.frame"+"_"+str(i)+"_"+str(j))
                        two_pushButton.append("self.pushButton"+"_"+str(i)+"_"+str(j))

                        for k in range(len(self.aa[i][key][j][key1])):
                            print(self.aa[i][key][j][key1][k],i,j,k)
                        three_frame.append("self.frame"+"_"+str(i)+"_"+str(j)+"_"+str(self.item_flag))

                        self.item_flag=self.item_flag+1   
                        print(self.item_flag)
            temp=[]
            print(one_pushButton)
            print(two_frame)
            print(two_pushButton)
            print(three_frame)
            temp.append(one_pushButton)
            temp.append(two_frame)
            temp.append(two_pushButton)
            temp.append(three_frame)
            self.all.append(temp)


        print(self.all[0],"\n",self.all[1])
        
        for k in range(len(self.all)):
            # eval(self.all[k][0]).clicked.connect(lambda: self.on_button(self.all[k][1]))
            self.a1(k)
            for h in self.all[k][1]:
                # eval(h).setVisible(False)
                self.a2(h)
            for f in range(len(self.all[k][2])):
                # eval(self.all[k][2][f]).clicked.connect(lambda: self.on_button2(self.all[k][3][f]))
                print(self.all[k][2][f])
                self.a3(k,f)
        
    def a1(self,k):
        eval(self.all[k][0]).clicked.connect(lambda: self.on_button(self.all[k][1]))
    def a2(self,h):
        eval(h).setVisible(False)
    def a3(self,k,f):
        eval(self.all[k][2][f]).clicked.connect(lambda: self.on_button2(self.all[k][3][f]))


        # self.iconLabel =  QtWidgets.QLabel()
        # self.textLabel =  QtWidgets.QLabel()
        
        # self.iconLabel.setFixedSize(25,40)
        # self.textLabel.setFixedWidth(150)

        # # self.iconLabel.setStyleSheet("border:1px solid red;")
        # # self.textLabel.setStyleSheet("border:1px solid red;")
        # self.iconLabel.setPixmap(QtGui.QPixmap("./Vector.png"))
        # self.textLabel.setText("常规检查")

        # # self.textLabel.setFixedWidth(100)
        # # self.textLabel.setFixedHeight(50);
        # self.myLayout = QtWidgets.QHBoxLayout()
        # self.myLayout.setContentsMargins(0, 0, 0, 0)
        # self.myLayout.setSpacing(0)

        # self.myLayout.addSpacing(32)
        # self.myLayout.addWidget(self.iconLabel)
        # self.myLayout.addSpacing(0)
        # self.myLayout.addWidget(self.textLabel)
        # self.myLayout.addStretch()

        # self.pushButton_1.setLayout(self.myLayout)

  
    # def on_button(self, frame):
    #     print("111",eval(frame).isVisible())
    #     if eval(frame).isVisible():
    #         eval(frame).setVisible(False)
    #         self.is_ture=""
    #         for item in self.is_hide:
    #             eval(item).setVisible(True)
    #     else:
    #         eval(frame).setVisible(True)
    #         if self.is_ture!="":
    #             eval(self.is_ture).setVisible(False)
    #         for item in self.is_hide:
    #             eval(item).setVisible(True)
    #         self.is_ture=frame
    #         # QtWidgets.QApplication.processEvents()
    #         # self.btn2.setVisible(True)

    def on_button(self, frame1):
        # count_clear_istrue=0
        for frame in frame1:
            # print(frame,eval(frame).isVisible())
            if eval(frame).isVisible():
                eval(frame).setVisible(False)
                for item in self.is_hide:
                    eval(item).setVisible(True)
            else:

                if len(self.is_ture)==len(frame1):
                    print(self.is_ture)
                    eval(self.is_ture[0]).setVisible(False)
                    self.is_ture.remove(self.is_ture[0])

                # if count_clear_istrue==0:
                #     print(self.is_ture)

                #     for is_true_item in self.is_ture:
                #         eval(is_true_item).setVisible(False)
                #         self.is_ture.remove(is_true_item)
                #     count_clear_istrue=count_clear_istrue+1
                
                eval(frame).setVisible(True)
                self.is_ture.append(frame)
                print("istrue",self.is_ture)

                for item in self.is_hide:
                    eval(item).setVisible(True)
                # self.is_ture.append(frame)
                # QtWidgets.QApplication.processEvents()
                # self.btn2.setVisible(True)


    def on_button2(self, frame):

        if eval(frame).isVisible():
            eval(frame).setVisible(False)
            self.is_hide.append(frame)
        else:
            eval(frame).setVisible(True)
            self.is_hide.remove(frame)



# 运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.setWindowIcon(QtGui.QIcon('logo.png'))
    main_window.show()
    
    # list = main_window.findChildren(QtWidgets.QFrame)
    # print(list)
    # for i in list:
    #     print(i.objectName())
    # print(main_window.objectName())
    app.exec()
