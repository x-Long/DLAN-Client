
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
import pickle
import os
from requests_manager import RequestManager
import requests
import u_key
from requests_manager import RequestManager

class Count_check_file_time(QtCore.QThread):
    _signal = pyqtSignal(str,int)

    def __init__(self,last_check_file_all_time, parent=None):
        super(Count_check_file_time, self).__init__(parent)
        self.last_check_file_all_time=last_check_file_all_time

    def run(self):
        start = datetime.datetime.now()
        while (True):
            time.sleep(1)
            end = datetime.datetime.now()
            count_time=(end-start).seconds+self.last_check_file_all_time
            text = "%d:%02d" % (count_time/60, count_time % 60)
            self._signal.emit(text,count_time)


class Network_check_is_connect(QtCore.QThread):
    _signal = pyqtSignal(bool)

    def __init__(self,parent=None):
        super(Network_check_is_connect, self).__init__(parent)

    def run(self):
        while True:
<<<<<<< HEAD

            result=True
            try:
                requests.get(RequestManager.get_base_url())
                # print("网络正常")
            except:
                result=False
                print("网络故障")
            self._signal.emit(result)
=======
            if RequestManager.is_server_ready():
                self._signal.emit(True)
                break
>>>>>>> 02cf2b6f507a736da70976fbce3ee746a341c015
            time.sleep(1)

class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.check_network()
        self.setupUi(self)
        self.init_dialog()
        self.pushButton.clicked.connect(self.di.show)

    def init_dialog(self):
        # self.last_check_file_all_time=0
        self.di = QtWidgets.QDialog()

        self.d = dialog.Ui_Dialog()
        self.d.setupUi(self.di)

        self.di.setWindowIcon(QtGui.QIcon('icon/logo.png'))
        self.di.setWindowTitle("常规文件检查配置")
 
        # self.di.show()
        self.read_dialog_config(self.d)
        self.d.add_com_src.clicked.connect(lambda: self.file_path(self.d))

        self.d.com_config.clicked.connect(self.di.reject)
        # self.d.com_config.clicked.connect(lambda: self.count_time())
        self.d.com_config.clicked.connect(lambda: self.complete_config(self.d))
        self.pushButton.clicked.connect(lambda: self.complete_config(self.d))
        
        self.d.default_config.clicked.connect(lambda: self.read_dialog_config(self.d))
        
        self.d.clean_com_src.clicked.connect(lambda: self.clean_dialog_table(self.d))
        for all_type in ["self.d.all_micsoft_type","self.d.all_wps_type","self.d.all_compress_type"]:
            eval(all_type).stateChanged.connect(lambda: self.all_type_state_change(self.d))

    def check_network(self):

        self.check_is_connect=Network_check_is_connect()
        self.check_is_connect._signal.connect(self.is_network_connect)
        self.check_is_connect.start()

    def is_network_connect(self,is_connect):
        if not is_connect:
            self.check_is_connect.terminate()
            msg_box=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '警告', "未检测到本地server，程序即将退出。\n\n请启动server后重新进入。")
            msg_box.exec_()
            self.close()
      
    def read_dialog_config(self,d):
        # {'dialog_check_box_list': {'d.all_micsoft_type': True, 'd.checkBox_xls': True, 'd.checkBox_ppt': True, 'd.checkBox_doc': True, 'd.all_wps_type': True, 'd.checkBox_9wps': True, 'd.checkBox_et': True, 'd.checkBox_dps': True, 'd.all_compress_type': True, 'd.checkBox_zip': True, 'd.checkBox_is_encrypt': True},
        #  'dialog_line_input': {'d.lineEdit_2': '', 'd.min_file_size_str': '0', 'd.max_file_size_str': '10240000'}, 
        # 'dialog_combobox': {'d.min_file_size_comboBox': 0, 'd.max_file_size_comboBox': 0}, 
        # 'dialog_choose_table_src': []}

        if os.path.exists('.\\check_file_dialog_config.pickle'):
            with open('.\\check_file_dialog_config.pickle', 'rb') as f :
                para= pickle.load(f) 
                for k,v in para["dialog_check_box_list"].items():
                    eval(k).setChecked(v)
                for k,v in para["dialog_line_input"].items():
                    eval(k).setText(v)
                for k,v in para["dialog_combobox"].items():
                    eval(k).setCurrentIndex(v)

                d.tableWidget.setRowCount(0)
                d.tableWidget.clearContents()           
                for i in para['dialog_choose_table_src']:
                    self.add_dialog_table_src(i,d)

    def clean_dialog_table(self,d):
        d.tableWidget.setRowCount(0)
        d.tableWidget.clearContents()

    def all_type_state_change(self,d):
        file_type = {
            "d.all_micsoft_type": ["d.checkBox_xls", "d.checkBox_ppt","d.checkBox_doc"],
            "d.all_wps_type": ["d.checkBox_9wps","d.checkBox_et", "d.checkBox_dps"],
            "d.all_compress_type": ["d.checkBox_zip"],
        }

        for k,v in file_type.items():
            for i in v:
                if eval(k).isChecked():
                    eval(i).setChecked(True)
                else:
                    eval(i).setChecked(False)

    def count_time(self):
        
        self.count_check_file_time=Count_check_file_time(self.last_check_file_all_time)
        self.count_check_file_time._signal.connect(self.show_time)
        self.count_check_file_time.start()

    def show_time(self,text,count_time):
        self.last_check_file_all_time=count_time
        self.label_progress_time_2.setText(text)

    def file_path(self,d):
        
        file_path1=QFileDialog.getExistingDirectory(self, "请选择检查路径", "C://")
        self.add_dialog_table_src(file_path1,d)   
        self.di.showMinimized()
        self.di.showNormal()    

    def add_dialog_table_src(self, item, d):

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

        if d.lineEdit_2.text()!="" and d.all_expansion_type.isChecked():
            for suf in d.lineEdit_2.text().split(" "):
                suffix.append("."+suf)
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
        # if len(scan_path)==0:
        #     scan_path.append("C://Users//long//Desktop//audit")
        return scan_path



    def complete_config(self,d):

        # {'d.all_micsoft_type': True, 'd.checkBox_xls': True, 'd.checkBox_ppt': True, 'd.checkBox_doc': True,
        #  'd.all_wps_type': True, 'd.checkBox_9wps': True, 'd.checkBox_et': True, 'd.checkBox_dps': True, 'd.all_compress_type': True,
        #     'd.checkBox_zip': True, 'd.checkBox_is_encrypt': True, 'd.lineEdit_2': '',
        #     'd.min_file_size_str': '0', 'd.max_file_size_str': '10240000', 'd.min_file_size_comboBox': 0, 'd.max_file_size_comboBox': 0, 'dialog_choose_table_src': []}


        dialog_check_box_status={
            "dialog_check_box_list":{},
            "dialog_line_input":{},
            "dialog_combobox":{},
            "dialog_choose_table_src":[],
        }

        dialog_check_box_list=["d.all_micsoft_type","d.checkBox_xls", "d.checkBox_ppt","d.checkBox_doc","d.all_wps_type","d.checkBox_9wps","d.checkBox_et", "d.checkBox_dps","d.all_compress_type","d.checkBox_zip","d.checkBox_is_encrypt"]
        dialog_line_input=["d.lineEdit_2","d.min_file_size_str","d.max_file_size_str","d.key_word_input"]
        dialog_combobox=["d.min_file_size_comboBox","d.max_file_size_comboBox"]

        for check_box in dialog_check_box_list:
            dialog_check_box_status["dialog_check_box_list"][check_box]=eval(check_box).isChecked()

        for line_input in dialog_line_input:
            dialog_check_box_status["dialog_line_input"][line_input]=eval(line_input).text()

        for combobox in dialog_combobox:
            dialog_check_box_status["dialog_combobox"][combobox]=eval(combobox).currentIndex()

        num = d.tableWidget.rowCount()
        for i in range(num):
            dialog_check_box_status["dialog_choose_table_src"].append(d.tableWidget.item(i,1).text())

        with open('.\\check_file_dialog_config.pickle', 'wb') as f :
            pickle.dump(dialog_check_box_status, f)
            
        with open('.\\check_file_dialog_config.pickle', 'rb') as f :
            dialog_check_box_status= pickle.load(f) 

def handle_u_key_verify(u_key_ui,u_key_dialog):

    u_key_ui.pushButton_verify.setText("正在验证...")
    QtWidgets.QApplication.processEvents()
    # res=True
    res=RequestManager.make_get_request("/v1.0/ukey/verify?code={}".format(u_key_ui.lineEdit_password.text()))

    print(res)
    if res :
        u_key_dialog.accept()
    else:
        msg_box=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '警告', '口令不正确，请重新输入。')
        msg_box.exec_()
        u_key_ui.pushButton_verify.setText("验证")
        QtWidgets.QApplication.processEvents()

def start_dlan_gui(server_port:int):
    RequestManager.on_port_ready(server_port)
    app = QtWidgets.QApplication(sys.argv)
    u_key_dialog = QtWidgets.QDialog()
    u_key_ui = u_key.Ui_Dialog()
    u_key_ui.setupUi(u_key_dialog)
    u_key_dialog.setWindowIcon(QtGui.QIcon('icon/logo.png'))
    u_key_dialog.setWindowTitle("帝岚科技计算机终端保密检查系统")
    u_key_ui.pushButton_verify.clicked.connect(lambda: handle_u_key_verify(u_key_ui,u_key_dialog))
    from PyQt5.QtGui import QIntValidator
    u_key_ui.lineEdit_password.setValidator(QIntValidator(0, 999999))
    u_key_dialog.show()

    if u_key_dialog.exec_() == QtWidgets.QDialog.Accepted:

        # app = QtWidgets.QApplication(sys.argv)
        main_window = Main_window()
        main_window.setWindowIcon(QtGui.QIcon('icon/logo.png'))
        main_window.setWindowTitle("帝岚科技计算机终端保密检查系统")
        print(main_window.width())
        # main_window.resize(main_window.width(),main_window.width()*0.6)
        main_window.show()
        app.exec()


if __name__ == '__main__':
    start_dlan_gui(50008)
