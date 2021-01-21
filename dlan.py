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

        self.side_bar_info = [
            {
                "常规检查": [
                    {"终端基本信息": ["主机信息", "硬盘信息", "主机信息", "硬盘信息",
                                "主机信息", "硬盘信息", "主机信息", "硬盘信息", ]},
                    {"USB设备检查": ["存储设备", "其他设备"]},
                    {"终端基本信息": ["主机信息", "硬盘信息"]},
                    {"USB设备检查": ["存储设备", "其他设备"]},
                    {"终端基本信息": ["主机信息", "硬盘信息"]},
                    {"USB设备检查": ["存储设备", "其他设备"]},
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
            "default": "default.png"
        }

        for i in range(len(self.side_bar_info)):
            for key in self.side_bar_info[i]:
                print(key, i)
                self.create_high_frame("self.frame"+"_"+str(i), "self.verticalLayout"+"_"+str(i), "self.pushButton"+"_"+str(i))
                self.item_flag = 0
                if key in self.pushButton_icon:
                    self.icon_src = self.pushButton_icon[key]
                else:
                    self.icon_src = self.pushButton_icon["default"]

                iconLabel = "self.iconLabel"+"_pushButton"+"_"+str(i)
                textLabel = "self.textLabel"+"_pushButton"+"_"+str(i)
                myLayout = "self.myLayout"+"_pushButton"+"_"+str(i)
                self.side_bar_button_layout(iconLabel, textLabel, myLayout, key,30)
                eval("self.pushButton"+"_"+str(i)).setLayout(eval(myLayout))

                for j in range(len(self.side_bar_info[i][key])):
                    for key1 in self.side_bar_info[i][key][j]:
                        if key1 in self.pushButton_icon:
                            self.icon_src = self.pushButton_icon[key1]
                        else:
                            self.icon_src = self.pushButton_icon["default"]
                        self.create_med_frame("self.frame"+"_"+str(i)+"_"+str(j), "self.verticalLayout"+"_"+str(i)+"_"+str(j), "self.pushButton"+"_"+str(i)+"_"+str(j), str(i))
                        iconLabel = "self.iconLabel" + "_pushButton"+"_"+str(i)+"_"+str(j)
                        textLabel = "self.textLabel" + "_pushButton"+"_"+str(i)+"_"+str(j)
                        myLayout = "self.myLayout" + "_pushButton"+"_"+str(i)+"_"+str(j)
                        self.side_bar_button_layout(iconLabel, textLabel, myLayout, key1,50)
                        eval("self.pushButton"+"_"+str(i)+"_" +str(j)).setLayout(eval(myLayout))

                        for k in range(len(self.side_bar_info[i][key][j][key1])):
                            if self.side_bar_info[i][key][j][key1][k] in self.pushButton_icon:
                                self.icon_src = self.pushButton_icon[self.side_bar_info[i][key][j][key1][k]]
                            else:
                                self.icon_src = self.pushButton_icon["default"]
                            self.create_low_frame("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k), str(i), str(j))
                            iconLabel = "self.iconLabel"+"_pushButton" + "_"+str(i)+"_"+str(j)+"_"+str(k)
                            textLabel = "self.textLabel"+"_pushButton" + "_"+str(i)+"_"+str(j)+"_"+str(k)
                            myLayout = "self.myLayout"+"_pushButton" + "_"+str(i)+"_"+str(j)+"_"+str(k)
                            self.side_bar_button_layout(iconLabel, textLabel, myLayout, self.side_bar_info[i][key][j][key1][k],70)
                            eval("self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k)).setLayout(eval(myLayout))
                        self.item_flag = self.item_flag+1

        self.status_bar()

    def side_bar_button_layout(self, iconLabel, textLabel, myLayout, text,spacing):
        exec(iconLabel+"= QtWidgets.QLabel()")
        exec(textLabel+"= QtWidgets.QLabel()")
        eval(iconLabel).setFixedSize(25, 30)
        eval(textLabel).setFixedWidth(150)
        eval(iconLabel).setPixmap(QtGui.QPixmap(self.icon_src))
        eval(textLabel).setText(text)
        exec(myLayout+"= QtWidgets.QHBoxLayout()")
        eval(myLayout).setContentsMargins(0, 0, 0, 0)
        eval(myLayout).setSpacing(0)
        eval(myLayout).addSpacing(spacing)
        eval(myLayout).addWidget(eval(iconLabel))
        eval(myLayout).addSpacing(0)
        eval(myLayout).addWidget(eval(textLabel))
        eval(myLayout).addStretch()

    def create_high_frame(self, frame, verticalLayout, pushButton):
        exec(frame+" = QtWidgets.QFrame(self.frame_dingji)")
        eval(frame).setFrameShape(QtWidgets.QFrame.NoFrame)
        eval(frame).setFrameShadow(QtWidgets.QFrame.Raised)
        eval(frame).setLineWidth(0)
        eval(frame).setObjectName(frame[5:])
        self.verticalLayout_8.addWidget(eval(frame))

        exec(verticalLayout+"= QtWidgets.QVBoxLayout(" + frame + "  )")
        eval(verticalLayout).setContentsMargins(0, 0, 0, 0)
        eval(verticalLayout).setSpacing(0)
        eval(verticalLayout).setObjectName(verticalLayout[5:])

        exec(pushButton+"= QtWidgets.QPushButton("+frame+")")
        eval(pushButton).setMinimumSize(QtCore.QSize(0, 40))
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

    def create_med_frame(self, frame, verticalLayout, pushButton, i):
        str_med_frame = 'self.frame'+'_'+i
        exec(frame+" = QtWidgets.QFrame( "+str_med_frame+"  )")
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

        str_item_flag = str(self.item_flag)
        str_med_frame = frame+"_" + str_item_flag + \
            " = QtWidgets.QFrame("+frame+")"
        exec(str_med_frame)
        eval(frame+"_"+str(self.item_flag)
             ).setFrameShape(QtWidgets.QFrame.NoFrame)
        eval(frame+"_"+str(self.item_flag)
             ).setFrameShadow(QtWidgets.QFrame.Raised)
        eval(frame+"_"+str(self.item_flag)).setLineWidth(0)
        eval(frame+"_"+str(self.item_flag)
             ).setObjectName((frame+"_"+str(self.item_flag))[5:])
        eval(verticalLayout).addWidget(eval(frame+"_"+str(self.item_flag)))
        exec(verticalLayout+"_" + str_item_flag +
             " = QtWidgets.QVBoxLayout("+frame+'_'+str_item_flag+")")
        eval(verticalLayout+"_"+str(self.item_flag)
             ).setContentsMargins(0, 0, 0, 0)
        eval(verticalLayout+"_"+str(self.item_flag)).setSpacing(0)
        eval(verticalLayout+"_"+str(self.item_flag)
             ).setObjectName((verticalLayout+"_"+str(self.item_flag))[5:])

    def create_low_frame(self, pushButton, i, j):

        str_item_flag = str(self.item_flag)
        exec(pushButton+"=QtWidgets.QPushButton(   self.frame_" +
             i+'_'+j+'_' + str_item_flag+")")
        eval(pushButton).setMinimumSize(QtCore.QSize(0, 25))
        eval(pushButton).setStyleSheet("font-family: PingFang SC;\n"
                                       "font-style: normal;\n"
                                       "font-weight: 300;\n"
                                       "font-size: 12px;\n"
                                       "line-height: 17px;\n"
                                       "color: rgba(255, 255, 255, 0.7);")
        eval(pushButton).setFlat(False)
        eval(pushButton).setObjectName(pushButton[5:])
        eval("self.verticalLayout"+"_"+str(i)+"_"+str(j)+"_" +
             str(self.item_flag)).addWidget(eval(pushButton))

    def status_bar(self):

        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
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
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_zhuangtai.sizePolicy().hasHeightForWidth())
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
        self.label_2.setAlignment(
            QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.frame_zhuangtai)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.frame_zhuangtai)
        self.label_2.setText("版权所有：帝岚科技计算机终端保密检查系统")
        self.label_3.setText("电话：029-999987656")
        self.label_5.setText("本机用户名：administration")
        self.label_4.setText("IP地址：198.888.111.09")
        self.label_6.setText("计算机密级：涉密计算机（秘密）")
