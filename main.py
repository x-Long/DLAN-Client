#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX

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
    
    def resizeEvent(self, event):#更新窗体大小事件
        self.message="窗口大小调整为：QSize({0},{1})".format(event.size().width(),event.size().height())
        self.frame_dingji.setMaximumHeight(event.size().height()-30)
        self.update()


    def high_level_button_event(self,k):
        print("self.side_bar_widgets[k][0]",self.side_bar_widgets[k][0])
        eval(self.side_bar_widgets[k][0]).clicked.connect(lambda: self.high_frame_res(self.side_bar_widgets[k][1],k))

    def hide_frame(self,h):
        eval(h).setVisible(False)
    def low_level_button_event(self,k,f):
        eval(self.side_bar_widgets[k][2][f]).clicked.connect(lambda: self.low_frame_res(self.side_bar_widgets[k][3][f],k,f))

    def change_arrows(self,wid,status_icon):
        eval(wid).itemAt(eval(wid).count()-1).widget().deleteLater()
        iconLabel = QtWidgets.QLabel()
        iconLabel.setFixedSize(25, 30)
        iconLabel.setPixmap(QtGui.QPixmap(status_icon))
        eval(wid).addWidget(iconLabel)


    def high_frame_res(self, frame_items,k):
        # print(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).count())
        # for i in range(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).count()):
        #     print(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).itemAt(i).widget().deleteLater(),11111111111111111)

        # eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).itemAt(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).count()-1).widget().deleteLater()

        if eval(frame_items[0]).isVisible():
            self.change_arrows("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:],"./icon/close.png")
            # iconLabel = QtWidgets.QLabel()
            # iconLabel.setFixedSize(25, 30)
            # iconLabel.setPixmap(QtGui.QPixmap("./icon/close.png"))
            # eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).addWidget(iconLabel)
        else:
            
            self.change_arrows("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:],"./icon/open.png")
            # iconLabel= QtWidgets.QLabel()
            # iconLabel.setFixedSize(25, 30)
            # iconLabel.setPixmap(QtGui.QPixmap("./icon/open.png"))
            # eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).addWidget(iconLabel)

        count_clear_istrue=0
        for frame in frame_items:
            if eval(frame).isVisible():

                eval(frame).setVisible(False)
                for item in self.is_hide:
                    eval(item).setVisible(True)
                    self.change_arrows("self.myLayout_pushButton_"+item[11:14],"./icon/open.png")
            else:
                if count_clear_istrue==0:
                    for is_true_item in self.is_display:
                        eval(is_true_item).setVisible(False)  
                        print(self.is_display,2222222222222222222222)
                        print(frame)
                    if len(self.is_display)!=0:
                        self.change_arrows("self.myLayout_pushButton_"+self.is_display[0][11],"./icon/close.png")
                    self.is_display.clear()
                    count_clear_istrue=count_clear_istrue+1

                eval(frame).setVisible(True)
                self.change_arrows("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:],"./icon/open.png")

                self.is_display.append(frame)
                for item in self.is_hide:
                    print("item",item)
                    eval(item).setVisible(True)
                    self.change_arrows("self.myLayout_pushButton_"+item[11:14],"./icon/open.png")

    def low_frame_res(self, frame,k,f):

        eval("self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:]).itemAt(eval("self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:]).count()-1).widget().deleteLater()
        if eval(frame).isVisible():
            self.change_arrows("self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:],"./icon/close.png")
            eval(frame).setVisible(False)
            self.is_hide.append(frame)
        else:
            self.change_arrows("self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:],"./icon/open.png")
            eval(frame).setVisible(True)
            self.is_hide.remove(frame)



# 运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.setWindowIcon(QtGui.QIcon('logo.png'))
    main_window.setWindowTitle("帝岚科技计算机终端保密检查系统")
    print(main_window.width())
    # main_window.resize(main_window.width(),main_window.width()*0.6)
    main_window.show()
    app.exec()
