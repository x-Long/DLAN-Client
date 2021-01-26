import time

from common.scaner_filter import ScanSettings
from decorators import singleton
from scanner.keywords_manager import KeywordsManager
from scanner.scanner_manage import ScannerManager
from utils.statistic_utils import timeit_statistic


@singleton
class GlobalStatus:
    _instance = None

    def __init__(self):
        self._scan_task = []

    def scan_file(self, path_list:list, file_suffix: list, keyword_list: list) -> int:
        ss = ScanSettings()
        ss.set_filter_file_suffix(file_suffix)
        KeywordsManager.load_from_list(keyword_list)
        task = ScannerManager(path_list, ss)
        task.start()
        self._scan_task.append(task)
        return len(self._scan_task)-1

    @timeit_statistic
    def get_scan_status(self, task_id: str, page_size: str):
        assert task_id.isdigit()
        assert page_size.isdigit()

        index = int(task_id)
        if index < 0 or index >= len(self._scan_task):
            return 'invalid task_id'
        task = self._scan_task[index]
        scan_results = []
        max_count = int(page_size)
        while len(scan_results) < max_count and not task.is_finished():
            report_event = task.get_result_or_null()
            if report_event is not None:
                scan_results.append(report_event.http_result())
            else:
                time.sleep(0.1)

        status = "finished" if task.is_finished() else "scanning"
        response = {
            "status": status,
            "results": scan_results
        }
        return response
