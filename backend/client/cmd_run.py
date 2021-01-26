# -*-encoding:utf-8-*-
import sys
from directory_config import DirectoryConfig
from scanner.find_keywords import find_keyword_from_file
from scanner.list_file import list_acceptable_files
from scanner.scanner_manage import ScannerManager
from os import path
from utils.file_utils import get_scan_path


def multiprocess_run(path_list: list):
    txt_file = path.join(DirectoryConfig.TMP_DIR, 'multi_scan.txt')
    s = ScannerManager(path_list, save_path=txt_file)
    s.start()


def scan_with_single_thread(path_list: list):
    for i in list_acceptable_files(path_list):
        print('scanning', i)
        s = find_keyword_from_file(i)
        print(s)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_list = sys.argv[1:]
    else:
        path_list = get_scan_path()
    multiprocess_run(path_list)
