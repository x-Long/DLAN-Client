from queue import Queue
from typing import List
from zipfile import BadZipFile, ZipFile
from common.scaner_filter import ScanSettings
from conf import WorkerNames
from os import path, walk
from directory_config import DirectoryConfig
from scan_config import ScanConfig
from utils.basic_utils import humanize_bytes
from utils.file_utils import get_file_suffix_with_dot
from utils.log_utils import logger
from global_variables import GlobalVariables
from common.custom_task import PauseAbleThread
from utils.system_utils import OSUtils

EXTRACTOR_PATH = path.join(DirectoryConfig.TOOLS_DIR, '7z.exe')


def extractfile(compressed_file:str, extracted_dir: str):
    cmd = f"{EXTRACTOR_PATH} x -o{extracted_dir} {compressed_file}"
    OSUtils.shell_run(cmd)


def uncompress_package(file_path, result_queue) -> int:
    dot = file_path.rfind('.')
    if dot < 0:
        raise Exception("invalid compressed package path", file_path)

    zip_dir = path.dirname(file_path)
    zip_name = path.basename(file_path)

    extracted_dir = path.join(zip_dir, '.'+zip_name)
    cnt = 0
    try:
        with ZipFile(file_path, 'r') as zipObj:
            file_list = zipObj.namelist()
            for filename in file_list:
                tmp = path.splitext(filename)
                # skip file which do not have suffix
                if len(tmp) < 2:
                    continue
                extension = tmp[1].lower()
                if extension not in ScanConfig.DefaultScanSuffix:
                    continue
                dest_path = path.join(extracted_dir, filename)
                if not path.exists(dest_path):
                    logger.info('extract %s from %s' % (filename, file_path))
                    zipObj.extract(filename, extracted_dir)
                logger.debug('add %s' % dest_path)
                result_queue.put(dest_path)
                cnt += 1
    except BadZipFile:
        pass
    return cnt


def list_dir(root_dir, result_queue: Queue, sc_filter: ScanSettings = None):
    assert result_queue is not None
    if sc_filter is not None and sc_filter.enable_filter_file_suffix:
        accepted_suffix = sc_filter.selected_file_suffix_list
    else:
        accepted_suffix = ScanConfig.DefaultScanSuffix

    supported_compressed_suffix = ScanConfig.CompressedSuffix
    matched_count = 0
    total_count = 0
    for root, dirs, files in walk(root_dir, topdown=True):
        for filename in files:
            total_count += 1
            extension = get_file_suffix_with_dot(filename)
            file_path = path.join(root, filename)
            if extension is None:
                continue
            extension = extension.lower()
            if extension in accepted_suffix:
                scan_path = None
                if sc_filter is None:
                    scan_path = file_path
                elif sc_filter.is_match(file_path):
                    scan_path = file_path
                if scan_path is not None:
                    print(f"found {file_path}")
                    result_queue.put(file_path)
                    matched_count += 1
            elif ScanConfig.EnableScanCompressedFile and extension in supported_compressed_suffix:
                if OSUtils.is_windows():
                    suffix = file_path.replace(':', '!')
                else:
                    suffix = f'{file_path[1:]}'
                # 解压到同级目录会导致同步软件产生大量文件同步操作，尤其是 Dropbox 或 坚果云
                extracted_dir = path.join(DirectoryConfig.UNCOMPRESS_DIR, suffix)
                if not path.exists(extracted_dir):
                    logger.info(f'extract {file_path}')
                    extractfile(file_path, extracted_dir)
                dirs.append(extracted_dir)

    return matched_count, total_count


class ScanFilesThread(PauseAbleThread):
    def __init__(self, path_list, filename_queue, sc_filters=None):
        PauseAbleThread.__init__(self)
        self.name = WorkerNames.SCANNER_WORKER_NAME
        self.path_list = path_list
        self.file_path_queue = filename_queue
        self.scanner_filters = sc_filters
        logger.info('creating new scan thread')
        self.total_count = -1
        self.matched_count = -1

    def run(self):
        try:
            self.total_count, self.matched_count = list_files_by_walk(self.path_list, self.file_path_queue, self)
            logger.info('list %d files from %d files', self.matched_count, self.total_count)
        except Exception as ex:
            logger.exception("list error", exc_info=ex)
        finally:
            self.is_finished = True


def list_files_by_walk(path_list: List[str], task_queue: Queue, obj: ScanFilesThread) -> tuple:
    assert len(path_list) > 0
    assert obj is not None
    accepted_suffix = ScanConfig.DefaultScanSuffix if obj.scanner_filters is None \
        else obj.scanner_filters.selected_file_suffix_list
    logger.info("scan dirs {} file suffix list {}".format(path_list, accepted_suffix))

    total_cnt = 0
    matched_cnt = 0
    for root_dir in path_list:
        count, total = list_dir(root_dir, task_queue, obj.scanner_filters)
        matched_cnt += count
        total_cnt += total
        for root, dirs, files in walk(root_dir, topdown=True):
            if DirectoryConfig.UNCOMPRESS_DIR in dirs:
                logger.info("ignore {}".format(dirs))
                dirs.remove(DirectoryConfig.UNCOMPRESS_DIR)
            obj.check_paused()
            if not obj.keep_running:
                logger.info('stop list files')
                break
    # TODO: remove global assignment
    GlobalVariables.total_files = total_cnt
    GlobalVariables.total_suffix_matched_count = matched_cnt
    return total_cnt, matched_cnt
