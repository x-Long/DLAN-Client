import subprocess
from os import path
import netifaces

from native.native_os import NativeOS


def get_network_mac(is_internet: bool = True):
    '''
    use the mac that connected to Internet
    docker or other virtual mac address may change which cause user login failed
    '''
    MAC_SIZE = 17
    VMWARE_MAC_PREFIX = "00:50:56"
    LOCALHOST_MAC = "00:00:00:00:00:00"
    card_type = netifaces.AF_INET if is_internet else netifaces.AF_LINK
    mac_list = []
    for if_name in netifaces.interfaces():
        if_info = netifaces.ifaddresses(if_name)
        inet_info = if_info.get(card_type)
        if inet_info is not None and if_info.get(netifaces.AF_LINK) is not None:
            mac = if_info[netifaces.AF_LINK][0].get('addr', '')
            mac = mac.upper()
            if len(mac) == MAC_SIZE and mac != LOCALHOST_MAC and not mac.startswith(VMWARE_MAC_PREFIX):
                if is_internet:
                    return mac
                else:
                    mac_list.append(mac)
    if is_internet:
        raise Exception("获取登录网卡地址失败")
    else:
        return mac_list


def get_device_mac() -> list:
    # TODO: testing on macos
    # AU-219 mysql computerInf hostMac is 64 bytes which can store 3 mac at most
    max_register_mac_num = 5
    mac_list = get_network_mac(False)
    return mac_list[:max_register_mac_num]


def get_harddisks_serials():
    return NativeOS.instance().list_all_hard_disks_serials()


if __name__ == '__main__':
    s = get_device_mac()
    print(s)
