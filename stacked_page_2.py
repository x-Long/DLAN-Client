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

import os
import requests
import json
import time
import datetime
# from main import Count_check_file_time
from win32process import SuspendThread


class Runthread_check_file(QtCore.QThread):

    _signal = pyqtSignal(dict,float,str,int)

    def __init__(self, postdatas,parent=None):
        super(Runthread_check_file, self).__init__(parent)
        self.post_info=postdatas


    def get_file_info(self):
        # postdatas = {
        #     "scan_path": ["C://Users//long//Desktop//audit", ],
        #     "file_suffix": [".wps", ".doc", "docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".xlsx"],
        #     "keywords_list": ["秘密", "机密"],
        #     "min_filesize": 1024,
        #     "max_filesize": 1024000000,
        #     "switches": {
        #         "size_switch": True,
        #     }
        # }

        headers = {"Content-Type": "application/json","Accept": "application/json", }
        dis_task = requests.post('http://localhost/v1.0/pc/files/scan',data=json.dumps(self.post_info), headers=headers).content
        dis_task = json.loads(dis_task)

        data = {
            "task_id": dis_task["task_id"],
            "page_size": 1
        }

        while True:
            net_info = requests.get("http://localhost/v1.0/files/scan/status?task_id={}&page_size={}".format(data["task_id"],data["page_size"])).content.decode('unicode-escape')
            # 返回结果中含有 \ ,使得json.loads无法解析，所以需要将返回结果中的 \ 替换为 \\
            net_info = net_info.replace("\\", "\\\\")
            net_info = json.loads(net_info)

            for result in net_info["results"]:
                self._signal.emit(result,net_info["progress"],net_info["status"],data["task_id"])
                print(result,net_info["progress"],111111111111111111111111)
            if net_info["status"] == "finished":
                print('扫描结束')
                break

    def run(self):
        self.get_file_info()
        pass

class Runthread_check_file1(QtCore.QThread):

    _signal = pyqtSignal(dict,float,str,int)

    def __init__(self,task_id,parent=None):
        super(Runthread_check_file1, self).__init__(parent)
        self.task_id=task_id

    def get_file_info(self):

        data = {
            "task_id": self.task_id,
            "page_size": 1
        }

        while True:
            net_info = requests.get("http://localhost/v1.0/files/scan/status?task_id={}&page_size={}".format(data["task_id"],data["page_size"])).content.decode('unicode-escape')
            # 返回结果中含有 \ ,使得json.loads无法解析，所以需要将返回结果中的 \ 替换为 \\
            net_info = net_info.replace("\\", "\\\\")
            net_info = json.loads(net_info)

            for result in net_info["results"]:
                self._signal.emit(result,net_info["progress"],net_info["status"],data["task_id"])
                print(result,net_info["progress"],111111111111111111111111)
            if net_info["status"] == "finished":
                print('扫描结束')
                break

    def run(self):
        self.get_file_info()
        pass


class menu_file_op(QtCore.QThread):

    def __init__(self, src, op, parent=None):
        super(menu_file_op, self).__init__(parent)
        self.src = src
        self.op = op

    def run(self):
        if self.op == "open_filename":
            os.startfile(self.src)
        if self.op == "open_dir":
            os.startfile(self.src)
        if self.op == "del_file":
            os.remove(self.src)


class Stacked_page_2(object):

    def set_up_stacked_page_2(self):

        self.stacked_page_2_ui()
        self.task_id=-1
        self.pushButton_2_0_0.clicked.connect(self.switche_check_file_page)
        self.pushButton_pause_2.clicked.connect(self.pause_check_file)
        self.pushButton_stop_2.clicked.connect(self.stop_check_file)
    
    def stop_check_file(self):
        self.thread.terminate()
        self.count_check_file_time.terminate()
        # self.label_35.setText("0%")
        # self.progressBar_2.setProperty("value", "1")
        # self.label_progress_time_2.setText("0:00")


    def pause_check_file(self):
        if self.pushButton_pause_2.text()=="暂停检查":
            self.pushButton_pause_2.setText("恢复检查")

            postdatas = {
                "task_id": self.task_id,
                "action": "pause"
            }

            headers = {"Content-Type": "application/json","Accept": "application/json", }
            requests.post('http://localhost//v1.0/files/scan/control',data=json.dumps(postdatas), headers=headers)

            self.thread.terminate()
            self.count_check_file_time.terminate()

        elif self.pushButton_pause_2.text()=="恢复检查":
            self.pushButton_pause_2.setText("暂停检查")
            postdatas = {
                "task_id": self.task_id,
                "action": "resume"
            }
            headers = {"Content-Type": "application/json","Accept": "application/json", }
            requests.post('http://localhost//v1.0/files/scan/control',data=json.dumps(postdatas), headers=headers)
            # self.thread.start()
            
            self.count_check_file_time.start()

            self.thread=Runthread_check_file1(self.task_id)
            self.thread._signal.connect(self.add_row)  # 连接信号
            self.thread.start()  # 


    def switche_check_file_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def thread_get_check_file_info(self):

        self.thread = Runthread_check_file(self.postdatas)  # 创建线程
        self.thread._signal.connect(self.add_row)  # 连接信号
        self.thread.start()  # 开始线程

    def page_2_table(self):

        self.init_table_widget()
        self.tableWidget.setHorizontalHeaderLabels(["标记", "序号", "文件名称", "文件大小",  "摘要", "是否加密", "文件路径", "关键字", "关键字位置"])
        # self.thread_get_check_file_info()
        self.table_style()

    def add_row(self, content,progress,status,task_id):
        self.task_id=task_id
        if status=="finished":
            self.count_check_file_time.terminate()
            # Count_check_file_time.time_status=1
        # print(int(self.progressBar_2.value()),int(progress*100-self.progressBar_2.value()),111111111111111111)
        for i in range(int(self.progressBar_2.value()),int(progress*100)+1):
            self.label_35.setText(str(i)+"%")
            self.progressBar_2.setProperty("value", i)
            time.sleep(0.001)

        def hum_convert(value):
            units = ["B", "KB", "MB", "GB", "TB", "PB"]
            size = 1024.0
            for i in range(len(units)):
                if (value / size) < 1:
                    return "%.2f%s" % (value, units[i])
                value = value / size

        def add_item(row, column, item):

            self.tableWidget.setItem(
                row, column, QtWidgets.QTableWidgetItem(str(item)))
            self.tableWidget.item(row, column).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)

        num = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(num+1)

        comBox = QCheckBox()
        hLayout = QtWidgets.QHBoxLayout()
        # 2.在布局里添加checkBox
        hLayout.addWidget(comBox)
        # 3.在布局里居中放置comBox
        hLayout.setAlignment(comBox, Qt.AlignCenter)
        hLayout.setContentsMargins(0, 0, 0, 0)
        hLayout.setSpacing(0)
        # 4.实例化一个QWidget（控件)
        widget = QtWidgets.QWidget()
        # 5.在QWidget放置布局
        widget.setLayout(hLayout)
        # widget.setFixedHeight(50)
        self.tableWidget.setCellWidget(num, 0, widget)

        add_item(num, 1, num+1)   # 序号
        add_item(num, 2, content["filename"])
        add_item(num, 6, content["filepath"])
        add_item(num, 4, content["keyword_details"]["context"])
        add_item(num, 5, content["is_encrypted"])
        add_item(num, 7, content["keyword_details"]["keyword"])
        add_item(num, 8, content["keyword_details"]["offset"])
        # add_item(num, 3, str(content["filesize"]/1024)+"KB")
        add_item(num, 3, hum_convert(content["filesize"]))

    def init_table_widget(self,):

        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.verticalHeader().setVisible(True)

        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        # self.verticalLayout.addWidget(self.tableWidget)
        self.tableWidget.setColumnCount(9)
        self.verticalLayout_13.addWidget(self.tableWidget)
        

        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().resizeSection(0, 40)  # 修改表头第一列的宽度为30
        self.tableWidget.setColumnWidth(0, 40)

        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().resizeSection(1, 40)  # 修改表头第一列的宽度为30
        self.tableWidget.setColumnWidth(1, 40)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().resizeSection(2, 150)  # 修改表头第一列的宽度为30
        # self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().resizeSection(4, 200)  # 修改表头第一列的宽度为30
        # self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.Interactive)
        # self.tableWidget.horizontalHeader().resizeSection(6, 200)  # 修改表头第一列的宽度为30

        self.tableWidget.setContextMenuPolicy(
            Qt.CustomContextMenu)  # 允许右键产生子菜单
        self.tableWidget.customContextMenuRequested.connect(
            self.generateMenu)  # 右键菜单

    def generateMenu(self, pos):
        # rint( pos)
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()

        menu = QMenu()
        item1 = menu.addAction(u"打开文件")
        item2 = menu.addAction(u"打开文件夹")
        item3 = menu.addAction(u"清除文件")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item1:
            print('打开文件', self.tableWidget.item(row_num, 6).text())
            # os.startfile(self.tableWidget.item(row_num, 6).text())
            file_name = self.tableWidget.item(row_num, 6).text()
            print(self.tableWidget.item(row_num, 6).text())
            self.menu_file_op = menu_file_op(file_name, "open_filename")
            self.menu_file_op.start()

        elif action == item2:
            print('打开文件夹', self.tableWidget.item(row_num, 6).text())
            # os.startfile(os.path.dirname(self.tableWidget.item(row_num, 6).text()))
            dir_name = os.path.dirname(self.tableWidget.item(row_num, 6).text())
            print(self.tableWidget.item(row_num, 6).text())
            self.menu_file_op = menu_file_op(dir_name, "open_dir")
            self.menu_file_op.start()

        elif action == item3:
            print('清除文件', self.tableWidget.item(row_num, 6).text())
            # os.remove(self.tableWidget.item(row_num, 6).text())
            del_name = self.tableWidget.item(row_num, 6).text()
            self.menu_file_op = menu_file_op(del_name, "del_file")
            self.menu_file_op.start()
        else:
            return

    def table_style(self):

        self.tableWidget.setStyleSheet("        QTableView\n"
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
        self.tableWidget.verticalScrollBar().setStyleSheet("QScrollBar:vertical{"  # 垂直滑块整体
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

        self.tableWidget.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal{"
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

    def stacked_page_2_ui(self):
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_progress_2 = QtWidgets.QFrame(self.page_2)
        self.frame_progress_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_progress_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progress_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progress_2.setObjectName("frame_progress_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_progress_2)
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 0)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_progress_time_2 = QtWidgets.QLabel(self.frame_progress_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_progress_time_2.sizePolicy().hasHeightForWidth())
        self.label_progress_time_2.setSizePolicy(sizePolicy)
        self.label_progress_time_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_progress_time_2.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        self.label_progress_time_2.setStyleSheet("font-family: Metropolis;\n"
                                                 "font-size: 18px;\n"
                                                 "line-height: 28px;\n"
                                                 "font-weight: 800;\n"
                                                 "\n"
                                                 "color: #565656;")
        self.label_progress_time_2.setObjectName("label_progress_time_2")
        self.horizontalLayout_10.addWidget(self.label_progress_time_2)
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_progress_2)
        self.progressBar_2.setMinimumSize(QtCore.QSize(0, 15))
        self.progressBar_2.setStyleSheet("QProgressBar{\n"
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
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_10.addWidget(self.progressBar_2)
        self.label_35 = QtWidgets.QLabel(self.frame_progress_2)
        self.label_35.setMinimumSize(QtCore.QSize(50, 0))
        self.label_35.setStyleSheet("font-family: Metropolis;\n"
                                    "font-size: 18px;\n"
                                    "line-height: 28px;\n"
                                    "font-weight: 800;\n"
                                    "\n"
                                    "color: #565656;")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_10.addWidget(self.label_35)
        self.pushButton_pause_2 = QtWidgets.QPushButton(self.frame_progress_2)
        self.pushButton_pause_2.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_pause_2.setStyleSheet("background: #3A7FED;\n"
                                              "font-family: PingFang SC;\n"
                                              "font-style: normal;\n"
                                              "font-weight: normal;\n"
                                              "font-size: 14px;\n"
                                              "line-height: 20px;\n"
                                              "border-radius: 3px;\n"
                                              "\n"
                                              "color: #FFFFFF;")
        self.pushButton_pause_2.setObjectName("pushButton_pause_2")
        self.horizontalLayout_10.addWidget(self.pushButton_pause_2)
        self.pushButton_stop_2 = QtWidgets.QPushButton(self.frame_progress_2)
        self.pushButton_stop_2.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_stop_2.setStyleSheet("background: #3A7FED;\n"
                                             "font-family: PingFang SC;\n"
                                             "font-style: normal;\n"
                                             "font-weight: normal;\n"
                                             "font-size: 14px;\n"
                                             "line-height: 20px;\n"
                                             "border-radius: 3px;\n"
                                             "\n"
                                             "color: #FFFFFF;")
        self.pushButton_stop_2.setObjectName("pushButton_stop_2")
        self.horizontalLayout_10.addWidget(self.pushButton_stop_2)
        self.verticalLayout_12.addWidget(self.frame_progress_2)
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setContentsMargins(5, 0, 5, 5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_36 = QtWidgets.QLabel(self.frame_3)
        self.label_36.setStyleSheet("\n"
                                    "font-size: 14px;\n"
                                    "line-height: 28px;\n"
                                    "font-weight: 800;\n"
                                    "\n"
                                    "color: #565656;")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_11.addWidget(self.label_36)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setStyleSheet("QQComboBox QAbstractItemView\n"
                                    "{\n"
                                    "border: 1px solid rgb(161,161,161);\n"
                                    "}\n"
                                    " \n"
                                    "QComboBox QAbstractItemView::item\n"
                                    "{\n"
                                    "height: 24px;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(0, 195, 255);\n"
                                    "}\n"
                                    " \n"
                                    "QComboBox QAbstractItemView::item:selected\n"
                                    "{    \n"
                                    "background-color:rgb(22, 37, 124);\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox)
        self.label_37 = QtWidgets.QLabel(self.frame_3)
        self.label_37.setStyleSheet("font-size: 14px;\n"
                                    "line-height: 28px;\n"
                                    "font-weight: 800;\n"
                                    "\n"
                                    "color: #565656;")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_11.addWidget(self.label_37)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_2)
        self.label_38 = QtWidgets.QLabel(self.frame_3)
        self.label_38.setStyleSheet("font-size: 14px;\n"
                                    "line-height: 28px;\n"
                                    "font-weight: 800;\n"
                                    "\n"
                                    "color: #565656;")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_11.addWidget(self.label_38)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton.setStyleSheet("background: #3A7FED;\n"
                                      "font-family: PingFang SC;\n"
                                      "font-style: normal;\n"
                                      "font-weight: normal;\n"
                                      "font-size: 14px;\n"
                                      "line-height: 20px;\n"
                                      "border-radius: 3px;\n"
                                      "\n"
                                      "color: #FFFFFF;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_12.addWidget(self.frame_3)
        self.tabWidget = QtWidgets.QTabWidget(self.page_2)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
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
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")



        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.page_2_table()



        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_12.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page_2)

        self.label_progress_time_2.setText("0:00")
        self.label_35.setText("0%")
        self.pushButton_pause_2.setText("暂停检查")
        self.pushButton_stop_2.setText("停止检查")
        self.label_36.setText("偏移过滤：")
        self.comboBox.setItemText(0, "不限偏移")
        self.comboBox.setItemText(1, "精准")
        self.comboBox.setItemText(2, "标题")
        self.comboBox.setItemText(3, "概要")
        self.label_37.setText(" 文件类型：")
        self.comboBox_2.setItemText(0, "全部类型")
        self.comboBox_2.setItemText(1, "文档")
        self.comboBox_2.setItemText(2, "压缩包")
        self.label_38.setText(" 是否加密：")
        self.comboBox_3.setItemText(0, "不限")
        self.comboBox_3.setItemText(1, "加密文件")
        self.comboBox_3.setItemText(2, "所有文件")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),  "关键词命中文件")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),  "疑似标密文件")
        self.pushButton.setText("常规文件检查配置")
