import os
from os import path, makedirs, getenv
import platform
from conf import PROCESS_NAME
from utils.system_utils import OSUtils
import sys


# as Boss Liu want all user on the same machine can login automatically
# I set the application data to this absolute path
# and adjust its permission to 777 on installer script
_DEFAULT_DATA_DIR = "/var/xadl/client"


class DirectoryConfig:
        IS_FROZEN = getattr(sys, 'frozen', False)
        # app depends dirs
        INSTALL_DIR = path.dirname(__file__)
        SRC_DIR = path.join(path.dirname(INSTALL_DIR), 'src')
        PROJECT_DIR = path.dirname(SRC_DIR)
        if OSUtils.is_windows():
            RUNTIME_ROOT = path.join(getenv("APPDATA"), PROCESS_NAME)
        else:
            RUNTIME_ROOT = _DEFAULT_DATA_DIR
            # above path is not writable when client installation script not executed
            # set it to user home for developer or other test users
            if not os.access("test", os.W_OK):
                RUNTIME_ROOT = path.expanduser("~/.audit")
        RUNTIME_DATA_DIR = path.join(RUNTIME_ROOT, 'data')
        USB_DATA_DIR = path.join(RUNTIME_DATA_DIR, "usb")
        # TODO: save task dir to sqlite not file
        TASK_DIR = path.join(RUNTIME_DATA_DIR, "tasks")
        LOG_DIR = path.join(RUNTIME_ROOT, "logs")

        TMP_DIR = path.join(RUNTIME_ROOT, 'tmp')
        TMP_UPDATE_DIR = path.join(TMP_DIR, "tmp_update")
        UNCOMPRESS_DIR = path.join(TMP_DIR, 'uncompress')
        CONFIG_FILE = path.join(RUNTIME_DATA_DIR, 'config.ini')
        need_create = [
                    RUNTIME_ROOT,
                    TMP_DIR,
                    RUNTIME_DATA_DIR,
                    TASK_DIR
            ]
        TEST_DATA_DIR = path.join(PROJECT_DIR, "tests", "data")
        KEYWORD_FILE_PATH = path.join(RUNTIME_DATA_DIR, 'keywords.bin')
        # make pid path global unique if put it under user home wont make sure only one instance exists
        PID_FILE = path.join(TMP_DIR, 'audit.pid')
        UPDATE_FLAG_PATH = path.join(TMP_DIR, 'audit.update')
        INVOKE_FILE = path.join(TMP_DIR, "invoke-open")
        INVOKE_EXIT_FILE = path.join(TMP_DIR, "invoke-exit")
        for i in need_create:
            if not path.exists(i):
                makedirs(i)

        # AU-58 tools dir locate at different path when its been packaged with pyinstaller
        if IS_FROZEN:
            TOOLS_DIR = path.join(INSTALL_DIR, 'tools')
            OCR_DATA_DIR = path.join(TOOLS_DIR, 'tessdata')
        else:
            machine = platform.uname()[4]
            tool_dir = path.join(path.dirname(INSTALL_DIR), 'tools')
            INSTALL_DIR = SRC_DIR
            OCR_DATA_DIR = path.join(tool_dir, 'tessdata')
            TOOLS_DIR = path.join(tool_dir, OSUtils.get_arch_name())

        # resource file
        icon_names = {
            "normal": "audit.png",
            "online": "online.png",
            "offline": "offline.png"
        }
        RES_DIR = path.join(INSTALL_DIR, 'res') if IS_FROZEN else path.join(SRC_DIR, 'res')
        AUDIT_ICON = path.join(RES_DIR, "audit.png")

        # design
        design_dir = path.join('gui', 'design')
        DESIGN_DIR = path.join(INSTALL_DIR, design_dir)
        MAIN_WINDOW_UI = path.join(DESIGN_DIR, 'realtime_scan.ui')

        IGNORED_DIRS = [RUNTIME_ROOT]
