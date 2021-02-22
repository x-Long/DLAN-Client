# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(881, 628)
        Dialog.setStyleSheet("background: white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    top:0em;\n"
"  background: white;\n"
"border-top: 2px solid rgba(0, 0, 0, 0.05);\n"
"}\n"
" \n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"    left: 0em;\n"
"    \n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"border:0px;\n"
"\n"
"\n"
"    font: bold 16px \'微软雅黑\';\n"
"    color: white;\n"
"    height:40px;\n"
"    width:100px;\n"
"\n"
"\n"
"\n"
"}\n"
"QTabBar::tab:selected {\n"
"    color: #256CDD;\n"
"\n"
"border-bottom: 2px solid #256CDD;\n"
" }\n"
"\n"
"QTabBar::tab:!selected {\n"
"\n"
"    color: #565656;;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(20, -1, 20, 30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_21 = QtWidgets.QFrame(self.frame)
        self.frame_21.setStyleSheet("QFrame#frame_21{\n"
"border: 0px;\n"
"border-bottom: 2px solid rgba(86, 86, 86, 0.05);;\n"
"}")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.all_doc_type_8 = QtWidgets.QCheckBox(self.frame_22)
        self.all_doc_type_8.setStyleSheet("color:#565656;\n"
"font-family: \"微软雅黑\";\n"
"\n"
"font-weight: 600;\n"
"font-size: 18px;\n"
"")
        self.all_doc_type_8.setChecked(True)
        self.all_doc_type_8.setObjectName("all_doc_type_8")
        self.horizontalLayout_10.addWidget(self.all_doc_type_8)
        self.horizontalLayout_10.setStretch(0, 1)
        self.verticalLayout_7.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setStyleSheet("font-family: \"微软雅黑\";\n"
"color: #565656;\n"
"\n"
"font-weight: 400;\n"
"font-size: 16px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_23)
        self.gridLayout_5.setContentsMargins(-1, 5, -1, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_doc = QtWidgets.QCheckBox(self.frame_23)
        self.checkBox_doc.setChecked(True)
        self.checkBox_doc.setObjectName("checkBox_doc")
        self.gridLayout_5.addWidget(self.checkBox_doc, 0, 0, 1, 1)
        self.checkBox_ppt = QtWidgets.QCheckBox(self.frame_23)
        self.checkBox_ppt.setChecked(True)
        self.checkBox_ppt.setObjectName("checkBox_ppt")
        self.gridLayout_5.addWidget(self.checkBox_ppt, 0, 2, 1, 1)
        self.checkBox_xls = QtWidgets.QCheckBox(self.frame_23)
        self.checkBox_xls.setChecked(True)
        self.checkBox_xls.setObjectName("checkBox_xls")
        self.gridLayout_5.addWidget(self.checkBox_xls, 0, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_23)
        self.verticalLayout_2.addWidget(self.frame_21)
        self.frame_18 = QtWidgets.QFrame(self.frame)
        self.frame_18.setStyleSheet("QFrame#frame_18{\n"
"border: 0px;\n"
"border-bottom: 2px solid rgba(86, 86, 86, 0.05);;\n"
"}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.all_doc_type_7 = QtWidgets.QCheckBox(self.frame_19)
        self.all_doc_type_7.setStyleSheet("color:#565656;\n"
"font-family: \"微软雅黑\";\n"
"\n"
"font-weight: 600;\n"
"font-size: 18px;\n"
"")
        self.all_doc_type_7.setChecked(True)
        self.all_doc_type_7.setObjectName("all_doc_type_7")
        self.horizontalLayout_9.addWidget(self.all_doc_type_7)
        self.horizontalLayout_9.setStretch(0, 1)
        self.verticalLayout_6.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setStyleSheet("font-family: \"微软雅黑\";\n"
"color: #565656;\n"
"\n"
"font-weight: 400;\n"
"font-size: 16px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_4.setContentsMargins(-1, 5, -1, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_et = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_et.setChecked(True)
        self.checkBox_et.setObjectName("checkBox_et")
        self.gridLayout_4.addWidget(self.checkBox_et, 0, 1, 1, 1)
        self.checkBox_dps = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_dps.setChecked(True)
        self.checkBox_dps.setObjectName("checkBox_dps")
        self.gridLayout_4.addWidget(self.checkBox_dps, 0, 2, 1, 1)
        self.checkBox_9wps = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_9wps.setChecked(True)
        self.checkBox_9wps.setObjectName("checkBox_9wps")
        self.gridLayout_4.addWidget(self.checkBox_9wps, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_20)
        self.verticalLayout_2.addWidget(self.frame_18)
        self.frame_25 = QtWidgets.QFrame(self.frame)
        self.frame_25.setStyleSheet("QFrame#frame_25{\n"
"\n"
"border: 0px;\n"
"border-bottom: 2px solid rgba(86, 86, 86, 0.05);;\n"
"}\n"
"\n"
"")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.all_doc_type_10 = QtWidgets.QCheckBox(self.frame_26)
        self.all_doc_type_10.setStyleSheet("color:#565656;\n"
"font-family: \"微软雅黑\";\n"
"\n"
"font-weight: 600;\n"
"font-size: 18px;\n"
"")
        self.all_doc_type_10.setChecked(True)
        self.all_doc_type_10.setObjectName("all_doc_type_10")
        self.horizontalLayout_12.addWidget(self.all_doc_type_10)
        self.verticalLayout_8.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.frame_25)
        self.frame_27.setStyleSheet("font-family: \"微软雅黑\";\n"
"color: #565656;\n"
"\n"
"font-weight: 400;\n"
"font-size: 16px;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_6.setContentsMargins(-1, 5, -1, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox_zip = QtWidgets.QCheckBox(self.frame_27)
        self.checkBox_zip.setChecked(True)
        self.checkBox_zip.setObjectName("checkBox_zip")
        self.gridLayout_6.addWidget(self.checkBox_zip, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_27)
        self.verticalLayout_2.addWidget(self.frame_25)
        self.frame_28 = QtWidgets.QFrame(self.frame)
        self.frame_28.setStyleSheet("QFrame#frame_28{\n"
"border: 0px;\n"
"border-bottom: 2px solid rgba(86, 86, 86, 0.05);;\n"
"}")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(11)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.all_doc_type_11 = QtWidgets.QCheckBox(self.frame_29)
        self.all_doc_type_11.setStyleSheet("color:#565656;\n"
"font-family: \"微软雅黑\";\n"
"\n"
"font-weight: 600;\n"
"font-size: 18px;\n"
"")
        self.all_doc_type_11.setChecked(True)
        self.all_doc_type_11.setObjectName("all_doc_type_11")
        self.horizontalLayout_13.addWidget(self.all_doc_type_11)
        self.verticalLayout_9.addWidget(self.frame_29)
        self.frame_30 = QtWidgets.QFrame(self.frame_28)
        self.frame_30.setStyleSheet("font-family: \"微软雅黑\";\n"
"color: #565656;\n"
"\n"
"font-weight: 400;\n"
"font-size: 16px;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_2.setContentsMargins(0, 0, 11, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_30)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    /* 外边框 */\n"
"    border: 1px solid rgba(86, 86, 86, 0.7);\n"
"    border-radius: 3px;\n"
"    padding: 5 8px;\n"
"    background: white;\n"
"\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_9.addWidget(self.frame_30)
        self.verticalLayout_2.addWidget(self.frame_28)
        self.frame_24 = QtWidgets.QFrame(self.frame)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setContentsMargins(11, 5, 0, 5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_is_encrypt = QtWidgets.QCheckBox(self.frame_24)
        self.checkBox_is_encrypt.setStyleSheet("color:#565656;\n"
"font-family: \"微软雅黑\";\n"
"\n"
"font-weight: 600;\n"
"font-size: 18px;\n"
"")
        self.checkBox_is_encrypt.setChecked(True)
        self.checkBox_is_encrypt.setObjectName("checkBox_is_encrypt")
        self.horizontalLayout_11.addWidget(self.checkBox_is_encrypt)
        self.verticalLayout_2.addWidget(self.frame_24)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setContentsMargins(20, -1, 20, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setStyleSheet("\n"
"QFrame#frame{\n"
"border: 0px;\n"
"border-bottom: 2px solid rgba(86, 86, 86, 0.05);;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(0, 0, 11, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setStyleSheet("color:#F54F47;\n"
"font-weight: 500;\n"
"font-size: 16px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#565656;\n"
"font-family: \"微软雅黑\";\n"
"\n"
"font-weight: 600;\n"
"font-size: 18px;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_com_src = QtWidgets.QPushButton(self.frame_5)
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
        self.clean_com_src = QtWidgets.QLabel(self.frame_5)
        self.clean_com_src.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clean_com_src.setStyleSheet("font-family: \"微软雅黑\";\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 20px;\n"
"\n"
"color: rgba(86, 86, 86, 0.4);")
        self.clean_com_src.setObjectName("clean_com_src")
        self.horizontalLayout.addWidget(self.clean_com_src)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setStyleSheet("QFrame#frame_11{\n"
"border: 0px;\n"
"border-bottom: 2px solid rgba(86, 86, 86, 0.05);;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setContentsMargins(11, 0, 11, 20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_11.addWidget(self.frame_12)
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
        spacerItem2 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        self.verticalLayout_11.addWidget(self.frame_13)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.verticalLayout_12.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_14.setContentsMargins(20, -1, 20, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_8 = QtWidgets.QFrame(self.tab_3)
        self.frame_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(11)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setStyleSheet("font-family: \"微软雅黑\";\n"
"font-size: 18px;\n"
"line-height: 20px;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.key_word_input = QtWidgets.QLineEdit(self.frame_9)
        self.key_word_input.setStyleSheet("QLineEdit {\n"
"    /* 外边框 */\n"
"    border: 1px solid rgba(86, 86, 86, 0.7);\n"
"    border-radius: 3px;\n"
"    padding: 5 8px;\n"
"    background: white;\n"
"    font-family:16px  \"微软雅黑\";\n"
"\n"
"}")
        self.key_word_input.setPlaceholderText("")
        self.key_word_input.setObjectName("key_word_input")
        self.horizontalLayout_5.addWidget(self.key_word_input)
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_2.setMinimumSize(QtCore.QSize(130, 30))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background:  white;\n"
"font-family: \"微软雅黑\";;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 20px;\n"
"border-radius: 5px;\n"
"color: #256CDD;\n"
"border: 2px solid #256CDD;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("color: #256CDD;")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.verticalLayout_13.addWidget(self.frame_9)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_8)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 150))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_2.setStatusTip("")
        self.tableWidget_2.setStyleSheet("        QTableView\n"
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
        self.tableWidget_2.setLineWidth(0)
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setAutoScrollMargin(3)
        self.tableWidget_2.setDragEnabled(True)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_13.addWidget(self.tableWidget_2)
        self.verticalLayout_14.addWidget(self.frame_8)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
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
        self.horizontalLayout_3.addWidget(self.com_config)
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
        self.horizontalLayout_3.addWidget(self.default_config)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.all_doc_type_8.setText(_translate("Dialog", "微软office文档"))
        self.checkBox_doc.setText(_translate("Dialog", "微软文字文档 (doc;docx)"))
        self.checkBox_ppt.setText(_translate("Dialog", "微软演示文档 (ppt;pptx;ppx）"))
        self.checkBox_xls.setText(_translate("Dialog", "微软图表文档 (xls;xlsx)"))
        self.all_doc_type_7.setText(_translate("Dialog", "金山wps文档"))
        self.checkBox_et.setText(_translate("Dialog", "金山图表文档 (et)"))
        self.checkBox_dps.setText(_translate("Dialog", "金山演示文档 (dps)"))
        self.checkBox_9wps.setText(_translate("Dialog", "金山文字文档 (9wps)"))
        self.all_doc_type_10.setText(_translate("Dialog", "压缩文件"))
        self.checkBox_zip.setText(_translate("Dialog", "压缩文件 (在压缩文件zip/rar中查找以上格式)"))
        self.all_doc_type_11.setText(_translate("Dialog", "拓展文件类型"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "例如：ini txt; 文件类型以空格分隔"))
        self.checkBox_is_encrypt.setText(_translate("Dialog", "在选中类型中选择是否加密"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "文件类型"))
        self.label_4.setText(_translate("Dialog", "*"))
        self.label_3.setText(_translate("Dialog", "  电脑路径选择"))
        self.add_com_src.setText(_translate("Dialog", "浏览并添加"))
        self.clean_com_src.setText(_translate("Dialog", "  清空"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "路径检查"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "检查范围"))
        self.label_6.setText(_translate("Dialog", "自定义关键词："))
        self.key_word_input.setText(_translate("Dialog", "绝密 机密 秘密"))
        self.label_7.setText(_translate("Dialog", "..."))
        self.pushButton_2.setText(_translate("Dialog", "加载关键词库"))
        self.label.setText(_translate("Dialog", "  下载关键词库"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "标记"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "行业"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "公文字号关键词组"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "秘密级关键词组"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "机密级关键词组"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "绝密级关键词组"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "关键词配置"))
        self.com_config.setText(_translate("Dialog", "完成配置"))
        self.default_config.setText(_translate("Dialog", "使用默认配置"))

