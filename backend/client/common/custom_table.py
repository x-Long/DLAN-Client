# -*-encoding:utf-8-*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class MyTableWidgetItem(QTableWidgetItem):
    def __lt__(self, other):
        if isinstance(other, QTableWidgetItem):
            my_value = self.data(Qt.UserRole)
            other_value = other.data(Qt.UserRole)
            return my_value < other_value

        return super(MyTableWidgetItem, self).__lt__(other)