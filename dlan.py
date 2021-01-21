# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DLAN-2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 621)
        Form.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"color: #FFFFFF;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(Form)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setLineWidth(0)
        self.frame_main.setObjectName("frame_main")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_dingji = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_dingji.sizePolicy().hasHeightForWidth())
        self.frame_dingji.setSizePolicy(sizePolicy)
        self.frame_dingji.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_dingji.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_dingji.setStyleSheet("background: #112853;")
        self.frame_dingji.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_dingji.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dingji.setLineWidth(0)
        self.frame_dingji.setObjectName("frame_dingji")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_dingji)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.aa = [
            {
                "常规检查": [
                    {"终端基本信息": ["主机信息", "硬盘信息"]},
                    {"USB设备检查": ["存储设备", "其他设备"]},

                ]
            },

            {
                "安全检查": [
                    {"系统安全检查": ["系统共享安全", "无线通信模块"]},
                    {"安全配置检查": ["安全审计配置", "账户安全配置"]},
                ]
            },
        ]
        self.pushButton_icon = {
            "常规检查": "./Vector.png",
            "终端基本信息": "./Vector.png",
            "主机信息": "./Vector.png",
            "硬盘信息": "./Vector.png",
            "USB设备检查": "./Vector.png",
            "存储设备": "./Vector.png",
            "其他设备": "./Vector.png",
            "安全检查": "./Vector.png",
            "系统安全检查": "./Vector.png",
            "系统共享安全": "./Vector.png",
            "无线通信模块": "./Vector.png",
            "安全配置检查": "./Vector.png",
            "安全审计配置": "./Vector.png",
            "账户安全配置": "./Vector.png",
            "default":"default.png"
        }

        # for i in range(len(self.aa)):
        #     for key in self.aa[i]:
        #         print(key,i)
        #         self.nihao1("self.frame"+"_"+str(i),"self.verticalLayout"+"_"+str(i),"self.pushButton"+"_"+str(i))
        #         eval("self.pushButton"+"_"+str(i)).setText(key)
        #         self.item_flag=0

        #         for j in range(len(self.aa[i][key])):
        #             for key1 in self.aa[i][key][j]:
                        
        #                 print(key1,str(i),j)
        #                 self.nihao2("self.frame"+"_"+str(i)+"_"+str(j),"self.verticalLayout"+"_"+str(i)+"_"+str(j),"self.pushButton"+"_"+str(i)+"_"+str(j),str(i))
        #                 eval("self.pushButton"+"_"+str(i)+"_"+str(j)).setText(key1)

        #                 for k in range(len(self.aa[i][key][j][key1])):
        #                     print(self.aa[i][key][j][key1][k],i,j,k)
        #                     self.nihao3("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k),str(i),str(j))    
        #                     eval("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setText(self.aa[i][key][j][key1][k])
        #                 self.item_flag=self.item_flag+1   

        for i in range(len(self.aa)):
            for key in self.aa[i]:
                print(key,i)
                self.nihao1("self.frame"+"_"+str(i),"self.verticalLayout"+"_"+str(i),"self.pushButton"+"_"+str(i))
                # eval("self.pushButton"+"_"+str(i)).setText(key)
                self.item_flag=0

                if key in self.pushButton_icon:
                    self.icon_src=self.pushButton_icon[key]
                else:
                    self.icon_src=self.pushButton_icon["default"]
                    
                  
                       

                exec("self.iconLabel"+"_pushButton"+"_"+str(i)+"= QtWidgets.QLabel()")
                exec("self.textLabel"+"_pushButton"+"_"+str(i)+"= QtWidgets.QLabel()")
                eval("self.iconLabel"+"_pushButton"+"_"+str(i)).setFixedSize(25,40)
                eval("self.textLabel"+"_pushButton"+"_"+str(i)).setFixedWidth(150)
                eval("self.iconLabel"+"_pushButton"+"_"+str(i)).setPixmap(QtGui.QPixmap(self.icon_src))
                eval("self.textLabel"+"_pushButton"+"_"+str(i)).setText(key)
                exec("self.myLayout"+"_pushButton"+"_"+str(i)+"= QtWidgets.QHBoxLayout()")
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).setContentsMargins(0, 0, 0, 0)
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).setSpacing(0)
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).addSpacing(32)
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).addWidget(eval("self.iconLabel"+"_pushButton"+"_"+str(i)))
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).addSpacing(0)
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).addWidget(eval("self.textLabel"+"_pushButton"+"_"+str(i)))
                eval("self.myLayout"+"_pushButton"+"_"+str(i)).addStretch()
                eval("self.pushButton"+"_"+str(i)).setLayout(eval("self.myLayout"+"_pushButton"+"_"+str(i)))

                for j in range(len(self.aa[i][key])):
                    for key1 in self.aa[i][key][j]:  
                        if key1 in self.pushButton_icon:
                            self.icon_src=self.pushButton_icon[key1]
                        else:
                            self.icon_src=self.pushButton_icon["default"]
                        
                        print(key1,str(i),j)
                        self.nihao2("self.frame"+"_"+str(i)+"_"+str(j),"self.verticalLayout"+"_"+str(i)+"_"+str(j),"self.pushButton"+"_"+str(i)+"_"+str(j),str(i))
                        eval("self.pushButton"+"_"+str(i)+"_"+str(j)).setText(key1)

                        exec("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"= QtWidgets.QLabel()")
                        exec("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"= QtWidgets.QLabel()")
                        eval("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)).setFixedSize(25,30)
                        eval("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)).setFixedWidth(150)
                        eval("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)).setPixmap(QtGui.QPixmap(self.icon_src))
                        eval("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)).setText(key1)
                        exec("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"= QtWidgets.QHBoxLayout()")
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).setContentsMargins(0, 0, 0, 0)
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).setSpacing(0)
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).addSpacing(50)
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).addWidget(eval("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)))
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).addSpacing(0)
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).addWidget(eval("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)))
                        eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)).addStretch()
                        eval("self.pushButton"+"_"+str(i)+"_"+str(j)).setLayout(eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)))

                        for k in range(len(self.aa[i][key][j][key1])):
                            print(self.aa[i][key][j][key1][k],i,j,k)

                            if self.aa[i][key][j][key1][k] in self.pushButton_icon:
                                self.icon_src=self.pushButton_icon[self.aa[i][key][j][key1][k]]
                            else:
                                self.icon_src=self.pushButton_icon["default"]

                            self.nihao3("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k),str(i),str(j))    
                            eval("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setText(self.aa[i][key][j][key1][k]) 

                            exec("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)+"= QtWidgets.QLabel()")
                            exec("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)+"= QtWidgets.QLabel()")
                            eval("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setFixedSize(25,25)
                            eval("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setFixedWidth(150)
                            eval("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setPixmap(QtGui.QPixmap(self.icon_src))
                            eval("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setText(self.aa[i][key][j][key1][k])
                            exec("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)+"= QtWidgets.QHBoxLayout()")
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setContentsMargins(0, 0, 0, 0)
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setSpacing(0)
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).addSpacing(70)
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).addWidget(eval("self.iconLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)))
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).addSpacing(0)
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).addWidget(eval("self.textLabel"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)))
                            eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).addStretch()
                            eval("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setLayout(eval("self.myLayout"+"_pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)))


                        self.item_flag=self.item_flag+1   


        self.nihao4()

    def nihao1(self,frame,verticalLayout,pushButton):
        exec(frame+" = QtWidgets.QFrame(self.frame_dingji)")
        
        # eval(frame) = QtWidgets.QFrame(self.frame_dingji)
        print(frame)
        eval(frame).setFrameShape(QtWidgets.QFrame.NoFrame)
        eval(frame).setFrameShadow(QtWidgets.QFrame.Raised)
        eval(frame).setLineWidth(0)
        eval(frame).setObjectName(frame[5:])
        self.verticalLayout_8.addWidget(eval(frame))

        exec(verticalLayout+"= QtWidgets.QVBoxLayout(" + frame + "  )")
        # eval(verticalLayout) = QtWidgets.QVBoxLayout(eval(frame))
        eval(verticalLayout).setContentsMargins(0, 0, 0, 0)
        eval(verticalLayout).setSpacing(0)
        eval(verticalLayout).setObjectName(verticalLayout[5:])

        exec(pushButton+"= QtWidgets.QPushButton("+frame+")")
        # eval(pushButton) = QtWidgets.QPushButton(eval(frame))
        eval(pushButton).setMinimumSize(QtCore.QSize(0, 40))
        # eval(pushButton).setFont()
        eval(pushButton).setStyleSheet("background: #17376A;\n"
    "border-bottom: 1px solid #29407C;\n"
    "font-family: PingFang SC;\n"
    "font-style: normal;\n"
    "font-weight: 600;\n"
    "font-size: 14px;\n"
    "line-height: 20px;\n"
    "\n"
    "color: #FFFFFF;\n"
    "")
        eval(pushButton).setAutoDefault(False)
        eval(pushButton).setFlat(False)
        eval(pushButton).setObjectName(pushButton[5:])
        eval(verticalLayout).addWidget(eval(pushButton))






    # "self.frame"+"_"+str(i)+"_"+str(j)
    # "self.verticalLayout"+"_"+str(i)+"_"+str(j)
    # "self.pushButton"+"_"+str(i)+"_"+str(j)
# "self.frame"+"_"+str(i)

# 'self.frame'+'_'+str(i)

# "eval('self.frame'+'_'+str(i))"
# self.frame'+'_'+str(i)+'_'+str(j)

    def nihao2(self,frame,verticalLayout,pushButton,i):
        ccc='self.frame'+'_'+i
        exec(frame+" = QtWidgets.QFrame( "+ccc+"  )")
        # eval(frame) = QtWidgets.QFrame(self.frame_1_1)
        eval(frame).setFrameShape(QtWidgets.QFrame.NoFrame)
        eval(frame).setFrameShadow(QtWidgets.QFrame.Raised)
        eval(frame).setLineWidth(0)
        eval(frame).setObjectName(frame[5:])
        eval("self.verticalLayout"+"_"+str(i)).addWidget(eval(frame))

        exec(verticalLayout+" = QtWidgets.QVBoxLayout("+frame+")")
        # eval(verticalLayout)  = QtWidgets.QVBoxLayout(eval(frame))
        eval(verticalLayout).setContentsMargins(0, 0, 0, 0)
        eval(verticalLayout).setSpacing(0)
        eval(verticalLayout).setObjectName(verticalLayout[5:])

        exec(pushButton+" = QtWidgets.QPushButton("+frame+")")
        # eval(pushButton) = QtWidgets.QPushButton(eval(frame))
        eval(pushButton).setMinimumSize(QtCore.QSize(0, 30))
        eval(pushButton).setStyleSheet("font-family: PingFang SC;\n"
    "font-style: normal;\n"
    "font-weight: 500;\n"
    "font-size: 13px;\n"
    "line-height: 20px;\n"
    "color: #FFFFFF;")
        eval(pushButton).setFlat(False)
        eval(pushButton).setObjectName(pushButton[5:])
        eval(verticalLayout).addWidget(eval(pushButton))

        # eval(frame+"_"+str(self.item_flag))
        dd=str(self.item_flag)
        print(dd)
        ddd=frame+"_"  + dd+ " = QtWidgets.QFrame("+frame+")"
        exec(ddd)
        # eval(frame+"_"+str(self.item_flag)) = QtWidgets.QFrame(eval(frame))
        eval(frame+"_"+str(self.item_flag)).setFrameShape(QtWidgets.QFrame.NoFrame)
        eval(frame+"_"+str(self.item_flag)).setFrameShadow(QtWidgets.QFrame.Raised)
        eval(frame+"_"+str(self.item_flag)).setLineWidth(0)
        eval(frame+"_"+str(self.item_flag)).setObjectName((frame+"_"+str(self.item_flag))[5:])
        eval(verticalLayout).addWidget(eval(frame+"_"+str(self.item_flag)))

        exec(verticalLayout+"_"  + dd+ " = QtWidgets.QVBoxLayout("+frame+'_'+dd+")")
        # exec(verticalLayout+"+'_'+str(self.item_flag) = QtWidgets.QVBoxLayout(eval(frame+'_'+str(self.item_flag)))")
        # eval(verticalLayout+"_"+str(self.item_flag)) = QtWidgets.QVBoxLayout(eval(frame+"_"+str(self.item_flag)))
        eval(verticalLayout+"_"+str(self.item_flag)).setContentsMargins(0, 0, 0, 0)
        eval(verticalLayout+"_"+str(self.item_flag)).setSpacing(0)
        eval(verticalLayout+"_"+str(self.item_flag)).setObjectName((verticalLayout+"_"+str(self.item_flag))[5:])



    # "self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)

    def nihao3(self,pushButton,i,j):
        
        hhh=str(self.item_flag)
        
        exec(pushButton+"=QtWidgets.QPushButton(   self.frame_"+i+'_'+j+'_'+ hhh+")")
        # pushButton = QtWidgets.QPushButton(eval('self.frame'+'_'+str(i)+'_'+str(j)+'_'+str(self.item_flag)))
        eval(pushButton).setMinimumSize(QtCore.QSize(0, 25))
        eval(pushButton).setStyleSheet("font-family: PingFang SC;\n"
    "font-style: normal;\n"
    "font-weight: 300;\n"
    "font-size: 12px;\n"
    "line-height: 17px;\n"
    "color: rgba(255, 255, 255, 0.7);")
        eval(pushButton).setFlat(False)
        eval(pushButton).setObjectName(pushButton[5:])

        eval("self.verticalLayout"+"_"+str(i)+"_"+str(j)+"_"+str(self.item_flag)).addWidget(eval(pushButton))

    def nihao4(self):

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        # self.frame_1_1.raise_()
        # self.frame_2_1.raise_()
        # self.frame_2_2.raise_()
        self.horizontalLayout.addWidget(self.frame_dingji)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_main)
        self.frame_zhuangtai = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_zhuangtai.sizePolicy().hasHeightForWidth())
        self.frame_zhuangtai.setSizePolicy(sizePolicy)
        self.frame_zhuangtai.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_zhuangtai.setStyleSheet("background: #112853;\n"
"font-family: PingFang SC;\n"
"font-style: normal;\n"
"font-weight: 300;\n"
"font-size: 12px;\n"
"line-height: 17px;\n"
"color: rgba(255, 255, 255, 0.8);\n"
"")
        self.frame_zhuangtai.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_zhuangtai.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_zhuangtai.setObjectName("frame_zhuangtai")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_zhuangtai)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label.setMinimumSize(QtCore.QSize(255, 0))
        self.label.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.frame_zhuangtai)

#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)

#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "帝岚科技计算机终端保密检查系统"))
#         self.pushButton_1_1.setText(_translate("Form", "常规检查"))
#         self.pushButton_1_2.setText(_translate("Form", "终端基本信息"))
#         self.pushButton_1_3_1.setText(_translate("Form", "主机信息"))
#         self.pushButton_1_3_2.setText(_translate("Form", "硬盘信息"))
#         self.pushButton_1_3_3.setText(_translate("Form", "操作系统"))
#         self.pushButton_1_3_4.setText(_translate("Form", "身份鉴别"))
#         self.pushButton_2_1.setText(_translate("Form", "安全检查"))
#         self.pushButton_2_2.setText(_translate("Form", "PushButton"))
#         self.pushButton_2_3_1.setText(_translate("Form", "PushButton"))
#         self.pushButton_2_3_2.setText(_translate("Form", "PushButton"))
#         self.pushButton_2_3_3.setText(_translate("Form", "PushButton"))
#         self.pushButton_2_3_4.setText(_translate("Form", "PushButton"))
#         self.label_2.setText(_translate("Form", "版权所有：帝岚科技计算机终端保密检查系统"))
#         self.label_3.setText(_translate("Form", "电话：029-999987656"))
#         self.label_5.setText(_translate("Form", "本机用户名：administration"))
#         self.label_4.setText(_translate("Form", "IP地址：198.888.111.09"))
#         self.label_6.setText(_translate("Form", "计算机密级：涉密计算机（秘密）"))



#         self.frame_1_1 = QtWidgets.QFrame(self.frame_dingji)
#         self.frame_1_1.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_1_1.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_1_1.setLineWidth(0)
#         self.frame_1_1.setObjectName("frame_1_1")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_1_1)
#         self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_4.setSpacing(0)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.pushButton_1_1 = QtWidgets.QPushButton(self.frame_1_1)
#         self.pushButton_1_1.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("PingFang SC")
#         font.setPointSize(-1)
#         font.setBold(True)
#         font.setItalic(False)
#         font.setWeight(75)
#         self.pushButton_1_1.setFont(font)
#         self.pushButton_1_1.setStyleSheet("background: #17376A;\n"
# "border-bottom: 1px solid #29407C;\n"
# "font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 600;\n"
# "font-size: 14px;\n"
# "line-height: 20px;\n"
# "\n"
# "color: #FFFFFF;\n"
# "")
#         self.pushButton_1_1.setAutoDefault(False)
#         self.pushButton_1_1.setFlat(False)
#         self.pushButton_1_1.setObjectName("pushButton_1_1")
#         self.verticalLayout_4.addWidget(self.pushButton_1_1)

#         self.frame_1_2 = QtWidgets.QFrame(self.frame_1_1)
#         self.frame_1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_1_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_1_2.setLineWidth(0)
#         self.frame_1_2.setObjectName("frame_1_2")


#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_1_2)
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_3.setSpacing(0)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.pushButton_1_2 = QtWidgets.QPushButton(self.frame_1_2)
#         self.pushButton_1_2.setMinimumSize(QtCore.QSize(0, 30))
#         self.pushButton_1_2.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 500;\n"
# "font-size: 14px;\n"
# "line-height: 20px;\n"
# "color: #FFFFFF;")
#         self.pushButton_1_2.setFlat(False)
#         self.pushButton_1_2.setObjectName("pushButton_1_2")
#         self.verticalLayout_3.addWidget(self.pushButton_1_2)

#         self.frame_1_3 = QtWidgets.QFrame(self.frame_1_2)
#         self.frame_1_3.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_1_3.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_1_3.setLineWidth(0)
#         self.frame_1_3.setObjectName("frame_1_3")

#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_1_3)
#         self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_2.setSpacing(0)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")

#         self.pushButton_1_3_1 = QtWidgets.QPushButton(self.frame_1_3)
#         self.pushButton_1_3_1.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_1_3_1.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_1_3_1.setFlat(False)
#         self.pushButton_1_3_1.setObjectName("pushButton_1_3_1")
#         self.verticalLayout_2.addWidget(self.pushButton_1_3_1)
#         self.pushButton_1_3_2 = QtWidgets.QPushButton(self.frame_1_3)
#         self.pushButton_1_3_2.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_1_3_2.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_1_3_2.setFlat(False)
#         self.pushButton_1_3_2.setObjectName("pushButton_1_3_2")
#         self.verticalLayout_2.addWidget(self.pushButton_1_3_2)
#         self.pushButton_1_3_3 = QtWidgets.QPushButton(self.frame_1_3)
#         self.pushButton_1_3_3.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_1_3_3.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_1_3_3.setObjectName("pushButton_1_3_3")
#         self.verticalLayout_2.addWidget(self.pushButton_1_3_3)
#         self.pushButton_1_3_4 = QtWidgets.QPushButton(self.frame_1_3)
#         self.pushButton_1_3_4.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_1_3_4.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_1_3_4.setObjectName("pushButton_1_3_4")
#         self.verticalLayout_2.addWidget(self.pushButton_1_3_4)

#         self.verticalLayout_2.addSpacing(10)

#         self.verticalLayout_3.addWidget(self.frame_1_3)
#         self.verticalLayout_4.addWidget(self.frame_1_2)
        
#         self.verticalLayout_8.addWidget(self.frame_1_1)

#         self.frame_2_1 = QtWidgets.QFrame(self.frame_dingji)
#         self.frame_2_1.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_2_1.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2_1.setLineWidth(0)
#         self.frame_2_1.setObjectName("frame_2_1")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2_1)
#         self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_5.setSpacing(0)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.pushButton_2_1 = QtWidgets.QPushButton(self.frame_2_1)
#         self.pushButton_2_1.setMinimumSize(QtCore.QSize(0, 40))
#         self.pushButton_2_1.setStyleSheet("background: #17376A;\n"
# "border-bottom: 1px solid #29407C;\n"
# "font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 600;\n"
# "font-size: 14px;\n"
# "line-height: 20px;\n"
# "\n"
# "color: #FFFFFF;")
#         self.pushButton_2_1.setObjectName("pushButton_2_1")
#         self.verticalLayout_5.addWidget(self.pushButton_2_1)
#         self.frame_2_2 = QtWidgets.QFrame(self.frame_2_1)
#         self.frame_2_2.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_2_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2_2.setLineWidth(0)
#         self.frame_2_2.setObjectName("frame_2_2")
#         self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2_2)
#         self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_6.setSpacing(0)
#         self.verticalLayout_6.setObjectName("verticalLayout_6")
#         self.pushButton_2_2 = QtWidgets.QPushButton(self.frame_2_2)
#         self.pushButton_2_2.setMinimumSize(QtCore.QSize(0, 30))
#         self.pushButton_2_2.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 500;\n"
# "font-size: 14px;\n"
# "line-height: 20px;\n"
# "color: #FFFFFF;")
#         self.pushButton_2_2.setObjectName("pushButton_2_2")
#         self.verticalLayout_6.addWidget(self.pushButton_2_2)
#         self.frame_2_3 = QtWidgets.QFrame(self.frame_2_2)
#         self.frame_2_3.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.frame_2_3.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2_3.setLineWidth(0)
#         self.frame_2_3.setObjectName("frame_2_3")
#         self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2_3)
#         self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_7.setSpacing(0)
#         self.verticalLayout_7.setObjectName("verticalLayout_7")
#         self.pushButton_2_3_1 = QtWidgets.QPushButton(self.frame_2_3)
#         self.pushButton_2_3_1.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_2_3_1.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_2_3_1.setObjectName("pushButton_2_3_1")
#         self.verticalLayout_7.addWidget(self.pushButton_2_3_1)
#         self.pushButton_2_3_2 = QtWidgets.QPushButton(self.frame_2_3)
#         self.pushButton_2_3_2.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_2_3_2.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_2_3_2.setObjectName("pushButton_2_3_2")
#         self.verticalLayout_7.addWidget(self.pushButton_2_3_2)
#         self.pushButton_2_3_3 = QtWidgets.QPushButton(self.frame_2_3)
#         self.pushButton_2_3_3.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_2_3_3.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_2_3_3.setObjectName("pushButton_2_3_3")
#         self.verticalLayout_7.addWidget(self.pushButton_2_3_3)
#         self.pushButton_2_3_4 = QtWidgets.QPushButton(self.frame_2_3)
#         self.pushButton_2_3_4.setMinimumSize(QtCore.QSize(0, 25))
#         self.pushButton_2_3_4.setStyleSheet("font-family: PingFang SC;\n"
# "font-style: normal;\n"
# "font-weight: 300;\n"
# "font-size: 12px;\n"
# "line-height: 17px;\n"
# "color: rgba(255, 255, 255, 0.7);")
#         self.pushButton_2_3_4.setObjectName("pushButton_2_3_4")
#         self.verticalLayout_7.addWidget(self.pushButton_2_3_4)
#         self.verticalLayout_6.addWidget(self.frame_2_3)
#         self.verticalLayout_5.addWidget(self.frame_2_2)
#         self.verticalLayout_8.addWidget(self.frame_2_1)

        # QtWidgets.QApplication.processEvents()








