# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'u_key.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(557, 359)
        Dialog.setStyleSheet("#Dialog{border-image: url('.//icon//u_key_cover.png');}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 296, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(60, 0, 60, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font-family:\"微软雅黑\";\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"font-style: normal;\n"
"color: #256CDD;\n"
"\n"
"\n"
"\n"
"")
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_password.setStyleSheet("    border: 1px solid rgba(86, 86, 86, 0.7);\n"
"    border-radius: 3px;\n"
"    padding: 5 8px;\n"
"    background: white;\n"
"    font-family:20px  \"微软雅黑\";")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout.addWidget(self.lineEdit_password)
        self.pushButton_verify = QtWidgets.QPushButton(self.frame)
        self.pushButton_verify.setMinimumSize(QtCore.QSize(100, 35))
        self.pushButton_verify.setStyleSheet(
                                                "QPushButton{"
                                                "background: #3A7FED;\n"
                                              "font-family: PingFang SC;\n"
                                              "font-style: normal;\n"
                                              "font-weight: normal;\n"
                                              "font-size: 14px;\n"
                                              "line-height: 20px;\n"
                                              "border-radius: 3px;\n"
                                              "\n"
                                              "color: #FFFFFF;"
                                              "}"
                                                "QPushButton:hover{"
                                                "background: #007acc;\n"
                                              "font-family: PingFang SC;\n"
                                              "font-style: normal;\n"
                                              "font-weight: normal;\n"
                                              "font-size: 14px;\n"
                                              "line-height: 20px;\n"
                                              "border-radius: 3px;\n"
                                              "\n"
                                              "color: #FFFFFF;"
                                              "}"
                                              )

        self.pushButton_verify.setObjectName("pushButton_verify")
        self.horizontalLayout.addWidget(self.pushButton_verify)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "动态口令:"))
        self.pushButton_verify.setText(_translate("Dialog", "验证"))

