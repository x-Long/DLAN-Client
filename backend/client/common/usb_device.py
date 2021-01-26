from threading import Thread
from common.scaner_filter import ScanSettings
from global_variables import GlobalVariables
from directory_config import DirectoryConfig
from native.native_os import NativeOS
from scan_config import ScanConfig
from scanner.list_file import list_dirs
from utils.log_utils import logger
from os import path, makedirs, remove
from utils.time_utils import get_current_date


class UsbScanner:
    """
        AU-119 always scan all files from usb flash device whenever it plug in
        but do not scan it when client restart and the device has been scanned
    """

    def __init__(self, usb_info):
        self.usb_info = usb_info
        self.usb_record_dir = DirectoryConfig.USB_DATA_DIR
        if not path.exists(self.usb_record_dir):
            makedirs(self.usb_record_dir)
        self.config_path = path.join(self.usb_record_dir, self.usb_info.device_id())

    def should_scan_this_usb(self) -> bool:
        """
            one device flagged by device_name should not being scanned twice within a day
            save report_date to file after upload all usb files reports
        :return:
        """
        if not path.exists(self.config_path):
            return True
        with open(self.config_path, 'r') as fp:
            line = fp.readline()
        last_report_date = line
        today_date = get_current_date()
        return today_date != last_report_date

    def list_files_from_usb(self):
        count = 0
        sc_filter = ScanSettings()
        sc_filter.set_filter_file_suffix(ScanConfig.DefaultScanSuffix)
        for file_path in list_dirs([self.usb_info.mount_dir], sc_filter):
            count += 1
            logger.info("prepare analyzing usb file %s", file_path)
            GlobalVariables.add_report_path(file_path)
        logger.info("found %d files from [%s] mount on [%s]",
                    count,
                    self.usb_info.model,
                    self.usb_info.mount_dir)

    def save_report_time(self):
        with open(self.config_path, 'w') as fp:
            today_date = get_current_date()
            fp.write(today_date)
            logger.info("save report time {} for {}".format(today_date, self.usb_info.model))

    def remove_flag_file(self):
        if path.exists(self.config_path):
            remove(self.config_path)
            logger.info("remove %s", self.config_path)


# AU-119 upload usb name and serials to server when report logs belongs to a usb flash device
class UsbDeviceEvent:
    def __init__(self, background=False):
        self.run_in_back = background
        self._thread = None

    @property
    def all_usb_path(self) -> list:
        ks = self.mounted_usb_map.keys()
        return list(ks)

    def scan_new_usb(self, usb_info):
        usb_scanner = UsbScanner(usb_info)
        logger.info("plug in {}".format(usb_info.mount_dir))
        usb_scanner.list_files_from_usb()
        usb_scanner.save_report_time()

    def loop(self):
        for usb_info in NativeOS.instance().list_removable_drives():
            self.scan_new_usb(usb_info)
        while True:
            for usb_info in NativeOS.instance().wait_for_new_usb():
                self.scan_new_usb(usb_info)

    def start_async(self):
        if self._thread is not None:
            logger.info("skip start as already exists {}".format(self._thread.name))
            return
        self._thread = Thread(target=self.loop, daemon=True, name="usb_event_thread")
        self._thread.start()


if __name__ == '__main__':
    a = UsbDeviceEvent()
    a.loop()
