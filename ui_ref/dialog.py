# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(810, 619)
        Dialog.setStyleSheet("background:#FFFFFF;")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setStyleSheet("border: 1px solid rgba(86, 86, 86, 0.05);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.frame_9 = QtWidgets.QFrame(Dialog)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 11, 11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_9)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setStyleSheet("color:#F54F47;\n"
                                   "font-weight: 500;\n"
                                   "font-size: 16px;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#565656;\n"
                                   "font-family: \"微软雅黑\";\n"
                                   "\n"
                                   "font-weight: 600;\n"
                                   "font-size: 18px;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setContentsMargins(5, 11, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setStyleSheet("font-family: \"微软雅黑\";\n"
                                   "color: #565656;\n"
                                   "\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.key_word_input = QtWidgets.QLineEdit(self.frame_10)
        self.key_word_input.setStyleSheet("font-family: \"微软雅黑\";\n"
                                          "color: #565656;\n"
                                          "font-weight: 400;\n"
                                          "font-size: 14px;\n"
                                          "border: 1px solid rgba(86, 86, 86, 0.7);\n"
                                          "border-radius: 3px;")
        self.key_word_input.setObjectName("key_word_input")
        self.horizontalLayout_5.addWidget(self.key_word_input)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setStyleSheet("border: 1px solid rgba(86, 86, 86, 0.05);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setStyleSheet("color:#F54F47;\n"
                                   "font-weight: 500;\n"
                                   "font-size: 16px;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)

        self.all_doc_type = QtWidgets.QCheckBox(self.frame_6)
        self.all_doc_type.setStyleSheet("color:#565656;\n"
                                        "font-family: \"微软雅黑\";\n"
                                        "\n"
                                        "font-weight: 600;\n"
                                        "font-size: 18px;\n"
                                        "")
        self.all_doc_type.setChecked(True)
        self.all_doc_type.setObjectName("all_doc_type")

        self.horizontalLayout_3.addWidget(self.all_doc_type)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("font-family: \"微软雅黑\";\n"
                                   "color: #565656;\n"
                                   "\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout.setContentsMargins(-1, 5, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_doc = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_doc.setChecked(True)
        self.checkBox_doc.setObjectName("checkBox_doc")
        self.gridLayout.addWidget(self.checkBox_doc, 0, 0, 1, 1)
        self.checkBox_xls = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_xls.setChecked(True)
        self.checkBox_xls.setObjectName("checkBox_xls")
        self.gridLayout.addWidget(self.checkBox_xls, 0, 1, 1, 1)
        self.checkBox_ppt = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_ppt.setChecked(True)
        self.checkBox_ppt.setObjectName("checkBox_ppt")
        self.gridLayout.addWidget(self.checkBox_ppt, 0, 2, 1, 1)
        self.checkBox_9wps = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_9wps.setChecked(True)
        self.checkBox_9wps.setObjectName("checkBox_9wps")
        self.gridLayout.addWidget(self.checkBox_9wps, 1, 0, 1, 1)
        self.checkBox_et = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_et.setChecked(True)
        self.checkBox_et.setObjectName("checkBox_et")
        self.gridLayout.addWidget(self.checkBox_et, 1, 1, 1, 1)
        self.checkBox_dps = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_dps.setChecked(True)
        self.checkBox_dps.setObjectName("checkBox_dps")
        self.gridLayout.addWidget(self.checkBox_dps, 1, 2, 1, 1)
        self.checkBox_zip = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_zip.setChecked(True)
        self.checkBox_zip.setObjectName("checkBox_zip")
        self.gridLayout.addWidget(self.checkBox_zip, 2, 0, 1, 1)
        self.checkBox_is_encrypt = QtWidgets.QCheckBox(self.frame_7)
        self.checkBox_is_encrypt.setStyleSheet("font-family: \"微软雅黑\";\n"
                                               "color: #565656;\n"
                                               "\n"
                                               "font-weight: 600;\n"
                                               "font-size: 16px;")
        self.checkBox_is_encrypt.setChecked(True)
        self.checkBox_is_encrypt.setObjectName("checkBox_is_encrypt")
        self.gridLayout.addWidget(self.checkBox_is_encrypt, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setStyleSheet("border: 1px solid rgba(86, 86, 86, 0.05);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.frame_11 = QtWidgets.QFrame(Dialog)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_12)
        self.label_5.setStyleSheet("color:#F54F47;\n"
                                   "font-weight: 500;\n"
                                   "font-size: 16px;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#565656;\n"
                                   "font-family: \"微软雅黑\";\n"
                                   "\n"
                                   "font-weight: 600;\n"
                                   "font-size: 18px;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setStyleSheet("font-family: \"微软雅黑\";\n"
                                    "color: #565656;\n"
                                    "\n"
                                    "font-weight: 400;\n"
                                    "font-size: 14px;")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.min_file_size_str = QtWidgets.QLineEdit(self.frame_13)
        self.min_file_size_str.setStyleSheet("font-family: \"微软雅黑\";\n"
                                             "color: #565656;\n"
                                             "font-weight: 400;\n"
                                             "font-size: 14px;\n"
                                             "border: 1px solid rgba(86, 86, 86, 0.7);\n"
                                             "border-radius: 3px;")
        self.min_file_size_str.setObjectName("min_file_size_str")
        self.horizontalLayout_7.addWidget(self.min_file_size_str)
        self.min_file_size_comboBox = QtWidgets.QComboBox(self.frame_13)
        self.min_file_size_comboBox.setObjectName("min_file_size_comboBox")
        self.min_file_size_comboBox.addItem("")
        self.min_file_size_comboBox.addItem("")
        self.min_file_size_comboBox.addItem("")
        self.min_file_size_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.min_file_size_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(
            167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.frame_13)
        self.label_11.setStyleSheet("font-family: \"微软雅黑\";\n"
                                    "color: #565656;\n"
                                    "\n"
                                    "font-weight: 400;\n"
                                    "font-size: 14px;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.max_file_size_str = QtWidgets.QLineEdit(self.frame_13)
        self.max_file_size_str.setStyleSheet("font-family: \"微软雅黑\";\n"
                                             "color: #565656;\n"
                                             "font-weight: 400;\n"
                                             "font-size: 14px;\n"
                                             "border: 1px solid rgba(86, 86, 86, 0.7);\n"
                                             "border-radius: 3px;")
        self.max_file_size_str.setObjectName("max_file_size_str")
        self.horizontalLayout_7.addWidget(self.max_file_size_str)
        self.max_file_size_comboBox = QtWidgets.QComboBox(self.frame_13)
        self.max_file_size_comboBox.setObjectName("max_file_size_comboBox")
        self.max_file_size_comboBox.addItem("")
        self.max_file_size_comboBox.addItem("")
        self.max_file_size_comboBox.addItem("")
        self.max_file_size_comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.max_file_size_comboBox)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setStyleSheet("border: 1px solid rgba(86, 86, 86, 0.05);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("font: \"微软雅黑\"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("color:#F54F47;\n"
                                   "font-weight: 500;\n"
                                   "font-size: 16px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#565656;\n"
                                   "font-family: \"微软雅黑\";\n"
                                   "\n"
                                   "font-weight: 600;\n"
                                   "font-size: 18px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.add_com_src = QtWidgets.QPushButton(self.frame_2)
        self.add_com_src.setMinimumSize(QtCore.QSize(100, 30))
        self.add_com_src.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_com_src.setStyleSheet("background: #3A7FED;\n"
                                       "font-family: \"微软雅黑\";;\n"
                                       "font-style: normal;\n"
                                       "font-weight: normal;\n"
                                       "font-size: 14px;\n"
                                       "line-height: 20px;\n"
                                       "border-radius: 3px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.add_com_src.setObjectName("add_com_src")

        self.horizontalLayout.addWidget(self.add_com_src)

        # self.add_com_src.clicked.connect(lambda: self.file_path())

        self.clean_com_src = QtWidgets.QLabel(self.frame_2)
        self.clean_com_src.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clean_com_src.setStyleSheet("font-family: \"微软雅黑\";\n"
                                         "font-style: normal;\n"
                                         "font-weight: normal;\n"
                                         "font-size: 14px;\n"
                                         "line-height: 20px;\n"
                                         "\n"
                                         "color: rgba(86, 86, 86, 0.4);")
        self.clean_com_src.setObjectName("clean_com_src")
        self.horizontalLayout.addWidget(self.clean_com_src)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 160))
        self.frame_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout.setObjectName("verticalLayout")

        self.config_table()

        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_6.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.com_config = QtWidgets.QPushButton(self.frame_3)
        self.com_config.setMinimumSize(QtCore.QSize(150, 35))
        self.com_config.setStyleSheet("background: #3A7FED;\n"
                                      "font-family: \"微软雅黑\";;\n"
                                      "font-style: normal;\n"
                                      "font-weight: normal;\n"
                                      "font-size: 14px;\n"
                                      "line-height: 20px;\n"
                                      "border-radius: 3px;\n"
                                      "\n"
                                      "color: #FFFFFF;")
        self.com_config.setObjectName("com_config")
        self.horizontalLayout_2.addWidget(self.com_config)
        self.default_config = QtWidgets.QPushButton(self.frame_3)
        self.default_config.setMinimumSize(QtCore.QSize(150, 35))
        self.default_config.setStyleSheet("background: #3A7FED;\n"
                                          "font-family: \"微软雅黑\";;\n"
                                          "font-style: normal;\n"
                                          "font-weight: normal;\n"
                                          "font-size: 14px;\n"
                                          "line-height: 20px;\n"
                                          "border-radius: 3px;\n"
                                          "\n"
                                          "color: #FFFFFF;")
        self.default_config.setObjectName("default_config")
        self.horizontalLayout_2.addWidget(self.default_config)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_6.addWidget(self.frame_3)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 208, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.frame.raise_()
        self.frame_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.frame_9.raise_()
        self.line_3.raise_()
        self.frame_3.raise_()
        self.frame_11.raise_()
        self.line_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def config_table(self):

        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 200))

        self.tableWidget.setStatusTip("")
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
                                       "\n"
                                       "}\n"
                                       " \n"
                                       "QTableView::item:selected\n"
                                       "{  \n"
                                       "    color:green;\n"
                                       "}\n"
                                       " \n"
                                       "QHeaderView::section { \n"
                                       "    color: #565656;;\n"
                                       "    font:bold 14px \"微软雅黑\";\n"
                                       "    text-align:right;\n"
                                       "    height:43px;\n"
                                       "    \n"
                                       "    border:0px;\n"
                                       "\n"
                                       "    border-bottom: 2px solid rgba(0, 0, 0, 0.1);\n"
                                       "\n"
                                       "    background: #FFFFFF;\n"
                                       "\n"
                                       "    border-left:none;\n"
                                       "border-left: 1px solid rgba(41, 43, 49, 0.2);\n"
                                       "border-right:1px solid rgba(41, 43, 49, 0.2);\n"
                                       "}\n"
                                       " \n"
                                       "// border-left:none;防止中间表头的border重叠\n"
                                       "QHeaderView::section:first\n"
                                       "{\n"
                                       "    border-left:1px solid #8faac9;\n"
                                       "border-radius: 3px;\n"
                                       "}")
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(3)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")

        # self.add_src()

        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.setRowCount(2)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 1, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

#     def add_src(self, item, Dialog):

#         def add_item(row, column, item):

#             self.tableWidget.setItem(
#                 row, column, QtWidgets.QTableWidgetItem(str(item)))
#             self.tableWidget.item(row, column).setTextAlignment(
#                 Qt.AlignHCenter | Qt.AlignVCenter)

#         num = self.tableWidget.rowCount()
#         self.tableWidget.setRowCount(num+1)

#         add_item(num, 0, num+1)   # 序号
#         add_item(num, 1, item)   # 序号

#     def file_path(self):

#         file_path = QFileDialog.getExistingDirectory(
#             self, "请选择文件夹路径", "E://demo//")
#         self.add_src(file_path)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "*"))
        self.label_6.setText(_translate("Dialog", "  关键词配置"))
        self.label_2.setText(_translate("Dialog", "自定义关键词： "))
        self.key_word_input.setText(_translate("Dialog", "机密 秘密 绝密"))
        self.label_8.setText(_translate("Dialog", "* "))
        self.all_doc_type.setText(_translate("Dialog", " 文档类型选择"))
        self.checkBox_doc.setText(_translate("Dialog", "微软文字文档 (doc;docx)"))
        self.checkBox_xls.setText(_translate("Dialog", "微软图表文档 (xls;xlsx)"))
        self.checkBox_ppt.setText(_translate(
            "Dialog", "微软演示文档 (ppt;pptx;ppx）"))
        self.checkBox_9wps.setText(_translate("Dialog", "金山文字文档 (9wps)"))
        self.checkBox_et.setText(_translate("Dialog", "金山图表文档 (et)"))
        self.checkBox_dps.setText(_translate("Dialog", "金山演示文档 (dps)"))
        self.checkBox_zip.setText(_translate("Dialog", "压缩文件 (zip;rar)"))
        self.checkBox_is_encrypt.setText(_translate("Dialog", "在选中类型中检查是否加密"))
        self.label_5.setText(_translate("Dialog", "*"))
        self.label_9.setText(_translate("Dialog", "  文件大小"))
        self.label_10.setText(_translate("Dialog", "最小："))
        self.min_file_size_str.setText(_translate("Dialog", "0"))
        self.min_file_size_comboBox.setItemText(0, _translate("Dialog", "B"))
        self.min_file_size_comboBox.setItemText(1, _translate("Dialog", "KB"))
        self.min_file_size_comboBox.setItemText(2, _translate("Dialog", "MB"))
        self.min_file_size_comboBox.setItemText(3, _translate("Dialog", "GB"))
        self.label_11.setText(_translate("Dialog", "最大："))
        self.max_file_size_str.setText(_translate("Dialog", "10240000"))
        self.max_file_size_comboBox.setItemText(0, _translate("Dialog", "B"))
        self.max_file_size_comboBox.setItemText(1, _translate("Dialog", "KB"))
        self.max_file_size_comboBox.setItemText(2, _translate("Dialog", "MB"))
        self.max_file_size_comboBox.setItemText(3, _translate("Dialog", "GB"))
        self.label_4.setText(_translate("Dialog", "*"))
        self.label_3.setText(_translate("Dialog", "  电脑路径选择"))
        self.add_com_src.setText(_translate("Dialog", "浏览并添加"))
        self.clean_com_src.setText(_translate("Dialog", "  清空"))

        # self.tableWidget.setSortingEnabled(True)
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("Dialog", "New Row"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("Dialog", "New Row"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("Dialog", "序号"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("Dialog", "路径检查"))
        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)
        # self.tableWidget.setSortingEnabled(__sortingEnabled)


        self.com_config.setText(_translate("Dialog", "完成配置"))
        self.default_config.setText(_translate("Dialog", "使用默认配置"))
