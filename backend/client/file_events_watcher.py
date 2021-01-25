from time import sleep
from os import path

from directory_config import DirectoryConfig
from global_variables import GlobalVariables
from scan_config import ScanConfig
from utils.log_utils import logger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils.file_utils import get_watching_path, is_subdir
from decorators import singleton


class MyEventHandler(FileSystemEventHandler):
    def __init__(self):
        self._is_mute = False

    def set_mute(self, is_mute):
        assert isinstance(is_mute, bool)
        self._is_mute = is_mute
        logger.info("set is_mute = %r", self._is_mute)

    def notify_checker_thread(self, file_path):
        if self._is_mute:
            return
        extension = path.splitext(file_path)[1]
        if extension.lower() in ScanConfig.DefaultScanSuffix:
            filename = path.basename(file_path)
            if filename.startswith(".~"):
                logger.warning("ignored tmp file [{}] from".format(filename, file_path))
                return
            for ignored_dir in DirectoryConfig.IGNORED_DIRS:
                if is_subdir(ignored_dir, file_path):
                    return
            if not GlobalVariables.realtime_reports_list.count(file_path):
                GlobalVariables.realtime_reports_list.append(file_path)
                logger.info("[+] %s", file_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.notify_checker_thread(event.dest_path)

    def on_created(self, event):
        if not event.is_directory:
            self.notify_checker_thread(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.notify_checker_thread(event.src_path)


@singleton
class FileEventsWatcher:
    def __init__(self, path_list=get_watching_path()):
        assert isinstance(path_list, list)
        assert len(path_list) > 0
        self.watch_path = path_list
        self.is_started = False
        self.observer = None
        self.eventHandle = MyEventHandler()

    def mute(self):
        self.eventHandle.set_mute(True)

    def un_mute(self):
        self.eventHandle.set_mute(False)

    def wait(self):
        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

    def start_async(self):
        if self.observer:
            logger.info("skip as file watcher already started")
            return
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # hide watchdog errors
            self.observer = Observer()
            for path in self.watch_path:
                try:
                    self.observer.schedule(self.eventHandle, path, recursive=True)
                    logger.info("watching %s", path)
                except PermissionError:
                    # macos watch ~/Documents raise this error
                    logger.warning("failed watch %s", path)
            self.observer.start()
            logger.info("file watcher start finished")

    def stop(self):
        if self.observer is not None:
            self.observer.stop()
            self.observer.join()
