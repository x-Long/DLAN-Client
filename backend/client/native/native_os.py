from decorators import singleton
from utils.system_utils import OSUtils
from native.abstract_os import AbstractOS


@singleton
class NativeOS(AbstractOS):
    def __init__(self):
        self._instance = None

    def instance(self) -> AbstractOS:
        if self._instance is not None:
            return self._instance
        if OSUtils.is_windows():
            from native.windows_os import WindowsNative
            self._instance = WindowsNative()
        elif OSUtils.is_linux():
            from native.linux_os import LinuxNative
            self._instance = LinuxNative()
        elif OSUtils.is_macos():
            from native.macos import MacNative
            self._instance = MacNative()
        else:
            raise NotImplementedError(OSUtils.get_arch_name())
        return self._instance


if __name__ == '__main__':
    # s = NativeOS.instance().list_removable_drives()
    s = NativeOS.instance().partition_list
    print(s)
