from common.disk_info import DiskInfo
from native.abstract_os import AbstractOS


class MacNative(AbstractOS):
    def __init__(self):
        super().__init__()
        self.partition_list = []

    def refresh(self):
        pass

    def block_until_event_changed(self):
        pass

    def uninstall_client(self):
        pass

    def list_wifi(self):
        pass

    def get_os_name_with_version(self) -> str:
        pass

