from decorators import singleton
from scanner.scanner_manage import ScannerManager


@singleton
class GlobalStatus:
    _instance = None

    def __init__(self):
        self._scan_task = []

    def scan_file(self, path_list:list, settings):
        task = ScannerManager(path_list, settings)
        self._scan_task.append(task)
        return len(self._scan_task)

    def get_scan_status(self, task_id: str):
        self._scan_task.get(task_id)
        r = {
            "status": "on scan",
            "results": [
                {
                    "filename": "测试文件.docx",
                    "filesize": "4.3 MB",
                    "keyword_details": {
                        "matched_keyword": "秘密",
                        "keyword_offset": 1721,
                        "keyword_context": "这是一个秘密的文件",
                    }
                }
            ],
        }
        return r
