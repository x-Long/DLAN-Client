from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys
from stacked_page_1 import Stacked_page_1
from stacked_page_2 import Stacked_page_2
from stacked_page_usb_storge_3 import Stacked_page_usb_storge_3
from stacked_page_hard_disk_4 import Stacked_page_hard_disk_4
from stacked_page_all_usb import Stacked_page_all_usb_4
from stacked_page_installed_software import Stacked_page_installed_software_4  
from stacked_page_anti_virus import Stacked_page_anti_virus_4
from stacked_page_file_access_records import Stacked_page_file_access_records_4
from stacked_page_power_off_records import Stacked_page_power_off_records_4

class Stacked_widget(Stacked_page_1,Stacked_page_2,Stacked_page_usb_storge_3,Stacked_page_hard_disk_4,Stacked_page_all_usb_4,Stacked_page_installed_software_4,Stacked_page_anti_virus_4,Stacked_page_file_access_records_4,Stacked_page_power_off_records_4):

    def set_up_stacked_widget(self):

        self.stacked_widget_ui()
        self.set_up_stacked_page_1()
        self.set_up_stacked_page_2()
        self.set_up_stacked_page_usb_storge_3()
        self.set_up_stacked_page_hard_disk_4()
        self.set_up_stacked_page_all_usb_4()
        self.set_up_stacked_page_installed_software_4()
        self.set_up_stacked_page_anti_virus_4()
        self.set_up_stacked_page_file_access_records_4()
        self.set_up_stacked_page_power_off_records_4()

    def stacked_widget_ui(self):

        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)       
