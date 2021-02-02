from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Table(QWidget):
  def __init__(self):
    super(Table, self).__init__()
    self.initUI()
  def initUI(self):
    self.setWindowTitle("QTableWidget例子")
    self.resize(400,300)

    layout=QHBoxLayout()
 
    #实现的效果是一样的，四行三列，所以要灵活运用函数，这里只是示范一下如何单独设置行列
    TableWidget=QTableWidget(4,3)
 
    # TableWidget = QTableWidget()
    # TableWidget.setRowCount(4)
    # TableWidget.setColumnCount(3)
 
 
 
    #设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
    TableWidget.setHorizontalHeaderLabels(['序号','文件名称','  | 命中关键字'])
    #Todo 优化1 设置垂直方向的表头标签
    #TableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])
 
    #TODO 优化 2 设置水平方向表格为自适应的伸缩模式
    # TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
 
    #TODO 优化3 将表格变为禁止编辑
    #TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
 
    #TODO 优化 4 设置表格整行选中
    #TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
 
    #TODO 优化 5 将行与列的高度设置为所显示的内容的宽度高度匹配
    #QTableWidget.resizeColumnsToContents(TableWidget)
    #QTableWidget.resizeRowsToContents(TableWidget)
 
    #TODO 优化 6 表格头的显示与隐藏
    TableWidget.verticalHeader().setVisible(False)
    #TableWidget.horizontalHeader().setVisible(False)
 
    #TOdo 优化7 在单元格内放置控件
    # comBox=QCheckBox()
    # comBox1=QCheckBox()
    # comBox2=QCheckBox()
    # comBox1.setStyleSheet('Color:red;Background-color:rgb(0,0,0);')

  
    # TableWidget.setCellWidget(0,1,comBox)
    # TableWidget.setCellWidget(1,1,comBox1)
    # TableWidget.setCellWidget(2,1,comBox2)
    
    # searchBtn=QPushButton('修改')
   
    # TableWidget.setCellWidget(0,2,searchBtn)
 
 
    #添加数据
    newItem=QTableWidgetItem('张三张三')
    TableWidget.setItem(0,0,newItem)


    newItem=QTableWidgetItem('a')
    TableWidget.setItem(1,0,newItem)
 
    newItem=QTableWidgetItem('男          ')
    TableWidget.setItem(0,1,newItem)
 
    newItem=QTableWidgetItem('160')
    TableWidget.setItem(0,2,newItem)
 
    layout.addWidget(TableWidget)
    # TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    # TableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
    TableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{font:bold 14px;")
            
    TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    TableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
    TableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    # TableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
    TableWidget.setShowGrid(False)
    TableWidget.setStyleSheet(
                           "QTableWidget::item{border-bottom:1px solid #014F84}")
    TableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignLeft | Qt.AlignBottom); 
 

    self.setLayout(layout)
if __name__ == '__main__':
  app=QApplication(sys.argv)
  win=Table()
  win.show()
  sys.exit(app.exec_())