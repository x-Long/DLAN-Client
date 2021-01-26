# -*-encoding:utf-8-*-
import json
from os import path

from utils.img_utils import is_img_contain_text


class ScanSettings:
    def __init__(self):
        # switches
        self.enable_filter_time = False
        self.enable_filter_file_size = False
        self.enable_filter_file_suffix = False
        self.enable_filter_resolution = False

        # values
        self.selected_time = None
        self.pic_must_have_text = False
        self.custom_suffix_list = None

        # backwards or forwards
        self.is_before_selected_time = False
        self.selected_min_file_bytes = None
        self.selected_max_file_bytes = None
        self.selected_file_suffix_list = None

        self.min_resolution = None

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def set_filter_time(self, filter_time: float, is_before_selected_time: bool):
        self.enable_filter_time = True
        self.is_before_selected_time = is_before_selected_time
        self.selected_time = filter_time
        return self

    def set_filter_size(self, min_size: str, max_size: str):
        self.enable_filter_file_size = True
        self.selected_min_file_bytes = min_size
        self.selected_max_file_bytes = max_size
        return self

    def set_filter_resolution(self, first: int, second: int):
        self.enable_filter_resolution = True
        self.min_resolution = (first, second)

    def set_filter_file_suffix(self, suffix_list):
        self.enable_filter_file_suffix = True
        self.selected_file_suffix_list = suffix_list
        return self

    def is_match(self, file_path) -> bool:
        if self.enable_filter_time:
            file_mtime = path.getmtime(file_path)
            if self.is_before_selected_time:
                if file_mtime > self.selected_time:
                    return False
            else:
                # after selected time
                if file_mtime < self.selected_time:
                    return False
        if self.enable_filter_file_size:
            file_size = path.getsize(file_path)
            if file_size < self.selected_min_file_bytes:
                return False
            if file_size > self.selected_max_file_bytes:
                return False
        return True


def get_settings_from_argus(size_limit=None,
                            filter_time: float = None,
                            is_before: bool = None,
                            suffix_list=None) -> ScanSettings:
    ss = ScanSettings()
    if size_limit is not None:
        s, l = size_limit
        ss.set_filter_size(s, l)
    if filter_time is not None:
        ss.set_filter_time(filter_time, is_before)
    if suffix_list is not None:
        ss.set_filter_file_suffix(suffix_list)
    return ss
