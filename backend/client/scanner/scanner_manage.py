from multiprocessing import Queue
from queue import Empty
from common.report_event import ReportEvent
from common.scaner_filter import ScanSettings
from file_events_watcher import FileEventsWatcher
from global_variables import GlobalVariables
from scanner.parser_manage import ParserManage
from utils.log_utils import logger
from scanner.workers.scan_file_worker import ScanFilesThread
from threading import Thread


'''
scanner -> parser -> collect_result
'''


class ScannerManager:
    def __init__(self, root_path: list, scanner_settings: ScanSettings = None, save_path: str = None):
        GlobalVariables.scanning_root = root_path
        self.path_list = root_path
        self.save_path = save_path
        self._is_finished = False
        self.result_queue = Queue()
        self.filename_queue = Queue()
        self.scanner_settings = scanner_settings
        self.scan_thread = None
        self.parser_manager = None
        self.is_started = False

    def check_result(self):
        self.scan_thread.join()
        logger.info('notifying parser manager to stop')
        self.parser_manager.notify_finished()
        self._is_finished = True

    def start_async(self, callback):
        def tmp():
            self.start()
            callback()

        Thread(target=tmp, daemon=True).start()

    def start(self):
        self.is_started = True
        GlobalVariables.is_busy = True
        # mute fs_listener otherwise local disk scan generating many FILE-OPEN events
        FileEventsWatcher.mute()

        self._is_finished = False
        self.result_queue = Queue()
        self.filename_queue = Queue()

        self.scan_thread = ScanFilesThread(self.path_list, self.filename_queue, self.scanner_settings)
        self.parser_manager = ParserManage(self.filename_queue, self.save_path, self.result_queue)

        self.scan_thread.start()
        logger.info('starting parser manager')
        self.parser_manager.start()
        if self.save_path is None:
            Thread(target=self.check_result, daemon=True).start()
        else:
            self.check_result()

    def stop(self):
        if not self._is_finished:
            self.scan_thread.stop()
        self.parser_manager.stop()
        GlobalVariables.is_busy = False
        FileEventsWatcher.un_mute()

    def pause(self):
        self.scan_thread.pause()
        self.parser_manager.pause()
        FileEventsWatcher.un_mute()

    def resume(self):
        self.scan_thread.resume()
        self.parser_manager.resume()
        FileEventsWatcher.mute()

    def is_finished(self):
        return self._is_finished and self.result_queue.empty()

    def get_result_or_null(self) -> ReportEvent:
        scan_result = None
        try:
            scan_result = self.parser_manager.output_queue.get_nowait()
        except Empty:
            pass
        finally:
            return scan_result
