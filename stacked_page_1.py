from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys
import time
import requests_manager 
from requests_manager import RequestManager


class Runthread(QtCore.QThread):

    _signal = pyqtSignal(list,dict)

    def __init__(self,parent=None):
        super(Runthread, self).__init__(parent)

    # def run(self):
    #     net_info=json.loads(requests.get("http://localhost/v1.0/pc/network").content)
    #     com_info=json.loads(requests.get("http://localhost/v1.0/pc/info").content)
    #     self._signal.emit(net_info,com_info); # 信号发送

    def run(self):
        net_info=RequestManager.make_get_request('/v1.0/pc/network')
        com_info=RequestManager.make_get_request('/v1.0/pc/info')
        self._signal.emit(net_info,com_info); # 信号发送



class Stacked_page_1(object):

    def set_up_stacked_page_1(self):

        self.stacked_page_1_ui()

        # 界面开始打开线程加载主机信息
        self.thread_get_com_net_info()

        # 点击主机信息按钮后打开线程加载主机信息，加载完记得在thread_get_com_net_info解除绑定，避免重复加载
        # self.pushButton_0_0_0.clicked.connect(self.thread_get_com_net_info)

        self.pushButton_0_0_0.clicked.connect(self.switche_com_net_info_page)

    def switche_com_net_info_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def thread_get_com_net_info(self):

        self.thread = Runthread() # 创建线程
        self.thread._signal.connect(self.stacked_page_1_func) # 连接信号
        # self.pushButton_0_0_0.clicked.disconnect(self.thread_get_com_net_info)
        self.thread.start() # 开始线程

    def stacked_page_1_func(self,net_info,com_info):

        self.create_com_info(com_info)
        self.create_net_info(net_info)

    def info_frame_res(self,frame):

        if frame.isVisible():
            frame.setVisible(False)
        else:
            frame.setVisible(True)

    def create_net_info(self, net_info):

        for info in net_info:
            self.computer_net_info_frame("self.verticalLayout_19","名称", info.get("name"))
            self.computer_net_info_frame("self.verticalLayout_19","MAC地址", info.get("mac"))
            self.computer_net_info_frame("self.verticalLayout_19","IP地址", info.get("ip"))

    def create_com_info(self,com_info):
       
        self.computer_net_info_frame("self.verticalLayout_11","电脑类型", com_info.get("pc_type"))
        self.computer_net_info_frame("self.verticalLayout_11","电脑用户名", com_info.get("pc_name"))
        self.computer_net_info_frame("self.verticalLayout_11","主板型号", com_info.get("mother_board_model"))
        if len(com_info.get("cd_drive"))!=0:
            for item in com_info.get("cd_drive"):
                self.computer_net_info_frame("self.verticalLayout_11","光驱信息", item.get("model")+" "+item.get("size")+" mount_dir:"+item.get("mount_dir"))
        else:
            self.computer_net_info_frame("self.verticalLayout_11","光驱信息", "-")
        self.computer_net_info_frame("self.verticalLayout_11","内存信息", com_info.get("ram_info"))
        self.computer_net_info_frame("self.verticalLayout_11","处理器信息", com_info.get("processor_info"))

    def computer_net_info_frame(self, layout, item_name, v):

        frame_4 = QtWidgets.QFrame(self.frame_computer_info)
        frame_4.setMaximumSize(QtCore.QSize(16777215, 30))
        frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_4.setObjectName("frame_4")

        horizontalLayout_4 = QtWidgets.QHBoxLayout(frame_4)
        horizontalLayout_4.setContentsMargins(0, 2, 0, 2)
        horizontalLayout_4.setSpacing(0)
        horizontalLayout_4.setObjectName("horizontalLayout_4")

        label_12 = QtWidgets.QLabel(frame_4)
        label_12.setObjectName("label_12")
        horizontalLayout_4.addWidget(label_12)
        label_12.setText(item_name)
        label_12.setTextInteractionFlags(Qt.TextSelectableByMouse)

        label_10 = QtWidgets.QLabel(frame_4)
        label_10.setObjectName("label_10")
        horizontalLayout_4.addWidget(label_10)
        label_10.setText(v)
        label_10.setTextInteractionFlags(Qt.TextSelectableByMouse)


        label_25 = QtWidgets.QLabel(frame_4)
        label_25.setObjectName("label_25")
        horizontalLayout_4.addWidget(label_25)
        label_25.setText("违规信息的提示")
        label_25.setTextInteractionFlags(Qt.TextSelectableByMouse)

        label_26 = QtWidgets.QLabel(frame_4)
        label_26.setStyleSheet("font-family: Microsoft YaHei;\n"
                               "font-style: normal;\n"
                               "font-weight: 800;\n"
                               "font-size: 14px;\n"
                               "line-height: 20px;\n"
                               "/* identical to box height */\n"
                               "\n"
                               "\n"
                               "color: #256CDD;\n"
                               "")
        label_26.setObjectName("label_26")
        horizontalLayout_4.addWidget(label_26)
        label_26.setText("违规提示")
        # label_26.setTextInteractionFlags(Qt.TextSelectableByMouse)

        horizontalLayout_4.setStretch(0, 1)
        horizontalLayout_4.setStretch(1, 3)
        horizontalLayout_4.setStretch(2, 3)
        horizontalLayout_4.setStretch(3, 1)

        eval(layout).addWidget(frame_4)

    def progress_bar_ui(self):
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

        self.label_progress_time.setText("02:00")
        self.label_21.setText("100%")
        self.pushButton_pause.setText("暂停检查")
        self.pushButton_stop.setText("停止检查")
        
    def stacked_page_1_ui(self):
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("QWidget#page{\n"
                                "background: #E5E5E5;\n"
                                "\n"
                                "\n"
                                "}")
        self.page.setObjectName("page")

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        # self.progress_bar_ui()

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
            QtCore.QRect(0, 0, 960, 696))
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
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setStyleSheet("color:rgba(86, 86, 86, 0.2);\n"
                                    "font-size: 20px;\n"
                                    "")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_3.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setStyleSheet("color:rgba(86, 86, 86, 0.2);\n"
                                    "font-size: 20px;\n"
                                    "")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_3.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_3.addWidget(self.label_24)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(4, 3)
        self.horizontalLayout_3.setStretch(6, 1)
        self.verticalLayout_10.addWidget(self.frame_2)

        self.pushButton_computer_info = QtWidgets.QToolButton(self.frame)
        self.pushButton_computer_info.setToolButtonStyle(
            Qt.ToolButtonTextBesideIcon)
        self.pushButton_computer_info.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.pushButton_computer_info.setIcon(QtGui.QIcon("./icon/info.png"))
        self.pushButton_computer_info.clicked.connect(lambda: self.info_frame_res(self.frame_computer_info))

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
        self.verticalLayout_11.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.verticalLayout_10.addWidget(self.frame_computer_info)

        self.pushButton_net_info = QtWidgets.QToolButton(self.frame)
        self.pushButton_net_info.setToolButtonStyle(
            Qt.ToolButtonTextBesideIcon)
        self.pushButton_net_info.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
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
        self.pushButton_net_info.clicked.connect(lambda: self.info_frame_res(self.frame_net_info))

        
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
        self.verticalLayout_19.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")


        self.verticalLayout_10.addWidget(self.frame_net_info)

        spacerItem1 = QtWidgets.QSpacerItem(
            20, 316, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.verticalLayout_16.addWidget(self.frame)
        self.scrollArea_content.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_content)
        self.stackedWidget.addWidget(self.page)

        # 设置填充信息


        self.label_7.setText("       项目")
        self.label_8.setText("|")
        self.label_9.setText("  基本信息")
        self.label_11.setText("|")
        self.label_22.setText(" 描述/违规提示")
        self.label_23.setText("|")
        self.label_24.setText(" 违规参考")
        self.pushButton_computer_info.setText("计算机信息")
        self.pushButton_net_info.setText("网络信息")