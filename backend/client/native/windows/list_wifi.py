from struct import unpack
from i18n import I18N
from utils.system_utils import OSUtils
from typing import List
import winreg

class WifiPassNotFoundError(Exception):
    pass

def parse_SYSTEMTIME(binary_date: bytes) -> str:
    # date = b'\xe4\x07\x05\x00\x05\x00\x1d\x00\x10\x00\x1d\x00\x2f\x00\x07\x00'
    # https://docs.python.org/3/library/struct.html
    # https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-systemtime?redirectedfrom=MSDN
    year, month, day_of_week, day, hour, minute, second, ms = unpack('h' * 8, binary_date)
    return "{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second)

def list_wifi_names() -> List[str]:
    cmd_line = 'netsh wlan show profiles'
    cmd_output = OSUtils.shell_run(cmd_line)
    cmd_output = cmd_output.replace('\r', '')
    ls = cmd_output.split('\n')[4:]
    i = 0
    wifi_name_list = []
    for line in ls:
        if line.find(':') > 0:
            _, wifi_name = line.split(':')
            wifi_name_list.append(wifi_name.strip())
    return wifi_name_list


class WifiRegistry:
    def __init__(self):
        self.wifi_reg_path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList'
        self.hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.wifi_reg_path)
        self.count = 0

    def get_wifi_date(self):
        a = winreg.EnumKey(self.hKey, self.count)
        self.count + 1
        print(a)



def get_wifi_password(wifi_name: str) -> str:
    cmd_line = 'netsh wlan show profile "{}" key=clear'.format(wifi_name)
    cmd_output = OSUtils.shell_run(cmd_line)
    output_lines = cmd_output.replace('\r', '').split('\n')
    for line in output_lines:
        line = line.strip()
        if line.startswith(I18N.tr('Key Content')):
            password = line.split(':')[1].strip()
            return password
    return I18N.tr('not encrypted')
