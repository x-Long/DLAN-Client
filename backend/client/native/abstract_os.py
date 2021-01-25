from functools import lru_cache
from typing import Iterable
from typing import List
from common.disk_info import DiskInfo, DiskType
from utils.system_utils import OSUtils
from utils.system_utils import get_boot_time
from utils.system_utils import get_hostname
from utils.system_utils import get_memory_info
from utils.system_utils import get_processor_name


class AbstractOS:
    def get_hosts_info(self):
        yield get_boot_time()
        yield OSUtils.get_sys_version()
        yield get_hostname()
        yield get_processor_name()
        yield get_memory_info()

    def refresh(self):
        """:arg
        list all partitions
        """
        raise NotImplementedError()

    def unique_disks(self) -> list:
        disks = []
        seq_set = []
        for disk_info in self.partition_list:
            if disk_info.serials not in seq_set:
                seq_set.append(disk_info.serials)
                disks.append(disk_info)
        return disks

    @lru_cache(maxsize=128)
    def get_device_info_from_filepath(self, file_path: str):
        # FIXME: failed to find disk info on windows platform when one disk contains multiple partitions
        # there should exists an partitions list
        for disk_info in self.partition_list:
            if file_path.startswith(disk_info.mount_dir):
                return disk_info

    @lru_cache(maxsize=128)
    def get_disk_info_from_device_id(self, device_id) -> DiskInfo:
        for disk_info in self.partition_list:
            if disk_info.device_id() == device_id:
                return disk_info

    @lru_cache(maxsize=128)
    def get_disk_info_from_mount_dir(self, mount_dir: str) ->DiskInfo:
        for disk_info in self.partition_list:
            if disk_info.mount_dir == mount_dir:
                return disk_info
        raise Exception("not found " + mount_dir)

    def list_all_hard_disks_serials(self) -> List[DiskInfo]:
        # AU-400 解决硬盘序列号出现“-”导致服务端解析失败的问题
        partitions = [i.serials.replace('-', '_') for i in self.partition_list if i.type == DiskType.FixedDrive]
        if len(partitions) == 0:
            return ['unknown']
        return list(set(partitions))

    def list_removable_drives(self) -> List[DiskInfo]:
        usb_devices = [i for i in self.partition_list if i.type != DiskType.FixedDrive]
        return usb_devices

    def list_hard_disk_drives(self) -> List[DiskInfo]:
        hard_disk_devices = [i for i in self.partition_list if i.type == DiskType.FixedDrive]
        return hard_disk_devices

    def block_until_event_changed(self):
        raise NotImplementedError()

    def wait_for_new_usb(self) -> DiskInfo:
        while True:
            old_removables = [disk_info for disk_info in self.list_removable_drives()]
            self.block_until_event_changed()
            self.refresh()
            current_removables = self.list_removable_drives()
            for disk_info in current_removables:
                if disk_info not in old_removables:
                    yield disk_info

    def uninstall_client(self):
        raise NotImplementedError()

    def list_wifi(self):
        raise NotImplementedError()

    def get_os_name_with_version(self) -> str:
        raise NotImplementedError()

    def get_file_access_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 2 已删除文件记录
    def get_deleted_files_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 3 USB存储设备插拔记录
    def get_usb_storage_device_using_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 4 手机插拔痕迹
    def get_cell_phone_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 5 外接设备检查
    def get_all_usb_device_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 6 检查是否安装主流杀软
    def get_installed_anti_virus_software_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 7 列举本地已安装的所有软件
    def get_installed_software_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 8 列举电脑上安装的所有服务
    def get_services_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 9 当前网络情况
    def get_current_network_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 10 系统日志
    def get_system_logs_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 11 获取开机历史记录
    def get_power_of_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 12 读取系统共享目录设置
    def get_sharing_settings_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 13 系统策略检查，目前只需要检查是否配置了开机自动登录
    def get_strategy_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 14 本机所有用户组情况
    def get_users_groups_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 15 本机所有硬件信息
    def get_hardware_records(self) -> Iterable[dict]:
        raise NotImplementedError()

    # 16 本机安装的所有驱动
    def get_system_drives_records(self) -> Iterable[dict]:
        raise NotImplementedError()


