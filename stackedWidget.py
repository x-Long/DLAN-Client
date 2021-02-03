from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json
# from dlan import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys
from stacked_page_1 import Stacked_page_1
from stacked_page_2 import Stacked_page_2

class Stacked_widget(Stacked_page_1,Stacked_page_2):

    def set_up_stacked_widget(self):

        self.stacked_widget_ui()
        self.set_up_stacked_page_1()
        self.set_up_stacked_page_2()

    def stacked_widget_ui(self):

        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)       
