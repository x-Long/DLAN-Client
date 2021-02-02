# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DLAN-2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import requests
import json

from sideBar import Side_bar
from statusBar import Status_bar
from stackedWidget import Stacked_widget


class Ui_Form(Side_bar,Status_bar,Stacked_widget):

    def setupUi(self, Form):

        self.setupForm(Form)
        self.set_up_side_bar()
        self.set_up_status_bar()
        self.set_up_stacked_widget()

    def setupForm(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 800)
        Form.setMinimumHeight(800)
        # Form.setMinimumWidth(1200)
        Form.setStyleSheet("QPushButton{\n"
                           "border:0px;\n"
                           "color: #FFFFFF;\n"
                           "}")

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_main = QtWidgets.QFrame(Form)
        self.frame_main.setStyleSheet("")
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setLineWidth(0)
        self.frame_main.setObjectName("frame_main")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
