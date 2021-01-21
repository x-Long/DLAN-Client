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

        self.is_display=[]
        self.is_hide=[]
        self.side_bar_widgets=[]

        for i in range(len(self.side_bar_info)):
            high_level_pushButton=""
            med_level_pushButton=[]
            high_level_frame=[]
            low_level_frame=[]

            for key in self.side_bar_info[i]:
   
                print(key,i)
                self.item_flag=0
                high_level_pushButton="self.pushButton"+"_"+str(i)

                for j in range(len(self.side_bar_info[i][key])):
                    for key1 in self.side_bar_info[i][key][j]:
                        
                        print(key1,str(i),j)
                        high_level_frame.append("self.frame"+"_"+str(i)+"_"+str(j))
                        med_level_pushButton.append("self.pushButton"+"_"+str(i)+"_"+str(j))

                        for k in range(len(self.side_bar_info[i][key][j][key1])):
                            print(self.side_bar_info[i][key][j][key1][k],i,j,k)
                        low_level_frame.append("self.frame"+"_"+str(i)+"_"+str(j)+"_"+str(self.item_flag))

                        self.item_flag=self.item_flag+1   
                        print(self.item_flag)
            temp=[]
            temp.append(high_level_pushButton)
            temp.append(high_level_frame)
            temp.append(med_level_pushButton)
            temp.append(low_level_frame)
            self.side_bar_widgets.append(temp)

        
        for k in range(len(self.side_bar_widgets)):
            self.high_level_button_event(k)
            for h in self.side_bar_widgets[k][1]:
                self.hide_frame(h)
            for f in range(len(self.side_bar_widgets[k][2])):
                print(self.side_bar_widgets[k][2][f])
                self.low_level_button_event(k,f)
        
    def high_level_button_event(self,k):
        eval(self.side_bar_widgets[k][0]).clicked.connect(lambda: self.high_frame_res(self.side_bar_widgets[k][1]))
    def hide_frame(self,h):
        eval(h).setVisible(False)
    def low_level_button_event(self,k,f):
        eval(self.side_bar_widgets[k][2][f]).clicked.connect(lambda: self.low_frame_res(self.side_bar_widgets[k][3][f]))

    def high_frame_res(self, frame_items):
        count_clear_istrue=0
        for frame in frame_items:
            if eval(frame).isVisible():
                eval(frame).setVisible(False)
                for item in self.is_hide:
                    eval(item).setVisible(True)
            else:
                if count_clear_istrue==0:
                    for is_true_item in self.is_display:
                        eval(is_true_item).setVisible(False)  
                    self.is_display.clear()
                    count_clear_istrue=count_clear_istrue+1
                eval(frame).setVisible(True)
                self.is_display.append(frame)
                for item in self.is_hide:
                    eval(item).setVisible(True)

    def low_frame_res(self, frame):

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
    app.exec()
