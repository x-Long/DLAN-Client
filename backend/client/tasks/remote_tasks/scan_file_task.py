# -*-encoding:utf-8-*-
from os import path

from tasks.task_interface import NoneBlockRemoteTask
from directory_config import DirectoryConfig
from scanner.scanner_manage import ScannerManager
from utils.file_utils import get_scan_path


class DiskScanTask(NoneBlockRemoteTask):
    def __init__(self, is_quick: bool, filename: str):
        super().__init__()
        self._result_file = path.join(DirectoryConfig.RUNTIME_DATA_DIR, filename)
        self._scan_path = get_scan_path(is_quick)
        self.scanner = ScannerManager(self._scan_path, save_path=self._result_file)

    def run(self):
        self.scanner.start_async(self.set_finished)


if __name__ == '__main__':
    s = DiskScanTask(True, "quick.rlog")
    s.run()