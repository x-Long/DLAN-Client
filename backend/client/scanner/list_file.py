from typing import List
from common.scaner_filter import ScanSettings
from os import path, walk

from scan_config import ScanConfig
from utils.file_utils import get_file_suffix_with_dot
from utils.img_utils import is_img_contain_text
from utils.log_utils import logger


def list_dirs(scan_dirs: List[str], sc_filter: ScanSettings):
    assert len(scan_dirs) > 0
    assert sc_filter is not None
    logger.info("scan dirs {} filters {}".format(scan_dirs, sc_filter))
    for root_dir in scan_dirs:
        accepted_suffix = sc_filter.selected_file_suffix_list
        for root, dirs, files in walk(root_dir, topdown=True):
            for filename in files:
                extension = get_file_suffix_with_dot(filename)
                file_path = path.join(root, filename)
                if extension is not None:
                    try:
                        if extension in accepted_suffix:
                            if sc_filter is None:
                                yield file_path
                            if sc_filter.is_match(file_path):
                                if extension not in ScanConfig.ImageSuffixList:
                                    yield file_path
                                else:
                                    if not sc_filter.pic_must_have_text:
                                        yield file_path
                                    else:
                                        if is_img_contain_text(file_path):
                                            yield file_path
                    except OSError as ex:
                        print(ex)


def list_acceptable_files(scan_dirs: List[str]):
    assert len(scan_dirs) > 0
    for root_dir in scan_dirs:
        accepted_suffix = ScanConfig.DefaultScanSuffix
        for root, dirs, files in walk(root_dir, topdown=True):
            for filename in files:
                extension = get_file_suffix_with_dot(filename)
                file_path = path.join(root, filename)
                if extension is not None:
                    extension = extension.lower()
                    if extension in accepted_suffix:
                        yield file_path
