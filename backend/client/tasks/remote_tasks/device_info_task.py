# -*-encoding:utf-8-*-
from common.usb_device import UsbDeviceEvent
from native.native_os import NativeOS
from tasks.task_interface import BlockedRemoteTask


class GetDeviceInfoTask(BlockedRemoteTask):
    def __init__(self, device_id: str, usb_obj: UsbDeviceEvent):
        super().__init__()
        assert usb_obj is not None
        self._device_id = device_id
        self._usb_obj = usb_obj

    def run(self):
        device_info = NativeOS.instance().get_disk_info_from_device_id(self._device_id)
        output = {
            "id": self._device_id,
            "device": device_info.get_upload_dict()
        }
        self.set_output(output)


if __name__ == '__main__':
    usb_obj = UsbDeviceEvent()
    t = GetDeviceInfoTask("6477204758e8", usb_obj)
    t.save_task()
    t.run_task()
    s = t.get_output()
    print("get task output", s)
    t.close_task()
