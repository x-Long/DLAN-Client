#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX

from dlanan_page_2 import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys

class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

      
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

