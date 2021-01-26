from multiprocessing import cpu_count
from multiprocessing import Process
import os
from os import path, system
import platform
from platform import uname
import re
import subprocess
from subprocess import check_output
from sys import platform as os_name
from typing import List

import netifaces
import psutil
from platform import release
from utils.basic_utils import humanize_bytes, force_decode
from utils.time_utils import epoch_to_local_date


_WINDOWS = 'windows'
_LINUX = 'linux'
_MACOS = 'macos'

StartMapTools = {
    _WINDOWS: 'explorer.exe',
    _LINUX: 'xdg-open',
    _MACOS: 'open'
}


class OSUtils:
    @staticmethod
    def get_sys_version() -> str:
        return "{}-{}".format(OSUtils.get_arch_name(), release())

    @staticmethod
    def get_sysname():
        if OSUtils.is_windows():
            return _WINDOWS
        elif OSUtils.is_macos():
            return _MACOS
        else:
            return _LINUX

    @staticmethod
    def get_arch_name():
        if OSUtils.is_mips64():
            return "mips64"
        elif OSUtils.is_arm64():
            return "aarch64"
        elif OSUtils.is_windows():
            return _WINDOWS
        elif OSUtils.is_linux():
            return _LINUX
        elif OSUtils.is_macos():
            return _MACOS
        else:
            raise NotImplementedError("not supported architecture {}".format(os_name))

    @staticmethod
    def is_posix():
        return OSUtils.is_linux() or OSUtils.is_macos()

    @staticmethod
    def is_mips64():
        machine = uname()[4]
        return machine == "mips64"

    @staticmethod
    def is_arm64():
        machine = uname()[4]
        return machine == "aarch64"

    @staticmethod
    def is_linux():
        return os_name == 'linux'

    @staticmethod
    def is_macos():
        return os_name == 'darwin'

    @staticmethod
    def is_windows():
        return os_name == 'win32'

    @staticmethod
    def open_with_app(filepath):
        assert filepath is not None
        toolname = StartMapTools.get(OSUtils.get_sysname())
        assert toolname is not None
        cmd = '{} "{}"'.format(toolname, filepath)
        Process(target=OSUtils.shell_run, args=(cmd,), daemon=True).start()

    @staticmethod
    def open_folder(filepath):
        if OSUtils.is_windows():
            cmd = 'explorer.exe  "{}", vbNormalFocus'.format(filepath)
            si = subprocess.STARTUPINFO()
            si.wShowWindow = subprocess.SW_HIDE
            subprocess.call(cmd, startupinfo=si)
        else:
            OSUtils.open_with_app(filepath)

    @staticmethod
    def open_parent_dir(filepath):
        if OSUtils.is_windows():
            cmd = 'explorer.exe /select, "{}", vbNormalFocus'.format(filepath)
            si = subprocess.STARTUPINFO()
            si.wShowWindow = subprocess.SW_HIDE
            subprocess.call(cmd, startupinfo=si)
        else:
            OSUtils.open_with_app(path.dirname(filepath))

    @staticmethod
    def shell_run(cmd, dry=False) -> str:
        assert len(cmd) > 0
        if OSUtils.is_windows():
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            # si.wShowWindow = subprocess.SW_HIDE
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si)
            # output = subprocess.call(cmd, startupinfo=si)
            output = p.communicate()[0]
            output = force_decode(output)
        else:
            output = check_output(cmd, shell=True)
            output = force_decode(output).strip()
        return output

    @staticmethod
    def get_working_cpu_count():
        """
        using all cpu cores make machine slow and fan also make big noisy
        """
        total_cpu = cpu_count()
        # leave 1 cpu for other programs
        work_cpu = int(total_cpu / 2)
        work_cpu = 1 if work_cpu == 0 else work_cpu
        return work_cpu


def get_boot_time() -> str:
    epoch_seconds = psutil.boot_time()
    return epoch_to_local_date(epoch_seconds)


def get_mac_and_ip() -> List:
    """
    List value's format is a tuple with tree elements: (if_name, mac, ip)
    like this: ('eno1', 'F8:B1:56:9A:C2:6D', '192.168.3.250')
    """
    interface_list = netifaces.interfaces()
    network_info_list = []
    for if_name in interface_list:
        dev_info = netifaces.ifaddresses(if_name)
        if netifaces.AF_LINK not in dev_info:
            continue
        mac = dev_info[netifaces.AF_LINK][0]['addr'].upper()
        if dev_info.get(netifaces.AF_INET):
            ip = dev_info[netifaces.AF_INET][0]['addr']
            if ip != '127.0.0.1':
                s = (if_name, mac, ip)
                network_info_list.append(s)
    return network_info_list


def get_processor_name():
    if OSUtils.is_windows():
        return platform.processor()
    elif OSUtils.is_macos():
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command = "sysctl -n machdep.cpu.brand_string"
        return OSUtils.shell_run(command)
    elif OSUtils.is_linux():
        command = "cat /proc/cpuinfo"
        all_info = OSUtils.shell_run(command)
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub(".*model name.*:", "", line, 1).strip()
    return ""


def get_hostname() -> str:
    import socket
    hostname = socket.gethostname()
    return hostname


def get_memory_info() -> str:
    s = psutil.virtual_memory()
    total = humanize_bytes(s.total)
    used = humanize_bytes(s.used)
    free = humanize_bytes(s.free)
    return "总共: {} 已用: {} 剩余: {}".format(total, used, free)


if __name__ == '__main__':
    s = OSUtils.get_sys_version()
    print(s)
