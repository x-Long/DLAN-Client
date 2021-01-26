import json
from functools import lru_cache

from utils.string_utils import hash_string
from utils.system_utils import OSUtils


class DiskType:
    FixedDrive = "HDD"
    UsbDevice = "USB"
    CdDevice = "CD-Drive"

    def __init__(self, disk_type: str):
        self.type = disk_type


class DiskInfo:
    def __init__(self,
                 model: str,
                 mount_dir: str,
                 file_system: str,
                 serials: str,
                 size: str,
                 disk_type: DiskType):
        self.model = model
        if OSUtils.is_windows() and not mount_dir.endswith('\\'):
            mount_dir += '\\'
        self.mount_dir = mount_dir
        self.file_system = file_system
        self.serials = serials.strip()
        self.size = int(size)
        self.type = disk_type.type

    def get_upload_dict(self) -> dict:
        return {
            'type': self.type,
            'model': self.model,
            'serials_number': self.serials,
            'mount_dir': self.mount_dir,
            'size_in_bytes': self.size,
        }

    @lru_cache(maxsize=128)
    def device_id(self) -> str:
        json_str = json.dumps(self.get_upload_dict(), sort_keys=True)
        md5_str = hash_string(json_str)
        device_id = md5_str[:12]
        return device_id

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4)


if __name__ == '__main__':
    d = DiskInfo("SamSung", "/mnt/C", "NTFS", "abcd1234", 1024000, DiskType("usb"))
    print(d, d.device_id())
