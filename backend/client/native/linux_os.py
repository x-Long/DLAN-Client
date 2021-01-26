import psutil
from time import sleep
from common.disk_info import DiskInfo
from common.disk_info import DiskType
from native.abstract_os import AbstractOS
from service.service_ctl import UnixDomainClient
from shutil import which
from app_config import AppMetaInfo
from typing import Iterable
import os
from xml.etree import ElementTree
from urllib.parse import unquote
import getpass
from datetime import datetime
import configparser
import json
import shlex
import subprocess as sp


RECENTUSED_XML_PATH = os.path.expanduser("~/.local/share/recently-used.xbel")
RECENTDOC_DIR_PATH = os.path.expanduser("~/.local/share/RecentDocuments")

TRASH_DIR_PATH = os.path.expanduser("~/.local/share/Trash")
TRASHFILE_DIR_PATH = os.path.join(TRASH_DIR_PATH, "files")
TRASHINFO_DIR_PATH = os.path.join(TRASH_DIR_PATH, "info")

def list_all_partitions():
    partitions = psutil.disk_partitions()
    all_disks = []
    for p in partitions:
        usg = psutil.disk_usage(p.mountpoint)
        mount_dir = p.mountpoint
        if not mount_dir.startswith('/media'):
            continue
        model = 'unknown'
        serials = 'unknown'
        disk_type = DiskType(DiskType.UsbDevice)
        disk_info = DiskInfo(model,
                             mount_dir,
                             p.fstype,
                             serials,
                             usg.total,
                             disk_type)
        all_disks.append(disk_info)
    return all_disks


class LinuxNative(AbstractOS):
    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        partitions = list_all_partitions()
        self.partition_list = partitions

    def block_until_event_changed(self):
        last_count = len(self.list_removable_drives())
        usb_check_interval_seconds = 3
        while True:
            partitions = psutil.disk_partitions()
            current_count = len([p for p in partitions if p.mountpoint.startswith('/media')])
            if current_count != last_count:
                last_count = current_count 
                return
            else:
                sleep(usb_check_interval_seconds)
    
    def uninstall_client(self):
        packaged_name = AppMetaInfo.packaged_name
        manager = 'apt' if which('apt') is not None else 'yum'
        cmd = "{} remove -y {}".format(manager, packaged_name)
        return UnixDomainClient().invoke_service_run(cmd)

    def get_file_access_records(self) -> Iterable[dict]:
        if os.path.isfile(RECENTUSED_XML_PATH):
            etree = ElementTree.parse(RECENTUSED_XML_PATH)
            for bookmark in etree.findall("bookmark"):
                if 'href' in bookmark.attrib:
                    href = bookmark.attrib['href']
                    if href.startswith("file://"):
                        href = href[7:]
                    href = unquote(href)
                    yield {
                        "username": getpass.getuser(),
                        "access_time": bookmark.attrib['visited'],
                        "file_path": href,
                        "is_exists": os.path.exists(href)
                    }
        elif os.path.isdir(RECENTDOC_DIR_PATH):
            for desktop_file in os.listdir(RECENTDOC_DIR_PATH):
                desktop_filepath = os.path.join(RECENTDOC_DIR_PATH, desktop_file)
                config = configparser.ConfigParser()
                config.read(desktop_filepath)

                stat = os.stat(desktop_filepath)
                filepath = None
                for k, v in config["Desktop Entry"].items():
                    if k.lower().startswith("url") and v.startswith("file:"):
                        filepath = v.lstrip("file:")

                if filepath is None:
                    continue

                filepath = os.path.expanduser(filepath)
                filepath = os.path.expandvars(filepath)

                yield {
                    "username": getpass.getuser(),
                    "access_time": datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
                    "file_path": filepath,
                    "is_exists": os.path.exists(filepath)
                }

    def get_deleted_files_records(self) -> Iterable[dict]:
        if os.path.isdir(TRASHFILE_DIR_PATH) and os.path.isdir(TRASHINFO_DIR_PATH):
            for filename in os.listdir(TRASHFILE_DIR_PATH):
                info_filename = os.path.join(TRASHINFO_DIR_PATH, filename + ".trashinfo")
                config = configparser.RawConfigParser()
                config.read(info_filename)

                filepath = unquote(config['Trash Info']['Path'])
                yield {
                    "file_path": filepath,
                    "delete_time": datetime.fromisoformat(config['Trash Info']['DeletionDate']).strftime(
                        "%Y-%m-%d %H:%M:%S"),
                }

    def _read_udev_log(self, filename, value_maps):
        try:
            with open(filename) as fp:
                for line in fp.readlines():
                    record = json.loads(line)

                    result = dict()
                    for k, v in value_maps.items():
                        result.update({
                            k: v(record)
                        })
                    yield result
        except FileNotFoundError:
            pass

    def get_usb_storage_device_using_records(self) -> Iterable[dict]:
        """
        read udev log from /var/log/udev-disks.log
        """
        return self._read_udev_log("/var/log/udev-disks.log", {
            "device_name": lambda x: x.get("ID_MODEL"),
            "manufacture": lambda x: x.get("ID_VENDOR_FROM_DATABASE"),
            "serials": lambda x: x.get("ID_SERIAL_SHORT"),
            "last_plugin_time": lambda x: x["time"],
        })

    def get_cell_phone_records(self) -> Iterable[dict]:
        """
        read udev log from /var/log/udev-android.log
        """
        return self._read_udev_log("/var/log/udev-android.log", {
            "serial": lambda x: x.get("ID_SERIAL_SHORT"),
            "manufacture": lambda x: x.get("ID_VENDOR_FROM_DATABASE"),
            "device_name": lambda x: x.get("ID_MODEL"),
            "last_plugin_time": lambda x: datetime.fromisoformat(x["time"]).strftime("%Y-%m-%d %H:%M:%S"),
        })

    def get_all_usb_device_records(self) -> Iterable[dict]:
        """
        read udev log from /var/log/udev-all.log
        """
        return self._read_udev_log("/var/log/udev-all.log", {
            "serial": lambda x: x.get("ID_SERIAL_SHORT"),
            "manufacture": lambda x: x.get("ID_VENDOR_FROM_DATABASE"),
            "device_name": lambda x: x.get("ID_MODEL"),
            "last_plugin_time": lambda x: datetime.fromisoformat(x["time"]).strftime("%Y-%m-%d %H:%M:%S"),
        })

    def get_installed_anti_virus_software_records(self) -> Iterable[dict]:
        return filter(lambda record: 'com.qihoo.360safe' == record.get("name"), self.get_installed_software_records())

    def get_installed_software_records(self, sep="####SEP####") -> Iterable[dict]:
        import shutil
        dpkg = shutil.which("dpkg")
        rpm = shutil.which("rpm")

        proc = None
        if dpkg is not None:
            proc = sp.run(shlex.split("dpkg-query -W -f '" + sep + "\\n${Package}|${Version}\\n${Description}\\n'"),
                          stdout=sp.PIPE, stderr=sp.PIPE)
        if rpm is not None:
            proc = sp.run(
                shlex.split("rpm -qa --queryformat '" + sep + "\\n%{name}|%{version}-%{release}\\n%{description}\\n'"),
                stdout=sp.PIPE, stderr=sp.PIPE)

        if proc is not None:
            stdout = proc.stdout.decode()
            packages = filter(lambda x: x.strip(), stdout.split(sep))
            for package in packages:
                lines = list(filter(None, (package.strip() for package in package.splitlines())))
                name, version = lines[0].strip().split("|")
                description = "\n".join(lines[1:])

                yield {
                    "name": name,
                    "version": version,
                    "description": description,
                }

    def get_services_records(self) -> Iterable[dict]:
        for service_type in ("system", "user"):
            proc = sp.run(
                shlex.split("systemctl list-unit-files --type service --no-legend --no-pager --" + service_type),
                stdout=sp.PIPE)
            service_units = dict(line.strip().split() for line in proc.stdout.decode().splitlines())

            proc = sp.run(shlex.split("systemctl list-units --type service --no-legend --no-pager --all"),
                          stdout=sp.PIPE, stderr=sp.PIPE)
            stdout = proc.stdout.decode()
            services = stdout.splitlines(False)
            for service in map(lambda s: s.strip(), services):
                name, loaded, active, running, description = service.split(maxsplit=4)
                if name not in service_units:
                    continue

                proc = sp.run(["systemctl", "show", "--property", "MainPID", "--value", name], stdout=sp.PIPE,
                              stderr=sp.PIPE)
                pid = int(proc.stdout)

                yield {
                    "name": name,
                    "display_name": description,
                    "start_type": "auto" if service_units[name] == "enabled" else "disabled" if service_units[
                                                                                                    name] == "masked" else "manual",
                    "process_id": pid,
                    "is_system_service": service_type == "system",
                    "status": running,
                }

    def get_current_network_records(self) -> Iterable[dict]:
        import socket
        return map(lambda conn: dict(
            protocol="tcp" if conn.type == socket.SOCK_STREAM else "udp" if conn.type == socket.SOCK_DGRAM else "raw",
            local_ip=conn.laddr.ip,
            local_port=conn.laddr.port,
            remote_ip=conn.raddr.ip if conn.raddr else '',
            remote_port=conn.raddr.port if conn.raddr else 0,
            status=conn.status.lower(),
            pid=conn.pid,
            program_path=psutil.Process(conn.pid).exe() if conn.pid else '-',
            process_name=psutil.Process(conn.pid).name() if conn.pid else 'unknown',
        ), filter(lambda conn: conn.family in (socket.AddressFamily.AF_INET, socket.AddressFamily.AF_INET6),
                  psutil.net_connections()))

    def get_system_logs_records(self) -> Iterable[dict]:
        pass

    def get_power_off_records(self, wtmp_path="/var/log/wtmp") -> Iterable[dict]:
        import utmp
        with open(wtmp_path, "rb") as fp:
            for record in utmp.read(fp.read()):
                if record.user == 'reboot':
                    yield dict(
                        time=record.time.strftime("%Y-%m-%d %H:%M:%S"),
                        event="power on",
                    )
                elif record.user == 'shutdown':
                    yield dict(
                        time=record.time.strftime("%Y-%m-%d %H:%M:%S"),
                        event="power off",
                    )

    def get_sharing_settings_records(self) -> Iterable[dict]:
        pass

    def get_strategy_records(self) -> Iterable[dict]:
        res = os.popen(
            "cat /etc/lightdm/lightdm.conf | grep ^autologin").readlines()
        res1 = "".join(res).split("=")
        item = {
            "user": "",
            "is_auto_login": False,
        }
        if len(res) == 0 or res1[-1] == "\n":
            yield item
        elif res1[-1] == "\n":
            yield item
        else:
            yield {
                "user": res1[-1][:-1],
                "is_auto_login": True,
            }

    def get_users_groups_records(self) -> Iterable[dict]:
        res = os.popen("cat /etc/group").readlines()

        for i in range(len(res)):
            group = res[i].split(":")
            yield {
                "group_name": group[0],
                "group_id": group[2],
                "members": group[-1][:-1]
            }

    def get_hardware_records(self) -> Iterable[dict]:
        with open('/proc/cpuinfo') as fd:
            for line in fd:
                if line.startswith('model name'):
                    cpu_model = line.split(':')[1].strip().split()
                    cpu_model = cpu_model[0] + ' ' + \
                                cpu_model[2] + ' ' + cpu_model[-1]
                    yield {'kind': 'CPU 处理器', 'info': cpu_model.strip()}

        with os.popen('sudo fdisk -l') as fd:
            for line in fd:
                if line.startswith('Disk /dev'):
                    cpu_model1 = line.split(':')[-1][:-1]
                elif line.startswith('Disk model: '):
                    cpu_model = line.split(':')[-1][:-1] + cpu_model1
                    yield {'kind': "硬盘", 'info': cpu_model.strip()}

        with os.popen('sudo dmidecode -t 2') as fd:
            for line in fd:
                line = line.strip()
                if line.startswith('Manufacturer'):
                    cpu_model1 = line.split(':')[-1][:-1]
                elif line.startswith('Product Name'):
                    cpu_model = line.split(':')[-1][:-1] + cpu_model1
                    yield {'kind': "主板", 'info': cpu_model.strip()}

        with os.popen('/sbin/ifconfig') as fd:
            for line in fd:

                if line.split(" ")[0] != "":
                    name = line.split(":")[0]
                if 'ether' in line:
                    yield {
                        "name": name,
                        "address": line.split()[1]
                    }

    def get_system_drives_records(self) -> Iterable[dict]:
        path_list = []

        def get_all(path):
            paths = os.listdir(path)
            for i in paths:
                com_path = os.path.join(path, i)
                if os.path.isdir(com_path):
                    get_all(com_path)
                elif os.path.isfile(com_path):
                    path_list.append(com_path)
            return path_list

        path_list = get_all("/lib/modules/" + os.listdir("/lib/modules")[0] + "/kernel/drivers")
        for path in path_list:
            name = path.split("/")[-1][:-3]
            with os.popen('modinfo ' + name) as fd:
                description = ''
                for line in fd:
                    if line.startswith('description'):
                        description = line.split(':')[-1].strip()
            yield {
                "name": name,
                "description": description,
                "install_time": str(datetime.fromtimestamp(os.stat(path).st_ctime))[0:19],
            }


