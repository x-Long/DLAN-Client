import hashlib
import tempfile

from conf import IS_DEBUG
from native.native_os import NativeOS
from scan_config import ScanConfig
from utils.encrypt_utils import token_bytes
from tempfile import mkdtemp
from os import name as system_name, path, getenv, remove, listdir
from shutil import copyfile
from shutil import rmtree
from typing import List
from utils.log_utils import logger
from utils.system_utils import OSUtils


class DupFile:
    def __init__(self, src_path):
        if not path.exists(src_path):
            raise FileNotFoundError(src_path)
        self.src_path = src_path
        self.temp_dir = mkdtemp(prefix='security-audit')
        self.copied_file = path.join(self.temp_dir, path.basename(self.src_path))
        copyfile(self.src_path, self.copied_file)
        print("backup {} => {}".format(src_path, self.copied_file))

    def clean(self):
        rmtree(self.temp_dir)


def compute_file_hash(file_path):
    if not path.isfile(file_path):
        raise FileNotFoundError()
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        while True:
            buf = f.read(4096)
            if len(buf) == 0:
                break
            md5obj.update(buf)
        file_hash = md5obj.hexdigest()
        return file_hash


def get_user_home() -> str:
    if system_name == 'nt':
        home = getenv('USERPROFILE').replace('/', '\\')
    else:
        home = getenv('HOME')
    if home is None:
        raise NotImplementedError('can not find home dir')
    return home


def _get_user_path(folder_name):
    home = get_user_home()
    for lang, name in folder_name.items():
        desktop = path.join(home, name)
        if path.exists(desktop):
            return desktop
    return home


def get_desktop_path():
    desktop = {
        'zh': '桌面',
        'en': 'Desktop'
    }
    return _get_user_path(desktop)


def get_quick_scan_path():
    quick_dirs = [
        {
            'zh': '桌面',
            'en': 'Desktop'
        },
        {
            'zh': '文档',
            'en': 'Documents'
        },
        {
            'zh': '下载',
            'en': 'Downloads'
        }
    ]
    return [_get_user_path(i) for i in quick_dirs]


def get_scan_dirs_from_home(ignored_names:list=[]) -> list:
    home = get_user_home()
    path_list = []
    if len(ignored_names) > 0:
        ignored_names = [i.lower() for i in ignored_names]

    for i in listdir(home):
        if not i.startswith('.') and i.lower() not in ignored_names:
            abspath = path.join(home, i)
            if path.isdir(abspath):
                path_list.append(abspath)
    if len(path_list) == 0:
        path_list.append(home)
    return path_list


def _get_windows_scan_path() -> List:
    ignored_dirs = ScanConfig.BLACK_LIST
    path_list = get_scan_dirs_from_home(ignored_dirs)
    if ScanConfig.EnableWhileList:
        end = len(path_list) - 1
        pos = end
        while pos >= 0:
            file_path = path_list[pos]
            dir_name = path.basename(file_path)
            if dir_name not in ScanConfig.WHITE_LIST:
                path_list.remove(file_path)
            pos -= 1

    all_drives = [disk_info.mount_dir for disk_info in NativeOS.instance().partition_list]
    for letter in all_drives:
        if not letter.upper().startswith('C:\\'):
            path_list.append(letter)
    return path_list


def _get_linux_scan_path() -> List:
    path_list = get_scan_dirs_from_home()
    path_list.extend(['/tmp', '/media'])
    return path_list


def get_scan_path(is_quick=False) -> list:
    if IS_DEBUG:
        desktop = get_desktop_path()
        return [desktop]
    if is_quick:
        return get_quick_scan_path()
    if OSUtils.is_windows():
        return _get_windows_scan_path()
    elif OSUtils.is_linux():
        return _get_linux_scan_path()
    else:
        return get_scan_dirs_from_home()


def path_is_parent(parent_path, child_path):
    # Smooth out relative path names, note: if you are concerned about symbolic links, you should use os.path.realpath too
    parent_path = path.abspath(parent_path)
    child_path = path.abspath(child_path)
    return parent_path == child_path or \
           child_path.startswith(parent_path)


def filter_child_path(path_list) -> List:
    dst = []
    for child in path_list:
        is_sub = False
        for parent in dst:
            if path_is_parent(parent, child):
                is_sub = True
        if not is_sub:
            dst.append(child)
    return dst



# linux /var /opt
# maxos home only
# windows home and others none system drives
def get_watching_path():
    path_list = get_quick_scan_path()
    return path_list


def rewrite_file(file_path, file_size):
    kWriteBufSize = 1024
    with open(file_path, 'wb') as fp:
        writen_bytes = 0
        while writen_bytes < file_size:
            random_bytes = token_bytes(file_size) if file_size < kWriteBufSize else token_bytes(kWriteBufSize)
            n = fp.write(random_bytes)
            writen_bytes += n


# AU-65 support erase file by rewrite random bytes before delete it
def erase_file_by_rewrite_three_times(file_path):
    if not path.exists(file_path):
        raise FileNotFoundError(file_path)
    file_size = path.getsize(file_path)
    kReWriteTimes = 3
    for i in range(kReWriteTimes):
        rewrite_file(file_path, file_size)
    remove(file_path)


def get_file_suffix_with_dot(filename: str):
    assert len(filename) > 0
    dot_pos = filename.rfind('.')
    if dot_pos == -1:
        return None
    else:
        suffix = filename[dot_pos:]
        return suffix.lower()


def convert_path_sep_to_native_format(file_path: str) -> str:
    if OSUtils.is_windows():
        trans_table = str.maketrans('/', '\\')
    else:
        trans_table = str.maketrans('\\', '/')
    return file_path.translate(trans_table)


def return_one_native_path(func):
    def wrapper(*args, **kw):
        original_path = func(*args, **kw)
        return convert_path_sep_to_native_format(original_path)
    return wrapper


def format_path_to_native(func):
    def wrapper(*args):
        argu_count = len(args)
        i = 0
        formated_path_list = []
        while i < argu_count:
            normalized_path = convert_path_sep_to_native_format(args[i])
            formated_path_list.append(normalized_path)
            i += 1
        return func(*formated_path_list)
    return wrapper


@format_path_to_native
def a(f: str, t: str):
    print("a print", f, t)


def expand_path(file_path: str) -> str:
    s = path.expanduser(file_path)
    return convert_path_sep_to_native_format(s)


@format_path_to_native
def is_subdir(parent: str, sub: str):
    """
    make sure parent path exists
    """
    if not parent.endswith(path.sep):
        parent += path.sep
    return sub.startswith(parent)


@return_one_native_path
def generate_random_path(prefix:str='', suffix:str=''):
    tmp = getenv("TMP", "/tmp")
    tmp_filename = next(tempfile._get_candidate_names())
    filename = "{}{}{}".format(prefix, tmp_filename, suffix)
    full_path = "{}{}{}".format(tmp, path.sep, filename)
    return full_path


if __name__ == '__main__':
    s = get_watching_path()
    print(s)
