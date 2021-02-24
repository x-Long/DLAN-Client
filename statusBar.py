from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
# from dlan import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys

from requests_manager import RequestManager


class Status_bar(object):

    def set_up_status_bar(self):

        self.status_bar_ui()
        # self.status_bar_func()
        self.thread_get_status_bar()


    def status_bar_ui(self):
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_dingji)

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

    def thread_get_status_bar(self):

        self.thread_status_bar = Runthread_status() # 创建线程
        self.thread_status_bar._signal_status.connect(self.get_status) # 连接信号
        self.thread_status_bar.start() # 开始线程
    def get_status(self,status_bar_info):
        self.label_2.setText("版权所有："+status_bar_info["copyright"])
        self.label_3.setText("电话："+status_bar_info["phone_number"])
        self.label_5.setText("本机用户名："+status_bar_info["current_user"])
        self.label_4.setText("IP地址："+status_bar_info["ip_addr"])
        self.label_6.setText("计算机密级："+status_bar_info["security_level"]+"    ")


class Runthread_status(QtCore.QThread):

    _signal_status = pyqtSignal(dict)

    def __init__(self,parent=None):
        super(Runthread_status, self).__init__(parent)

    def run(self):
        status_bar_info = RequestManager.make_get_request('/v1.0/app/footer/info')
        self._signal_status.emit(status_bar_info)
