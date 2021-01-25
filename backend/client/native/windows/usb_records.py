import winreg
from winreg import HKEY_LOCAL_MACHINE as HKLM


class UsbRerocrds:
    def __init__(self):
        self.usb_stor = r'SYSTEM\CurrentControlSet\Enum\USBSTOR'
        self.wanted_keys = ['FriendlyName']

    def list_details(self, sub_entry):
        i = 0
        details = {}
        while True:
            try:
                name, value, _ = winreg.EnumValue(sub_entry, i)
                i += 1
                if name in self.wanted_keys:
                    details[name] = value
            except OSError:
                return details



    def list_usb_names(self, usb_keys):
        for usb_entry in usb_keys:
            key_path = f'{self.usb_stor}\\{usb_entry}'
            try:
                reg = winreg.OpenKey(HKLM, key_path)
                sub_key = winreg.EnumKey(reg, 0)
                sub_entry = winreg.OpenKey(HKLM, f'{self.usb_stor}\\{usb_entry}\\{sub_key}')
                s = self.list_details(sub_entry)
                if len(s) != 0:
                    print(s)
            except FileNotFoundError as ex:
                raise

    def list_usb_entries(self):
        i = 0
        entries = []
        reg = winreg.OpenKey(HKLM, self.usb_stor, 0)
        while True:
            try:
                key = winreg.EnumKey(reg, i)
                entries.append(key)
                i += 1
            except OSError:
                return entries


def list_usb_records():
    u = UsbRerocrds()
    l = u.list_usb_entries()
    u.list_usb_names(l)

if __name__ == '__main__':
    list_usb_records()
