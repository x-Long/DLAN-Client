from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
# from dlan import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys


class Side_bar(object):
    # def __init__(self, parent=None):
    #     super().__init__(parent)

    def set_up_side_bar(self):

        side_bar_config = json.load(
            open("side_bar_info.json", encoding='utf8'))
        self.side_bar_info = side_bar_config["side_bar_info"]
        self.pushButton_icon = side_bar_config["pushButton_icon"]

        self.side_bar_ui()
        self.side_bar_func()

    def side_bar_ui(self):

        self.frame_dingji = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_dingji.sizePolicy().hasHeightForWidth())
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
        self.three_pushButton = []

        for i in range(len(self.side_bar_info)):
            for key in self.side_bar_info[i]:
                print(key, i)
                self.create_high_frame(
                    "self.frame"+"_"+str(i), "self.verticalLayout"+"_"+str(i), "self.pushButton"+"_"+str(i))
                self.item_flag = 0
                if key in self.pushButton_icon:
                    self.icon_src = self.pushButton_icon[key]
                else:
                    self.icon_src = self.pushButton_icon["default"]

                iconLabel = "self.iconLabel"+"_pushButton"+"_"+str(i)
                textLabel = "self.textLabel"+"_pushButton"+"_"+str(i)
                myLayout = "self.myLayout"+"_pushButton"+"_"+str(i)
                self.side_bar_button_layout(
                    iconLabel, textLabel, myLayout, key, 30)
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
                        self.create_med_frame("self.frame"+"_"+str(i)+"_"+str(j), "self.verticalLayout"+"_"+str(
                            i)+"_"+str(j), "self.pushButton"+"_"+str(i)+"_"+str(j), str(i))
                        iconLabel = "self.iconLabel" + \
                            "_pushButton"+"_"+str(i)+"_"+str(j)
                        textLabel = "self.textLabel" + \
                            "_pushButton"+"_"+str(i)+"_"+str(j)
                        myLayout = "self.myLayout" + \
                            "_pushButton"+"_"+str(i)+"_"+str(j)
                        self.side_bar_button_layout(
                            iconLabel, textLabel, myLayout, key1, 50)
                        eval("self.pushButton"+"_"+str(i)+"_" +
                             str(j)).setLayout(eval(myLayout))

                        arrow = QtWidgets.QLabel()
                        arrow.setFixedSize(25, 30)
                        arrow.setPixmap(QtGui.QPixmap("./icon/open.png"))
                        eval(myLayout).addWidget(arrow)

                        for k in range(len(self.side_bar_info[i][key][j][key1])):
                            if self.side_bar_info[i][key][j][key1][k] in self.pushButton_icon:
                                self.icon_src = self.pushButton_icon[self.side_bar_info[i]
                                                                     [key][j][key1][k]]
                            else:
                                self.icon_src = self.pushButton_icon["default"]
                            self.create_low_frame(
                                "self.pushButton"+"_"+str(i)+"_"+str(j)+"_"+str(k), str(i), str(j))
                            iconLabel = "self.iconLabel"+"_pushButton" + \
                                "_"+str(i)+"_"+str(j)+"_"+str(k)
                            textLabel = "self.textLabel"+"_pushButton" + \
                                "_"+str(i)+"_"+str(j)+"_"+str(k)
                            myLayout = "self.myLayout"+"_pushButton" + \
                                "_"+str(i)+"_"+str(j)+"_"+str(k)
                            self.side_bar_button_layout(
                                iconLabel, textLabel, myLayout, self.side_bar_info[i][key][j][key1][k], 70)
                            eval("self.pushButton"+"_"+str(i)+"_" +
                                 str(j)+"_"+str(k)).setLayout(eval(myLayout))

                            self.three_pushButton.append(
                                "self.pushButton"+"_"+str(i)+"_" + str(j)+"_"+str(k))

                        self.item_flag = self.item_flag+1

    def side_bar_button_layout(self, iconLabel, textLabel, myLayout, text, spacing):
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
        eval(pushButton).clicked.connect(
            lambda: self.change_big_pushbutton_style(pushButton))
        eval(pushButton).setCursor(QCursor(Qt.PointingHandCursor))

        eval(pushButton).setAutoDefault(False)
        eval(pushButton).setFlat(False)
        eval(pushButton).setObjectName(pushButton[5:])
        eval(verticalLayout).addWidget(eval(pushButton))

    def change_big_pushbutton_style(self, pushButton):
        for i in self.side_bar_widgets:
            eval(i[0]).setStyleSheet("background: #17376A;\n"
                                     "border-bottom: 1px solid #29407C;\n"
                                     "font-family: Microsoft YaHei;\n"
                                     "font-style: normal;\n"
                                     "font-weight: 600;\n"
                                     "font-size: 14px;\n"
                                     "line-height: 20px;\n"
                                     "\n"
                                     "color: #FFFFFF;\n"
                                     "")

        eval(pushButton).setStyleSheet("background: #256CDD;\n"
                                       "border-bottom: 1px solid #29407C;\n"
                                       "font-family: Microsoft YaHei;\n"
                                       "font-style: normal;\n"
                                       "font-weight: 600;\n"
                                       "font-size: 14px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;\n"
                                       "")

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
        eval(pushButton).setStyleSheet(
            "QPushButton QLabel{  "
            "font-family: Microsoft YaHei;\n"
            "font-style: normal;\n"
            "font-weight: 300;\n"
            "font-size: 12px;\n"
            "line-height: 17px;\n"
            "color: rgba(255, 255, 255, 0.7);"
            " } "
            #            "QPushButton QLabel:hover {  "
            #         # "background:rgb(40,85,20); "
            #        "color: rgba(255, 255, 255, 0.7);"
            #    " } "
        )
        eval(pushButton).setCursor(QCursor(Qt.PointingHandCursor))
        eval(pushButton).clicked.connect(
            lambda: self.change_small_pushbutton_style(pushButton))

        eval(pushButton).setFlat(False)
        eval(pushButton).setObjectName(pushButton[5:])
        eval("self.verticalLayout"+"_"+str(i)+"_"+str(j)+"_" +
             str(self.item_flag)).addWidget(eval(pushButton))

    def change_small_pushbutton_style(self, pushButton):
        for i in self.three_pushButton:
            eval(i).setStyleSheet(
                "QPushButton QLabel{  "
                "font-family: Microsoft YaHei;\n"
                "font-style: normal;\n"
                "font-weight: 300;\n"
                "font-size: 12px;\n"
                "line-height: 17px;\n"
                "color: rgba(255, 255, 255, 0.7);"
                " } "
            )
        eval(pushButton).setStyleSheet(
            "QPushButton QLabel{  "
            "font-family: Microsoft YaHei;\n"
            "font-style: normal;\n"
            "font-weight: 300;\n"
            "font-size: 12px;\n"
            "line-height: 17px;\n"
            "color: #1FBADE;;"
            " } "
        )
# --------------------------ui结束

    def side_bar_func(self):
        self.is_display = []
        self.is_hide = []
        self.side_bar_widgets = []
        self.get_side_bar_wifgets()
        self.side_bar_bind_event()

    def get_side_bar_wifgets(self):
        for i in range(len(self.side_bar_info)):
            high_level_pushButton = ""
            med_level_pushButton = []
            high_level_frame = []
            low_level_frame = []

            for key in self.side_bar_info[i]:

                print(key, i)
                self.item_flag = 0
                high_level_pushButton = "self.pushButton"+"_"+str(i)

                for j in range(len(self.side_bar_info[i][key])):
                    for key1 in self.side_bar_info[i][key][j]:

                        print(key1, str(i), j)
                        high_level_frame.append(
                            "self.frame"+"_"+str(i)+"_"+str(j))
                        med_level_pushButton.append(
                            "self.pushButton"+"_"+str(i)+"_"+str(j))

                        for k in range(len(self.side_bar_info[i][key][j][key1])):
                            print(self.side_bar_info[i]
                                  [key][j][key1][k], i, j, k,)

                        low_level_frame.append(
                            "self.frame"+"_"+str(i)+"_"+str(j)+"_"+str(self.item_flag))

                        self.item_flag = self.item_flag+1
                        print(self.item_flag)
            temp = []
            temp.append(high_level_pushButton)
            temp.append(high_level_frame)
            temp.append(med_level_pushButton)
            temp.append(low_level_frame)
            self.side_bar_widgets.append(temp)

    def side_bar_bind_event(self):
        for k in range(len(self.side_bar_widgets)):
            self.high_level_button_event(k)
            for h in self.side_bar_widgets[k][1]:
                self.hide_frame(h)
            for f in range(len(self.side_bar_widgets[k][2])):
                print(self.side_bar_widgets[k][2][f])
                self.low_level_button_event(k, f)

    def resizeEvent(self, event):
        #更新窗体大小事件
        self.message = "窗口大小调整为：QSize({0},{1})".format(
            event.size().width(), event.size().height())
        self.frame_dingji.setMaximumHeight(event.size().height()-30)
        self.update()

    def high_level_button_event(self, k):
        print("self.side_bar_widgets[k][0]", self.side_bar_widgets[k][0])
        eval(self.side_bar_widgets[k][0]).clicked.connect(
            lambda: self.high_frame_res(self.side_bar_widgets[k][1], k))

    def hide_frame(self, h):
        eval(h).setVisible(False)

    def low_level_button_event(self, k, f):
        eval(self.side_bar_widgets[k][2][f]).clicked.connect(
            lambda: self.low_frame_res(self.side_bar_widgets[k][3][f], k, f))

    def change_arrows(self, wid, status_icon):
        eval(wid).itemAt(eval(wid).count()-1).widget().deleteLater()
        iconLabel = QtWidgets.QLabel()
        iconLabel.setFixedSize(25, 30)
        iconLabel.setPixmap(QtGui.QPixmap(status_icon))
        eval(wid).addWidget(iconLabel)

    def high_frame_res(self, frame_items, k):
        # print(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).count())
        # for i in range(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).count()):
        #     print(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).itemAt(i).widget().deleteLater(),11111111111111111)

        # eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).itemAt(eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).count()-1).widget().deleteLater()

        if eval(frame_items[0]).isVisible():
            self.change_arrows(
                "self.myLayout"+"_"+self.side_bar_widgets[k][0][5:], "./icon/close.png")
            # iconLabel = QtWidgets.QLabel()
            # iconLabel.setFixedSize(25, 30)
            # iconLabel.setPixmap(QtGui.QPixmap("./icon/close.png"))
            # eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).addWidget(iconLabel)
        else:

            self.change_arrows(
                "self.myLayout"+"_"+self.side_bar_widgets[k][0][5:], "./icon/open.png")
            # iconLabel= QtWidgets.QLabel()
            # iconLabel.setFixedSize(25, 30)
            # iconLabel.setPixmap(QtGui.QPixmap("./icon/open.png"))
            # eval("self.myLayout"+"_"+self.side_bar_widgets[k][0][5:]).addWidget(iconLabel)

        count_clear_istrue = 0
        for frame in frame_items:
            if eval(frame).isVisible():

                eval(frame).setVisible(False)
                for item in self.is_hide:
                    eval(item).setVisible(True)
                    self.change_arrows(
                        "self.myLayout_pushButton_"+item[11:14], "./icon/open.png")
            else:
                if count_clear_istrue == 0:
                    for is_true_item in self.is_display:
                        eval(is_true_item).setVisible(False)
                        print(self.is_display, 2222222222222222222222)
                        print(frame)
                    if len(self.is_display) != 0:
                        self.change_arrows(
                            "self.myLayout_pushButton_"+self.is_display[0][11], "./icon/close.png")
                    self.is_display.clear()
                    count_clear_istrue = count_clear_istrue+1

                eval(frame).setVisible(True)
                self.change_arrows(
                    "self.myLayout"+"_"+self.side_bar_widgets[k][0][5:], "./icon/open.png")

                self.is_display.append(frame)
                for item in self.is_hide:
                    print("item", item)
                    eval(item).setVisible(True)
                    self.change_arrows(
                        "self.myLayout_pushButton_"+item[11:14], "./icon/open.png")

    def low_frame_res(self, frame, k, f):

        eval("self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:]).itemAt(eval(
            "self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:]).count()-1).widget().deleteLater()
        if eval(frame).isVisible():
            self.change_arrows(
                "self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:], "./icon/close.png")
            eval(frame).setVisible(False)
            self.is_hide.append(frame)
        else:
            self.change_arrows(
                "self.myLayout"+"_"+self.side_bar_widgets[k][2][f][5:], "./icon/open.png")
            eval(frame).setVisible(True)
            self.is_hide.remove(frame)
