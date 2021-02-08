#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX

from Form import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from functools import partial
import sys
import dialog
import datetime
import time

class Count_check_file_time(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Count_check_file_time, self).__init__(parent)

    def run(self):
        start = datetime.datetime.now()
        while (True):
            time.sleep(1)
            end = datetime.datetime.now()
            text = "%d:%02d" % ((end-start).seconds/60, (end-start).seconds % 60)
            print(text)
            self._signal.emit(text)
            

class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_dialog)

    def show_dialog(self):
        self.di = QtWidgets.QDialog()

        d = dialog.Ui_Dialog()
        d.setupUi(self.di)

        # self.di.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.di.setWindowIcon(QtGui.QIcon('icon/logo.png'))
        self.di.setWindowTitle("常规文件检查配置")
        # self.di.setWindowFlags(Qt.FramelessWindowHint)
        # self.di.setWindowFlags(Qt.WindowContextHelpButtonHint)
 
        self.di.show()
        d.add_com_src.clicked.connect(lambda: self.file_path(d))
        d.com_config.clicked.connect(lambda: self.get_info_info(d))
        d.com_config.clicked.connect(lambda: self.count_time())

    def count_time(self):
        
        self.count_check_file_time=Count_check_file_time()
        self.count_check_file_time._signal.connect(self.show_time)
        self.count_check_file_time.start()


    def show_time(self,text):
        self.label_progress_time_2.setText(text)

    def file_path(self,d):
        
        file_path1=QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "E://demo//")
        self.add_src1(file_path1,d)       

    def add_src1(self, item, d):

        def add_item(row, column, item, d):

            d.tableWidget.setItem(
                row, column, QtWidgets.QTableWidgetItem(str(item)))
            d.tableWidget.item(row, column).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)

        num = d.tableWidget.rowCount()
        d.tableWidget.setRowCount(num+1)

        add_item(num, 0, num+1, d)   # 序号
        add_item(num, 1, item, d)   # 序号

    def get_config_key_word(self, d):
        keywords_str = d.key_word_input.text()
        keywords_list = keywords_str.split(" ")
        return keywords_list

    def get_config_file_suffix(self, d):
        file_type = {
            "d.checkBox_doc":[".doc", ".docx"],
            "d.checkBox_xls":[".xls", ".xlsx"],
            "d.checkBox_ppt":[".ppt", ".pptx", ".ppx"],
            "d.checkBox_9wps":[".9wps"],
            "d.checkBox_et":[".et"],
            "d.checkBox_dps":[".dps"],
            "d.checkBox_zip":[".zip", ".rar"],
        }
        suffix=[]

        for k,v in file_type.items():
            if eval(k).isChecked():
                suffix.extend(v)
        return suffix

    def get_config_filesize(self,d):

        # units = ["B","KB", "MB", "GB", "TB", "PB"]
        min_filesize=int(d.min_file_size_str.text())*(1024**(d.min_file_size_comboBox.currentIndex()))
        max_filesize=int(d.max_file_size_str.text())*(1024**(d.max_file_size_comboBox.currentIndex()))
        return min_filesize,max_filesize

    def get_config_switches(self,d):

        return d.checkBox_is_encrypt.isChecked()

    def get_scan_path_in_table(self,d):
        num = d.tableWidget.rowCount()
        scan_path=[]
        for i in range(d.tableWidget.rowCount()):
            src=d.tableWidget.item(i, 1).text()
            # src=src.replace("\\", "\\\\")
            scan_path.append(src)
        return scan_path

    def get_info_info(self,d):
        self.label_35.setText("0%")
        self.progressBar_2.setProperty("value", "1")
        self.label_progress_time_2.setText("0:00")
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents()
        
        # for num in range(self.tableWidget.rowCount()):
        #     self.tableWidget.removeRow(num)

        print(self.get_config_file_suffix(d))
        print(self.get_config_key_word(d))
        print(self.get_config_filesize(d))
        print(self.get_config_switches(d))
        print(self.get_scan_path_in_table(d))

        self.postdatas = {
            "scan_path": self.get_scan_path_in_table(d),
            "file_suffix": self.get_config_file_suffix(d),
            "keywords_list": self.get_config_key_word(d),
            "min_filesize": self.get_config_filesize(d)[0],
            "max_filesize": self.get_config_filesize(d)[1],
            "switches": {
                "size_switch": self.get_config_switches(d),
            }

        }
        self.thread_get_check_file_info()

        self.di.reject()




# 运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.setWindowIcon(QtGui.QIcon('icon/logo.png'))
    main_window.setWindowTitle("帝岚科技计算机终端保密检查系统")
    print(main_window.width())
    # main_window.resize(main_window.width(),main_window.width()*0.6)
    main_window.show()
    app.exec()
