# -*- coding: utf-8 -*-
from multiprocessing import Value as SharedValue
from os import path
from queue import Queue
from shutil import rmtree

from utils.time_utils import to_human_time
from app_config import AppMetaInfo


class GlobalVariables:
    scanning_root = []
    notifications_queue = Queue()
    status_queue = None
    tray_status_queue = Queue()
    realtime_reports_list = []
    # 记录扫描时的压缩包解压路径，等待扫描完毕后逐一清除
    uncompressed_dirs = []
    total_analyzing_ms = SharedValue('d', 0)
    # hide login window when client auto start
    is_auto_start = False
    is_busy = False
    mutex = None

    total_files = 0
    total_suffix_matched_count = 0
    matched_keywords_count = 0
    unique_files_count = 0
    username = None

    @staticmethod
    def record_convert_ms(ms):
        with GlobalVariables.total_analyzing_ms.get_lock():
            GlobalVariables.total_analyzing_ms.value += ms

    @staticmethod
    def get_spent_time():
        return to_human_time(GlobalVariables.total_analyzing_ms.value)

    @staticmethod
    def get_dict():
        return {
            'scanning_root': GlobalVariables.scanning_root,
            'total_analyzing_time': to_human_time(GlobalVariables.total_analyzing_ms.value),
            'concurrent_process_count': GlobalVariables.concurrent_process_count,

            'total_files': GlobalVariables.total_files,
            'total_suffix_matched_count': GlobalVariables.total_suffix_matched_count,
            'matched_keywords_count': GlobalVariables.matched_keywords_count,
            'unique_files_count': GlobalVariables.unique_files_count,
            'version': AppMetaInfo.version
        }

    @staticmethod
    def add_report_path(file_path):
        # TODO: save scan path persistent so we can report it when client restarted
        assert len(file_path) > 0
        if not GlobalVariables.realtime_reports_list.count(file_path):
            GlobalVariables.realtime_reports_list.append(file_path)

    @staticmethod
    def get_report_path():
        try:
            return GlobalVariables.realtime_reports_list.pop(0)
        except IndexError:
            return None

    @staticmethod
    def set_login_status(msg: str):
        assert msg is not None
        GlobalVariables.status_queue = msg

    @staticmethod
    def get_login_status() -> str:
        return GlobalVariables.status_queue

class Notification:
    def __init__(self, title, body):
        self.title = title
        self.body = body


def set_notify(title: str, body: str):
    notify = Notification(title, body)
    GlobalVariables.notifications_queue.put(notify)
