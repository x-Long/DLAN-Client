# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DLAN-2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import * 


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(1113, 730)
        Form.setMinimumHeight(800)
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
                    {"终端基本信息": ["主机信息", "硬盘信息", "操作系统","身份鉴别",  ]},
                    {"USB设备检查": ["存储设备", "其他设备",]},
                    {"联网设备检查": ["浏览器记录", "cookies记录","上网软件记录","邮件收发记录","终端外联状态"]},
                    {"软件安装检查": ["软件系统", "邮件客户端","虚拟机软件","杀毒软件信息","反取证软件检查"]},
                    {"其他辅助检查": ["文件使用记录", "开关机记录"]},
                ]
            },
            {
                "安全检查": [
                    {"系统安全检查": ["三合一”客户端", "系统共享安全 ", "无线通信模块", "音频视频模块", "操作系统补丁","系统进程信息 " ]},
                    {"安全配置检查": ["安全审计配置", "账户安全配置", "账户权限配置", "系统服务配置", "系统端口配置", ]},
                ]
            },
            {
                "文件检查": [
                    {"常规文件": ["常规文件检查 ", ]},
                    {"图片文件": ["图片文件检查", ]},
                ]
            },
            {
                "深度检查": [
                    {"使用记录检查": ["USB设备记录 ","历史上网记录","文件操作记录" ]},
                    {"文件恢复检查": ["删除文件恢复", "文件碎片恢复"]},
                ]
            },           
            {
                "本机报告": [
                    {"总体检查报告": []},
                    {"文件检查报告": []},
                    {"人工检查报告": []},
                    {"详细检查报告": []},
                    {"二维码报告": []},
                ]
            },     
        ]
        self.pushButton_icon = {
            "常规检查": "./icon/1.png",
            "终端基本信息": "./icon/two.png",
            "USB设备检查": "./icon/two.png",
            "联网设备检查": "./icon/two.png",
            "软件安装检查": "./icon/two.png",
            "其他辅助检查": "./icon/two.png",
            "安全检查": "./icon/2.png",
            "系统安全检查": "./icon/two.png",
            "安全配置检查": "./icon/two.png",
            "文件检查": "./icon/3.png",
            "常规文件": "./icon/two.png",
            "图片文件": "./icon/two.png",
            "深度检查": "./icon/4.png",
            "使用记录检查": "./icon/two.png",
            "文件恢复检查": "./icon/two.png",
            "本机报告": "./icon/5.png",
            "default": "./icon/Vector.png"
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

                arrow = QtWidgets.QLabel()
                arrow.setFixedSize(25, 30)
                arrow.setPixmap(QtGui.QPixmap("./icon/close.png"))
                eval(myLayout).addWidget(arrow)

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


                        arrow = QtWidgets.QLabel()
                        arrow.setFixedSize(25, 30)
                        arrow.setPixmap(QtGui.QPixmap("./icon/open.png"))
                        eval(myLayout).addWidget(arrow)

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
        self.stackedWidgets()

    def side_bar_button_layout(self, iconLabel, textLabel, myLayout, text,spacing):
        exec(iconLabel+"= QtWidgets.QLabel()")
        exec(textLabel+"= QtWidgets.QLabel()")

        eval(iconLabel).setFixedSize(25, 20)

        eval(textLabel).setFixedWidth(100)

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
                                       "font-family: Microsoft YaHei;\n"
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
        eval(pushButton).setStyleSheet("font-family: Microsoft YaHei;\n"
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
        eval(pushButton).setStyleSheet("font-family: Microsoft YaHei;\n"
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




        # self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        # self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.stackedWidget.setLineWidth(0)
        # self.stackedWidget.setObjectName("stackedWidget")
        # self.page = QtWidgets.QWidget()
        # self.page.setObjectName("page")
        # self.stackedWidget.addWidget(self.page)
        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)
        # self.horizontalLayout.addWidget(self.stackedWidget)



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
                                           "font-family: Microsoft YaHei;\n"
                                           "font-style: normal;\n"
                                           "font-weight: 300;\n"
                                           "font-size: 12px;\n"
                                           "line-height: 17px;\n"
                                           "color: rgba(255, 255, 255, 1);\n"
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
        self.label_2.setText("版权所有：帝岚科技 ")
        self.label_3.setText("电话：029-999987656 ")
        self.label_5.setText("本机用户名：administration ")
        self.label_4.setText("IP地址：198.888.111.09 ")
        self.label_6.setText("计算机密级：涉密计算机（秘密） ")



    def stackedWidgets(self):
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("QWidget#page{\n"
                                "background: #E5E5E5;\n"
                                "\n"
                                "\n"
                                "}")
        self.page.setObjectName("page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_progress = QtWidgets.QFrame(self.page)
        self.frame_progress.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progress.setObjectName("frame_progress")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_progress)
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_progress_time = QtWidgets.QLabel(self.frame_progress)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_progress_time.sizePolicy().hasHeightForWidth())
        self.label_progress_time.setSizePolicy(sizePolicy)
        self.label_progress_time.setMinimumSize(QtCore.QSize(60, 0))
        self.label_progress_time.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_progress_time.setStyleSheet("font-family: Metropolis;\n"
                                               "font-size: 18px;\n"
                                               "line-height: 28px;\n"
                                               "font-weight: 800;\n"
                                               "\n"
                                               "color: #565656;")
        self.label_progress_time.setObjectName("label_progress_time")
        self.horizontalLayout_9.addWidget(self.label_progress_time)
        self.progressBar = QtWidgets.QProgressBar(self.frame_progress)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 15))
        self.progressBar.setStyleSheet("QProgressBar{\n"
                                       "\n"
                                       "background-color: #DEDEDE; \n"
                                       "height:12px;\n"
                                       "border-radius: 8px;\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QProgressBar::chunk{\n"
                                       "background-color: #83C088; \n"
                                       "border-radius: 6px;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       " ")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.label_21 = QtWidgets.QLabel(self.frame_progress)
        self.label_21.setMinimumSize(QtCore.QSize(50, 0))
        self.label_21.setStyleSheet("font-family: Metropolis;\n"
                                    "font-size: 18px;\n"
                                    "line-height: 28px;\n"
                                    "font-weight: 800;\n"
                                    "\n"
                                    "color: #565656;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.pushButton_pause = QtWidgets.QPushButton(self.frame_progress)
        self.pushButton_pause.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_pause.setStyleSheet("background: #3A7FED;\n"
                                            "font-family: PingFang SC;\n"
                                            "font-style: normal;\n"
                                            "font-weight: normal;\n"
                                            "font-size: 14px;\n"
                                            "line-height: 20px;\n"
                                            "border-radius: 3px;\n"
                                            "\n"
                                            "color: #FFFFFF;")
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.horizontalLayout_9.addWidget(self.pushButton_pause)
        self.pushButton_stop = QtWidgets.QPushButton(self.frame_progress)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_stop.setStyleSheet("background: #3A7FED;\n"
                                           "font-family: PingFang SC;\n"
                                           "font-style: normal;\n"
                                           "font-weight: normal;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 20px;\n"
                                           "border-radius: 3px;\n"
                                           "\n"
                                           "color: #FFFFFF;")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_9.addWidget(self.pushButton_stop)
        self.verticalLayout_9.addWidget(self.frame_progress)
        self.scrollArea_content = QtWidgets.QScrollArea(self.page)
        self.scrollArea_content.setStyleSheet("QScrollArea{\n"
                                              "border: 0px solid;\n"
                                              "border-right-width: 1px;\n"
                                              "border-right-color: #dcdbdc;\n"
                                              "\n"
                                              "}\n"
                                              "QScrollBar:vertical {\n"
                                              "border: none;\n"
                                              "background: #f5f5f7;\n"
                                              "width: 10px;\n"
                                              "margin: 0px 0 0px 0;\n"
                                              "}\n"
                                              "QScrollBar::handle:vertical {\n"
                                              "background: Gainsboro;\n"
                                              "min-height: 20px;\n"
                                              "border-radius: 5px;\n"
                                              "border: none;\n"
                                              "}\n"
                                              "QScrollBar::add-line:vertical {\n"
                                              "border: 0px solid grey;\n"
                                              "background: #32CC99;\n"
                                              "height: 0px;\n"
                                              "subcontrol-position: bottom;\n"
                                              "subcontrol-origin: margin;\n"
                                              "}\n"
                                              "QScrollBar::sub-line:vertical {\n"
                                              "border: 0px solid grey;\n"
                                              "background: #32CC99;\n"
                                              "height: 0px;\n"
                                              "subcontrol-position: top;\n"
                                              "subcontrol-origin: margin;\n"
                                              "}\n"
                                              "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                              "background: none;\n"
                                              "width: 0px;\n"
                                              "height: 0px;\n"
                                              "}")
        self.scrollArea_content.setWidgetResizable(True)
        self.scrollArea_content.setObjectName("scrollArea_content")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(
            QtCore.QRect(0, 0, 919, 696))
        self.scrollAreaWidgetContents_3.setObjectName(
            "scrollAreaWidgetContents_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_3)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame.setStyleSheet("QFrame#frame{\n"
                                 "border-radius: 3px;\n"
                                 "background: #F6F6F6;\n"
                                 "\n"
                                 "border:2px solid rgba(0, 0, 0, 0.1);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("font-family: Microsoft YaHei;\n"
                                   "font-style: normal;\n"
                                   "font-weight: 600;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 22px;\n"
                                   "background: #FFFFFF;\n"
                                   "\n"
                                   "color: #565656;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setStyleSheet("color:rgba(86, 86, 86, 0.2);\n"
                                   "font-size: 20px;\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_10.addWidget(self.frame_2)

        self.pushButton_computer_info = QtWidgets.QToolButton(self.frame)
        self.pushButton_computer_info.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.pushButton_computer_info.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
        self.pushButton_computer_info.setIcon(QtGui.QIcon("./icon/info.png"))

        self.pushButton_computer_info.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_computer_info.setStyleSheet("background: #FFFFFF;\n"
                                                    "border:2px solid rgba(0, 0, 0, 0.1);\n"
                                                    "border-left:4px solid #256CDD;\n"
                                                    "border-right:0px;\n"
                                                    "font-family: MICsoft YAHEi;\n"
                                                    "font-style: normal;\n"
                                                    "font-weight: 500;\n"
                                                    "font-size: 14px;\n"
                                                    "line-height: 20px;\n"
                                                    "/* identical to box height */\n"
                                                    "color: #256CDD;\n"
                                                    "text-align : left;"
                                                    )
        self.pushButton_computer_info.setObjectName("pushButton_computer_info")




        self.verticalLayout_10.addWidget(self.pushButton_computer_info)
        self.frame_computer_info = QtWidgets.QFrame(self.frame)
        self.frame_computer_info.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_computer_info.setStyleSheet("font-family: Microsoft YaHei;\n"
                                               "font-style: normal;\n"
                                               "font-weight: 300;\n"
                                               "font-size: 14px;\n"
                                               "line-height: 20px;\n"
                                               "/* identical to box height */\n"
                                               "\n"
                                               "\n"
                                               "color: #565656;\n"
                                               "")
        self.frame_computer_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_computer_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_computer_info.setObjectName("frame_computer_info")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(
            self.frame_computer_info)
        self.verticalLayout_11.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_4 = QtWidgets.QFrame(self.frame_computer_info)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.verticalLayout_11.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_computer_info)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.verticalLayout_11.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_computer_info)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_computer_info)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.frame_7)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.verticalLayout_11.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_computer_info)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.frame_8)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.frame_8)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.verticalLayout_11.addWidget(self.frame_8)
        self.verticalLayout_10.addWidget(self.frame_computer_info)



        self.pushButton_net_info = QtWidgets.QToolButton(self.frame)
        self.pushButton_net_info.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.pushButton_net_info.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
        self.pushButton_net_info.setIcon(QtGui.QIcon("./icon/info.png"))

        self.pushButton_net_info.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_net_info.setStyleSheet("background: #FFFFFF;\n"
                                               "border:2px solid rgba(0, 0, 0, 0.1);\n"
                                               "border-left:4px solid #256CDD;\n"
                                               "border-right:0px;\n"
                                               "font-family: MICsoft YAHEi;\n"
                                               "font-style: normal;\n"
                                               "font-weight: 500;\n"
                                               "font-size: 14px;\n"
                                               "line-height: 20px;\n"
                                               "/* identical to box height */\n"
                                               "color: #256CDD;\n"
                                               "text-align : left;")
        self.pushButton_net_info.setObjectName("pushButton_net_info")

        self.verticalLayout_10.addWidget(self.pushButton_net_info)
        self.frame_net_info = QtWidgets.QFrame(self.frame)
        self.frame_net_info.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_net_info.setStyleSheet("font-family: Microsoft YaHei;\n"
                                          "font-style: normal;\n"
                                          "font-weight: 300;\n"
                                          "font-size: 14px;\n"
                                          "line-height: 20px;\n"
                                          "/* identical to box height */\n"
                                          "\n"
                                          "\n"
                                          "color: #565656;\n"
                                          "")
        self.frame_net_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_net_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_net_info.setObjectName("frame_net_info")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_net_info)
        self.verticalLayout_19.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_28 = QtWidgets.QFrame(self.frame_net_info)
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_26.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_54 = QtWidgets.QLabel(self.frame_28)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_26.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.frame_28)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_26.addWidget(self.label_55)
        self.verticalLayout_19.addWidget(self.frame_28)
        self.frame_29 = QtWidgets.QFrame(self.frame_net_info)
        self.frame_29.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_27.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_56 = QtWidgets.QLabel(self.frame_29)
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_27.addWidget(self.label_56)
        self.label_57 = QtWidgets.QLabel(self.frame_29)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_27.addWidget(self.label_57)
        self.verticalLayout_19.addWidget(self.frame_29)
        self.frame_30 = QtWidgets.QFrame(self.frame_net_info)
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_28.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_58 = QtWidgets.QLabel(self.frame_30)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_28.addWidget(self.label_58)
        self.label_59 = QtWidgets.QLabel(self.frame_30)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_28.addWidget(self.label_59)
        self.verticalLayout_19.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_net_info)
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_29.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_60 = QtWidgets.QLabel(self.frame_31)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_29.addWidget(self.label_60)
        self.label_61 = QtWidgets.QLabel(self.frame_31)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_29.addWidget(self.label_61)
        self.verticalLayout_19.addWidget(self.frame_31)
        self.frame_32 = QtWidgets.QFrame(self.frame_net_info)
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_30.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_62 = QtWidgets.QLabel(self.frame_32)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_30.addWidget(self.label_62)
        self.label_63 = QtWidgets.QLabel(self.frame_32)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_30.addWidget(self.label_63)
        self.verticalLayout_19.addWidget(self.frame_32)
        self.verticalLayout_10.addWidget(self.frame_net_info)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 316, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.verticalLayout_16.addWidget(self.frame)
        self.scrollArea_content.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_content)
        self.stackedWidget.addWidget(self.page)


        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        # 设置填充信息

        self.label_progress_time.setText("02:00")
        self.label_21.setText("100%")
        self.pushButton_pause.setText("暂停检查")
        self.pushButton_stop.setText("停止检查")
        self.label_7.setText("         项目")
        self.label_8.setText("|")
        self.label_9.setText("  基本信息")
        self.pushButton_computer_info.setText("计算机信息")
        self.label_12.setText("电脑类型")
        self.label_10.setText("VivoBook")
        self.label_13.setText("主板型号")
        self.label_15.setText(
            "ASUST eK COMPUTER INC. - X542UF")
        self.label_14.setText("光驱信息")
        self.label_16.setText("无光驱")
        self.label_17.setText("内存信息")
        self.label_18.setText("8000MB")
        self.label_19.setText("处理器")
        self.label_20.setText(
            "Inter(R) Core(TM) i7-8550U CPU 1.8GHz")
        self.pushButton_net_info.setText("网络信息")
        self.label_54.setText("电脑类型")
        self.label_55.setText("VivoBook")
        self.label_56.setText("主板型号")
        self.label_57.setText(
            "ASUST eK COMPUTER INC. - X542UF")
        self.label_58.setText("光驱信息")
        self.label_59.setText("无光驱")
        self.label_60.setText("内存信息")
        self.label_61.setText("8000MB")
        self.label_62.setText("处理器")
        self.label_63.setText(
            "Inter(R) Core(TM) i7-8550U CPU 1.8GHz")


        ###############################