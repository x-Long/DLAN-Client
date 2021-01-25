from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QFileIconProvider
from utils.file_utils import get_file_suffix_with_dot
from decorators import singleton


@singleton
class FileIconsManage:
    def __init__(self):
        self._cache = {}

    def find_file_icon(self, file_path):
        suffix = get_file_suffix_with_dot(file_path)
        if suffix in self._cache:
            icon = self._cache.get(suffix)
            return icon
        else:
            file_info = QFileInfo(file_path)
            iconProvider = QFileIconProvider()
            icon = iconProvider.icon(file_info)
            self._cache[suffix] = icon
            return icon
