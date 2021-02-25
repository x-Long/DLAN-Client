from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QObject, pyqtSignal
from requests_manager import RequestManager

import os
import requests
import json
import time
import datetime


class Runthread_cell_phone_records_info(QtCore.QThread):

    # 看情况需要替换
    _signal = pyqtSignal(list)

    def __init__(self,parent=None):
        super(Runthread_cell_phone_records_info, self).__init__(parent)

    def run(self):
        # 需要替换
        net_info=RequestManager.make_get_request('/v1.0/native/get_cell_phone_records')
        self._signal.emit(net_info); # 信号发送


class Stacked_page_cell_phone_records_4(object):

    def set_up_stacked_page_cell_phone_records_4(self):

        self.stacked_page_cell_phone_records_4_ui()
        # 需要替换
        self.pushButton_3_0_0.clicked.connect(self.switche_cell_phone_records_page)
        self.thread_get_cell_phone_records_info()

    def switche_cell_phone_records_page(self):
        # 需要替换
        self.stackedWidget.setCurrentIndex(10)

    def thread_get_cell_phone_records_info(self):

        self.thread_cell_phone_records_info = Runthread_cell_phone_records_info() # 创建线程
        self.thread_cell_phone_records_info._signal.connect(self.add_cell_phone_records_row) # 连接信号
        self.thread_cell_phone_records_info.start() # 开始线程

    def page_cell_phone_records_4(self):

        self.init_cell_phone_records_table_widget()
        # 需要替换
        self.tableWidget_9.setHorizontalHeaderLabels(["序号","设备名", "厂商", "容量", "上次插入时间"])
        self.usb_cell_phone_records_style()

    def add_cell_phone_records_row(self,content):
        def add_item(row, column, item):
            self.tableWidget_9.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
            self.tableWidget_9.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        for item in content:
            num = self.tableWidget_9.rowCount()
            self.tableWidget_9.setRowCount(num+1)

            # 需要替换
            add_item(num, 0, num+1)   # 序号
            add_item(num, 1, item["device_name"])
            add_item(num, 2, item["manufacture"])
            add_item(num, 3, item["storage"])
            add_item(num, 4, item["last_plugin_time"])
   

    def init_cell_phone_records_table_widget(self):

        self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_10)

        # self.tableWidget_9.setSortingEnabled(True)
        self.tableWidget_9.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_9.setShowGrid(False)
        self.tableWidget_9.setWordWrap(True)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.verticalHeader().setVisible(False)

        self.tableWidget_9.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_9.verticalHeader().setStretchLastSection(False)
        # self.verticalLayout.addWidget(self.tableWidget_9)

        # 需要替换，列数
        self.tableWidget_9.setColumnCount(5)

        # self.tableWidget_9.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_9.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_9.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_9.setSelectionBehavior(QAbstractItemView.SelectRows)
        # # self.tableWidget_9.setSelectionMode(QAbstractItemView.SingleSelection)

        # # self.tableWidget_9.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tableWidget_9.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        # self.tableWidget_9.horizontalHeader().resizeSection(0, 40)  # 修改表头第一列的宽度为30
        self.tableWidget_9.setColumnWidth(0, 40)

        # self.tableWidget_9.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        # # self.tableWidget_9.horizontalHeader().resizeSection(1, 40)  # 修改表头第一列的宽度为30
        # self.tableWidget_9.setColumnWidth(1, 40)

        # self.tableWidget_9.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        # self.tableWidget_9.horizontalHeader().resizeSection(2, 150)  # 修改表头第一列的宽度为30
        # self.tableWidget_9.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        # self.tableWidget_9.horizontalHeader().resizeSection(4, 200)  # 修改表头第一列的宽度为30
        # self.tableWidget_9.horizontalHeader().setSectionResizeMode(6, QHeaderView.Interactive)
        # self.tableWidget_9.horizontalHeader().resizeSection(6, 200)  # 修改表头第一列的宽度为30

 

    def stacked_page_cell_phone_records_4_ui(self):
        self.page_get_cell_phone_records = QtWidgets.QWidget()
        self.page_get_cell_phone_records.setObjectName("page_get_cell_phone_records")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.page_get_cell_phone_records)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        # self.frame_progress_11 = QtWidgets.QFrame(self.page_get_cell_phone_records)
        # self.frame_progress_11.setMinimumSize(QtCore.QSize(0, 0))
        # self.frame_progress_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_progress_11.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_progress_11.setObjectName("frame_progress_11")
        # self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_progress_11)
        # self.horizontalLayout_21.setContentsMargins(5, 5, 5, 5)
        # self.horizontalLayout_21.setSpacing(5)
        # self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        # self.label_progress_time_11 = QtWidgets.QLabel(self.frame_progress_11)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_progress_time_11.sizePolicy().hasHeightForWidth())
        # self.label_progress_time_11.setSizePolicy(sizePolicy)
        # self.label_progress_time_11.setMinimumSize(QtCore.QSize(60, 0))
        # self.label_progress_time_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        # self.label_progress_time_11.setStyleSheet("font-family: Metropolis;\n"
        #                                           "font-size: 18px;\n"
        #                                           "line-height: 28px;\n"
        #                                           "font-weight: 800;\n"
        #                                           "\n"
        #                                           "color: #565656;")
        # self.label_progress_time_11.setObjectName("label_progress_time_11")
        # self.horizontalLayout_21.addWidget(self.label_progress_time_11)
        # self.progressBar_11 = QtWidgets.QProgressBar(self.frame_progress_11)
        # self.progressBar_11.setMinimumSize(QtCore.QSize(0, 15))
        # self.progressBar_11.setStyleSheet("QProgressBar{\n"
        #                                   "\n"
        #                                   "background-color: #DEDEDE; \n"
        #                                   "height:12px;\n"
        #                                   "border-radius: 8px;\n"
        #                                   "\n"
        #                                   "\n"
        #                                   "\n"
        #                                   "}\n"
        #                                   "\n"
        #                                   "\n"
        #                                   "QProgressBar::chunk{\n"
        #                                   "background-color: #83C088; \n"
        #                                   "border-radius: 6px;\n"
        #                                   "\n"
        #                                   "}\n"
        #                                   "\n"
        #                                   " ")
        # self.progressBar_11.setProperty("value", 24)
        # self.progressBar_11.setTextVisible(False)
        # self.progressBar_11.setObjectName("progressBar_11")
        # self.horizontalLayout_21.addWidget(self.progressBar_11)
        # self.label_49 = QtWidgets.QLabel(self.frame_progress_11)
        # self.label_49.setMinimumSize(QtCore.QSize(50, 0))
        # self.label_49.setStyleSheet("font-family: Metropolis;\n"
        #                             "font-size: 18px;\n"
        #                             "line-height: 28px;\n"
        #                             "font-weight: 800;\n"
        #                             "\n"
        #                             "color: #565656;")
        # self.label_49.setObjectName("label_49")
        # self.horizontalLayout_21.addWidget(self.label_49)
        # self.pushButton_pause_11 = QtWidgets.QPushButton(self.frame_progress_11)
        # self.pushButton_pause_11.setMinimumSize(QtCore.QSize(100, 35))
        # self.pushButton_pause_11.setStyleSheet("background: #3A7FED;\n"
        #                                        "font-family: PingFang SC;\n"
        #                                        "font-style: normal;\n"
        #                                        "font-weight: normal;\n"
        #                                        "font-size: 14px;\n"
        #                                        "line-height: 20px;\n"
        #                                        "border-radius: 3px;\n"
        #                                        "\n"
        #                                        "color: #FFFFFF;")
        # self.pushButton_pause_11.setObjectName("pushButton_pause_11")
        # self.horizontalLayout_21.addWidget(self.pushButton_pause_11)
        # self.pushButton_stop_11 = QtWidgets.QPushButton(self.frame_progress_11)
        # self.pushButton_stop_11.setMinimumSize(QtCore.QSize(100, 35))
        # self.pushButton_stop_11.setStyleSheet("background: #3A7FED;\n"
        #                                       "font-family: PingFang SC;\n"
        #                                       "font-style: normal;\n"
        #                                       "font-weight: normal;\n"
        #                                       "font-size: 14px;\n"
        #                                       "line-height: 20px;\n"
        #                                       "border-radius: 3px;\n"
        #                                       "\n"
        #                                       "color: #FFFFFF;")
        # self.pushButton_stop_11.setObjectName("pushButton_stop_11")
        # self.horizontalLayout_21.addWidget(self.pushButton_stop_11)
        # self.verticalLayout_35.addWidget(self.frame_progress_11)
        self.tabWidget_9 = QtWidgets.QTabWidget(self.page_get_cell_phone_records)
        self.tabWidget_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_9.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
                                       "    top: -0.01em;\n"
                                       "}\n"
                                       " \n"
                                       "QTabWidget::tab-bar {\n"
                                       "    alignment: left;\n"
                                       "    left: 2em;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QTabBar::tab {\n"
                                       "    border-top-left-radius: 10px;border-top-right-radius: 10px;\n"
                                       "    background-color: #4094da;\n"
                                       "    font: bold 12px \'Arial\';\n"
                                       "    color: white;\n"
                                       "    height:40px;\n"
                                       "    width:200px;\n"
                                       "    font-style: normal;\n"
                                       "    font-weight: 600;\n"
                                       "    font-size: 16px;\n"
                                       "    line-height: 22px;\n"
                                       "}\n"
                                       "QTabBar::tab:selected {\n"
                                       "    color: white;\n"
                                       "    background: #213E75;\n"
                                       " }\n"
                                       "\n"
                                       "QTabBar::tab:!selected {\n"
                                       "    background-color: white;\n"
                                       "    color: #565656;;\n"
                                       "}\n"
                                       "")
        self.tabWidget_9.setObjectName("tabWidget_9")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setStyleSheet("")
        self.tab_10.setObjectName("tab_10")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.tab_10)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.tab_10)
        self.page_cell_phone_records_4()
        self.verticalLayout_34.addWidget(self.tableWidget_9)
        self.tabWidget_9.addTab(self.tab_10, "")
        self.verticalLayout_35.addWidget(self.tabWidget_9)
        self.stackedWidget.addWidget(self.page_get_cell_phone_records)

        # self.label_progress_time_11.setText("02:00")
        # self.label_49.setText("100%")
        # self.pushButton_pause_11.setText("暂停检查")
        # self.pushButton_stop_11.setText("停止检查")
        # 替换变量名后，替换tabWidget_8
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_10),  "手机拔插记录")


    # 框架内表格的ui,只需要替换表格的对象名
    def usb_cell_phone_records_style(self):

        self.tableWidget_9.setStyleSheet("        QTableView\n"
                                       "{\n"
                                       "    background-color: #FFFFFF;\n"
                                       "    alternate-background-color:#e3edf9;\n"
                                       "    font:14px \"微软雅黑\";\n"
                                       "    color:#677483;\n"
                                       "    gridline-color: #ccddf0;  \n"
                                       "\n"
                                       "border: 2px solid rgba(41, 43, 49, 0.2);\n"
                                       "border-top: 5px solid #213E75;\n"
                                       "border-bottom: 3px solid rgba(41, 43, 49, 0.2);\n"
                                       "\n"
                                       "border-radius:5px\n"
                                       "\n"
                                       "}\n"
                                       " \n"
                                       "QTableView::item\n"
                                       "{  \n"
                                       "    font:20px \"微软雅黑\";\n"
                                       "    color:#29414E; \n"
                                       "    border:0px;   \n"
                                       "    border-bottom: 1px solid rgba(0, 0, 0, 0.05);\n"
                                       "}\n"
                                       " \n"
                                       "QTableView::item:selected\n"
                                       "{  \n"
                                       #    "    color:#256CDD;\n"
                                       "background:#cde8ff;"
                                       "}\n"
                                       " \n"
                                       "QHeaderView::section { \n"
                                       "    color: #565656;;\n"
                                       "    font:bold 14px \"微软雅黑\";\n"
                                       "    text-align:right;\n"
                                       "    height:43px;\n"
                                    #    "    width:23px;"
                                       "    \n"
                                       "    border:0px;\n"
                                       "\n"
                                       "    border-bottom: 2px solid rgba(0, 0, 0, 0.1);\n"
                                       "    border-right: 1px solid rgba(0, 0, 0, 0.1);\n"
                                       "\n"
                                       "    background: #FFFFFF;\n"
                                       "\n"
                                       "    border-left:none;\n"
                                       "    padding:0px;\n"
                                       "}\n"
                                       " \n"
                                       "// border-left:none;防止中间表头的border重叠\n"
                                       "QHeaderView::section:first\n"
                                       "{\n"
                                       "    border-left:1px solid #8faac9;\n"
                                       "border-radius: 3px;\n"
                                       "}")

        # 滚动条样式
        self.tableWidget_9.verticalScrollBar().setStyleSheet("QScrollBar:vertical{"  # 垂直滑块整体
                                                           "background:#FFFFFF;"  # 背景色
                                                           "padding-top:10px;"  # 上预留位置（放置向上箭头）
                                                           "padding-bottom:10px;"  # 下预留位置（放置向下箭头）
                                                           "padding-left:3px;"  # 左预留位置（美观）
                                                           "padding-right:3px;"  # 右预留位置（美观）
                                                           "border-left:1px solid #d7d7d7;}"  # 左分割线
                                                           # 滑块样式
                                                           "QScrollBar::handle:vertical{"
                                                           "background:#dbdbdb;"  # 滑块颜色
                                                           "border-radius:6px;"  # 边角圆润
                                                           "min-height:80px;}"  # 滑块最小高度
                                                           # 鼠标触及滑块样式
                                                           "QScrollBar::handle:vertical:hover{"
                                                           "background:#d0d0d0;}"  # 滑块颜色
                                                           # 向下箭头样式
                                                           "QScrollBar::add-line:vertical{"
                                                           "background:url(:/images/resource/images/checkout/down.png) center no-repeat;}"
                                                           # 向上箭头样式
                                                           "QScrollBar::sub-line:vertical{"
                                                           "background:url(:/images/resource/images/checkout/up.png) center no-repeat;}")

        self.tableWidget_9.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal{"
                                                             "background:#FFFFFF;"
                                                             "padding-top:3px;"
                                                             "padding-bottom:3px;"
                                                             "padding-left:10px;"
                                                             "padding-right:10px;}"
                                                             "QScrollBar::handle:horizontal{"
                                                             "background:#dbdbdb;"
                                                             "border-radius:6px;"
                                                             "min-width:30px;}"
                                                             "QScrollBar::handle:horizontal:hover{"
                                                             "background:#d0d0d0;}"
                                                             "QScrollBar::add-line:horizontal{"
                                                             "background:url(:/images/resource/images/checkout/right.png) center no-repeat;}"
                                                             "QScrollBar::sub-line:horizontal{"
                                                             "background:url(:/images/resource/images/checkout/left.png) center no-repeat;}")
