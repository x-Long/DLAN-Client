import re
from typing import List
from utils.log_utils import logger
from common.disk_info import DiskInfo
from common.disk_info import DiskType

# AU-84 解决在 win7 系统获取到的硬盘序列号不正确的问题
def correct_windows_disks_sn(in_sn: str):
    invalid_prefix = '202020'
    if in_sn is None:
        return ''
    if not in_sn.startswith(invalid_prefix):
        return in_sn
    dec_res = bytearray.fromhex(in_sn).decode()
    dec_len = len(dec_res)
    ltr1 = 0
    ltr2 = 2
    dec_changed = []

    for count in range(dec_len):
        if ltr1 >= dec_len:
            break
        two_ltr = dec_res[ltr1:ltr2:1]
        a = two_ltr[0]
        b = two_ltr[1]
        mix_res = b, a
        dec_changed.append(mix_res)

        ltr1 += 2
        ltr2 += 2

    dec_changed = str(dec_changed).strip('[]')
    dec_changed = re.sub(r'\(|\)|\'|,| ', '', dec_changed)
    return dec_changed



def get_disk_type_from(interface_type: str):
    if interface_type is None or interface_type.startswith('USB'):
        return DiskType(DiskType.UsbDevice)
    elif interface_type.startswith('CD'):
        return DiskType(DiskType.CdDevice)
    else:
        return DiskType(DiskType.FixedDrive)


def list_cd_drive(wmi_instance):
    DRIVE_TYPES = {
        0: "Unknown",
        1: "No Root Directory",
        2: "Removable Disk",
        3: "Local Disk",
        4: "Network Drive",
        5: "Compact Disc",
        6: "RAM Disk"
    }
    dvd_list = []
    for drive in wmi_instance.Win32_LogicalDisk():
        if drive.DriveType != 5:
            continue
        mount_dir = drive.Caption
        if drive.Size is None:
            logger.info("ignore empty CD {}".format(drive.VolumeName))
            continue
        disk_info = DiskInfo(drive.VolumeName,
                             mount_dir,
                             drive.FileSystem,
                             drive.VolumeSerialNumber,
                             drive.Size,
                             DiskType(DiskType.CdDevice))
        dvd_list.append(disk_info)
    return dvd_list


def list_all_partitions(wmi_instance) -> List[DiskInfo]:
    all_disks = []
    for physical_disk in wmi_instance.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                mount_dir = logical_disk.Caption
                type = get_disk_type_from(physical_disk.InterfaceType)
                sn = correct_windows_disks_sn(physical_disk.SerialNumber)
                disk_info = DiskInfo(physical_disk.Model,
                                     mount_dir,
                                     logical_disk.FileSystem,
                                     sn,
                                     physical_disk.Size,
                                     type)
                all_disks.append(disk_info)
    return all_disks
