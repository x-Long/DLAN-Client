from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys
import time
from PyQt5.QtCore import QObject, pyqtSignal


class Runthread_hard_disk_info(QtCore.QThread):

    _signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Runthread_hard_disk_info, self).__init__(parent)

    def run(self):
        # net_info = json.loads(requests.get("http://localhost/v1.0/harddisks/info").content)
        from requests_manager import RequestManager
        net_info=RequestManager.make_get_request('/v1.0/harddisks/info')

        self._signal.emit(net_info)  # 信号发送


class Stacked_page_hard_disk_4(object):

    def set_up_stacked_page_hard_disk_4(self):

        self.stacked_page_hard_disk_4_ui()

        # 界面开始打开线程加载主机信息
        self.thread_page_hard_disk_4()

        self.pushButton_0_0_1.clicked.connect(self.switche_page_hard_disk_4)

    def switche_page_hard_disk_4(self):
        self.stackedWidget.setCurrentIndex(3)

    def thread_page_hard_disk_4(self):

        self.thread_page_hard_disk_4 = Runthread_hard_disk_info()  # 创建线程
        self.thread_page_hard_disk_4._signal.connect(
            self.stacked_page_hard_disk_func)  # 连接信号
        self.thread_page_hard_disk_4.start()  # 开始线程

    def stacked_page_hard_disk_func(self, net_info):

        self.create_hard_disk_info(net_info)

    def info_hard_disk_frame_res(self,frame):

        if frame.isVisible():
            frame.setVisible(False)
        else:
            frame.setVisible(True)

    def create_hard_disk_info(self, net_info):

        for info in net_info:
            self.hard_disk_frame("self.verticalLayout_20",
                                 "型号", info.get("model"))
            self.hard_disk_frame("self.verticalLayout_20",
                                 "序列号", info.get("serials"))
            self.hard_disk_frame("self.verticalLayout_20",
                                 "容量", info.get("capacity"))

    def hard_disk_frame(self, layout, item_name, v):

        frame_33 = QtWidgets.QFrame(self.frame_net_info_2)
        frame_33.setMaximumSize(QtCore.QSize(16777215, 30))
        frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_33.setObjectName("frame_33")

        horizontalLayout_31 = QtWidgets.QHBoxLayout(frame_33)
        horizontalLayout_31.setContentsMargins(0, 2, 0, 2)
        horizontalLayout_31.setSpacing(0)
        horizontalLayout_31.setObjectName("horizontalLayout_31")

        label_76 = QtWidgets.QLabel(frame_33)
        label_76.setObjectName("label_76")
        label_76.setText(item_name)
        horizontalLayout_31.addWidget(label_76)
        label_77 = QtWidgets.QLabel(frame_33)
        label_77.setObjectName("label_77")
        label_77.setText(v)
        horizontalLayout_31.addWidget(label_77)

        horizontalLayout_31.setStretch(0, 1)
        horizontalLayout_31.setStretch(1, 3)
        eval(layout).addWidget(frame_33)
        # 。

        # frame_41 = QtWidgets.QFrame(self.frame_net_info_2)
        # frame_41.setMaximumSize(QtCore.QSize(16777215, 30))
        # frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        # frame_41.setObjectName("frame_41")

        # horizontalLayout_41 = QtWidgets.QHBoxLayout(frame_41)
        # horizontalLayout_41.setContentsMargins(0, 2, 0, 2)
        # horizontalLayout_41.setSpacing(0)
        # horizontalLayout_41.setObjectName("horizontalLayout_41")

        # label_121 = QtWidgets.QLabel(frame_41)
        # label_121.setObjectName("label_121")
        # horizontalLayout_41.addWidget(label_121)
        # label_121.setText(item_name)
        # label_121.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # label_101 = QtWidgets.QLabel(frame_41)
        # label_101.setObjectName("label_101")
        # horizontalLayout_41.addWidget(label_101)
        # label_101.setText(v)
        # label_101.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # horizontalLayout_41.setStretch(0, 1)
        # horizontalLayout_41.setStretch(1, 3)

        # eval(layout).addWidget(frame_41)

    def stacked_page_hard_disk_4_ui(self):

        self.page_hard_disk_info = QtWidgets.QWidget()
        self.page_hard_disk_info.setObjectName("page_hard_disk_info")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(
            self.page_hard_disk_info)
        self.verticalLayout_18.setObjectName("verticalLayout_18")

        self.frame_progress_3 = QtWidgets.QFrame(self.page_hard_disk_info)
        self.frame_progress_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_progress_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progress_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progress_3.setObjectName("frame_progress_3")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_progress_3)
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_progress_time_3 = QtWidgets.QLabel(self.frame_progress_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_progress_time_3.sizePolicy().hasHeightForWidth())
        self.label_progress_time_3.setSizePolicy(sizePolicy)
        self.label_progress_time_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_progress_time_3.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_progress_time_3.setStyleSheet("font-family: Metropolis;\n"
                                                 "font-size: 18px;\n"
                                                 "line-height: 28px;\n"
                                                 "font-weight: 800;\n"
                                                 "\n"
                                                 "color: #565656;")
        self.label_progress_time_3.setObjectName("label_progress_time_3")
        self.horizontalLayout_18.addWidget(self.label_progress_time_3)
        self.progressBar_3 = QtWidgets.QProgressBar(self.frame_progress_3)
        self.progressBar_3.setMinimumSize(QtCore.QSize(0, 15))
        self.progressBar_3.setStyleSheet("QProgressBar{\n"
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
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_18.addWidget(self.progressBar_3)
        self.label_86 = QtWidgets.QLabel(self.frame_progress_3)
        self.label_86.setMinimumSize(QtCore.QSize(50, 0))
        self.label_86.setStyleSheet("font-family: Metropolis;\n"
                                    "font-size: 18px;\n"
                                    "line-height: 28px;\n"
                                    "font-weight: 800;\n"
                                    "\n"
                                    "color: #565656;")
        self.label_86.setObjectName("label_86")
        self.horizontalLayout_18.addWidget(self.label_86)
        self.pushButton_pause_3 = QtWidgets.QPushButton(self.frame_progress_3)
        self.pushButton_pause_3.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_pause_3.setStyleSheet("background: #3A7FED;\n"
                                              "font-family: PingFang SC;\n"
                                              "font-style: normal;\n"
                                              "font-weight: normal;\n"
                                              "font-size: 14px;\n"
                                              "line-height: 20px;\n"
                                              "border-radius: 3px;\n"
                                              "\n"
                                              "color: #FFFFFF;")
        self.pushButton_pause_3.setObjectName("pushButton_pause_3")
        self.horizontalLayout_18.addWidget(self.pushButton_pause_3)
        self.pushButton_stop_3 = QtWidgets.QPushButton(self.frame_progress_3)
        self.pushButton_stop_3.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_stop_3.setStyleSheet("background: #3A7FED;\n"
                                             "font-family: PingFang SC;\n"
                                             "font-style: normal;\n"
                                             "font-weight: normal;\n"
                                             "font-size: 14px;\n"
                                             "line-height: 20px;\n"
                                             "border-radius: 3px;\n"
                                             "\n"
                                             "color: #FFFFFF;")
        self.pushButton_stop_3.setObjectName("pushButton_stop_3")
        self.horizontalLayout_18.addWidget(self.pushButton_stop_3)
        self.verticalLayout_18.addWidget(self.frame_progress_3)

        self.scrollArea_content_2 = QtWidgets.QScrollArea(
            self.page_hard_disk_info)
        self.scrollArea_content_2.setStyleSheet("QScrollArea{\n"
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
        self.scrollArea_content_2.setWidgetResizable(True)
        self.scrollArea_content_2.setObjectName("scrollArea_content_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(
            QtCore.QRect(0, 0, 976, 696))
        self.scrollAreaWidgetContents_4.setObjectName(
            "scrollAreaWidgetContents_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_4)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_9.setStyleSheet("QFrame#frame{\n"
                                   "border-radius: 3px;\n"
                                   "background: #F6F6F6;\n"
                                   "\n"
                                   "border:2px solid rgba(0, 0, 0, 0.1);}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setStyleSheet("font-family: Microsoft YaHei;\n"
                                    "font-style: normal;\n"
                                    "font-weight: 600;\n"
                                    "font-size: 16px;\n"
                                    "line-height: 22px;\n"
                                    "background: #FFFFFF;\n"
                                    "\n"
                                    "color: #565656;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_39 = QtWidgets.QLabel(self.frame_10)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_12.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.frame_10)
        self.label_40.setStyleSheet("color:rgba(86, 86, 86, 0.2);\n"
                                    "font-size: 20px;\n"
                                    "")
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_12.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.frame_10)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_12.addWidget(self.label_41)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(2, 3)
        
        self.verticalLayout_14.addWidget(self.frame_10)
        self.pushButton_net_info_2 = QtWidgets.QToolButton(self.frame_9)

        self.pushButton_net_info_2.setToolButtonStyle(
            Qt.ToolButtonTextBesideIcon)
        self.pushButton_net_info_2.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.pushButton_net_info_2.setIcon(QtGui.QIcon("./icon/info.png"))
        self.pushButton_net_info_2.clicked.connect(lambda: self.info_hard_disk_frame_res(self.frame_net_info_2))

        self.pushButton_net_info_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_net_info_2.setStyleSheet("background: #FFFFFF;\n"
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
        self.pushButton_net_info_2.setObjectName("pushButton_net_info_2")
        self.verticalLayout_14.addWidget(self.pushButton_net_info_2)

        self.frame_net_info_2 = QtWidgets.QFrame(self.frame_9)
        self.frame_net_info_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_net_info_2.setStyleSheet("font-family: Microsoft YaHei;\n"
                                            "font-style: normal;\n"
                                            "font-weight: 300;\n"
                                            "font-size: 14px;\n"
                                            "line-height: 20px;\n"
                                            "/* identical to box height */\n"
                                            "\n"
                                            "\n"
                                            "color: #565656;\n"
                                            "")
        self.frame_net_info_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_net_info_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_net_info_2.setObjectName("frame_net_info_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_net_info_2)
        self.verticalLayout_20.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")

        # self.frame_33 = QtWidgets.QFrame(self.frame_net_info_2)
        # self.frame_33.setMaximumSize(QtCore.QSize(16777215, 30))
        # self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_33.setObjectName("frame_33")

        # self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_33)
        # self.horizontalLayout_31.setContentsMargins(0, 2, 0, 2)
        # self.horizontalLayout_31.setSpacing(0)
        # self.horizontalLayout_31.setObjectName("horizontalLayout_31")

        # self.label_76 = QtWidgets.QLabel(self.frame_33)
        # self.label_76.setObjectName("label_76")
        # self.horizontalLayout_31.addWidget(self.label_76)
        # self.label_77 = QtWidgets.QLabel(self.frame_33)
        # self.label_77.setObjectName("label_77")
        # self.horizontalLayout_31.addWidget(self.label_77)

        # self.horizontalLayout_31.setStretch(0, 1)
        # self.horizontalLayout_31.setStretch(1, 3)
        # self.verticalLayout_20.addWidget(self.frame_33)

        # self.frame_34 = QtWidgets.QFrame(self.frame_net_info_2)
        # self.frame_34.setMaximumSize(QtCore.QSize(16777215, 30))
        # self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_34.setObjectName("frame_34")
        # self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_34)
        # self.horizontalLayout_32.setContentsMargins(0, 2, 0, 2)
        # self.horizontalLayout_32.setSpacing(0)
        # self.horizontalLayout_32.setObjectName("horizontalLayout_32")

        # self.label_78 = QtWidgets.QLabel(self.frame_34)
        # self.label_78.setObjectName("label_78")
        # self.horizontalLayout_32.addWidget(self.label_78)
        # self.label_79 = QtWidgets.QLabel(self.frame_34)
        # self.label_79.setObjectName("label_79")
        # self.horizontalLayout_32.addWidget(self.label_79)
        # self.horizontalLayout_32.setStretch(0, 1)
        # self.horizontalLayout_32.setStretch(1, 3)
        # self.verticalLayout_20.addWidget(self.frame_34)
        # self.frame_35 = QtWidgets.QFrame(self.frame_net_info_2)
        # self.frame_35.setMaximumSize(QtCore.QSize(16777215, 30))
        # self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_35.setObjectName("frame_35")
        # self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_35)
        # self.horizontalLayout_33.setContentsMargins(0, 2, 0, 2)
        # self.horizontalLayout_33.setSpacing(0)
        # self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        # self.label_80 = QtWidgets.QLabel(self.frame_35)
        # self.label_80.setObjectName("label_80")
        # self.horizontalLayout_33.addWidget(self.label_80)
        # self.label_81 = QtWidgets.QLabel(self.frame_35)
        # self.label_81.setObjectName("label_81")
        # self.horizontalLayout_33.addWidget(self.label_81)
        # self.horizontalLayout_33.setStretch(0, 1)
        # self.horizontalLayout_33.setStretch(1, 3)
        # self.verticalLayout_20.addWidget(self.frame_35)

        self.verticalLayout_14.addWidget(self.frame_net_info_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 316, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem2)
        self.verticalLayout_17.addWidget(self.frame_9)
        self.scrollArea_content_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_18.addWidget(self.scrollArea_content_2)
        self.stackedWidget.addWidget(self.page_hard_disk_info)

        # 设置填充信息

        self.label_progress_time_3.setText("02:00")
        self.label_86.setText("100%")
        self.pushButton_pause_3.setText("暂停检查")
        self.pushButton_stop_3.setText("停止检查")
        self.label_39.setText("    项目")
        self.label_40.setText("|")
        self.label_41.setText(" 基本信息")
        self.pushButton_net_info_2.setText("硬盘信息")

       
        # self.label_76.setText( "名称")
        # self.label_77.setText( "Samsung SSD 960 EVO 1TB")
        # self.label_78.setText( "序列号")
        # self.label_79.setText( "0025_3852_81B1_E5F9.")
        # self.label_80.setText( "容量")
        # self.label_81.setText( "931.51 GB")
