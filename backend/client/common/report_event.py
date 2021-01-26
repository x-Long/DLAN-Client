from common.custom_error import FatalException
from common.usb_device import UsbDeviceEvent
from directory_config import DirectoryConfig
from common.xadl_keyword import Keyword
from conf import ENABLE_JSON_OUTPUT
from json import dumps

from native.native_os import NativeOS
from utils.file_utils import compute_file_hash
from utils.time_utils import get_formatted_time


class MatchDetails:
    def __init__(self, keyword_info, keyword_context, offset, file_size):
        if not isinstance(keyword_info, Keyword):
            raise FatalException("{} {} is not Keyword".format(type(keyword_info), keyword_info))
        self.keyword = keyword_info
        self.context = keyword_context
        self.offset = offset
        self.file_size = file_size

    # hash and eq method ensure we can merge the save scan result to one
    def __hash__(self):
        return hash("{} {}".format(self.context, self.offset))

    def __eq__(self, other):
        return self.file_size == other.file_size and self.context == other.context

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def to_text(self):
        return '{rank}-{word}-{repeat_times}-{offset}:{size}|{context}'.format(
            rank=self.keyword.rank, word=self.keyword.word,
            repeat_times=1, offset=self.offset, size=self.file_size, context=self.context)

    @property
    def key_info(self):
        return '{rank}-{word}-{repeat_times}-{offset}:'.format(
            rank=self.keyword.rank, word=self.keyword.word,
            offset=self.offset, repeat_times=1)

    def __str__(self):
        return self.to_text()


class ReportEvent:
    def __init__(self, file_info):
        super().__init__()
        self.log_time = get_formatted_time()
        self.file_size_in_bytes = file_info.file_size
        self.characters_count = file_info.text_len
        self.filename = file_info.filename
        self.file_path = file_info.file_path
        self.match_details = []
        self._file_hash = None
        self.dup_list = []
        if self.file_path.startswith(DirectoryConfig.UNCOMPRESS_DIR):
            self.display_path = self.file_path[len(DirectoryConfig.UNCOMPRESS_DIR)+1:].replace('!', ':')
        else:
            self.display_path = self.file_path


    @property
    def file_hash(self):
        if self._file_hash is None:
            self._file_hash = compute_file_hash(self.file_path)
        return self._file_hash

    def to_text(self):
        _text = self.display_path + '|'
        # report the first keyword match details which keyword-rank is highest
        md = self.match_details[0]
        _text += md.to_text()
        return _text

    def http_result(self):
        md = self.get_one_match_detail()
        return {
            "filepath": self.file_path,
            "filesize": self.file_size_in_bytes,
            "keyword_details": {
                "keyword": md.keyword.word,
                "offset": md.offset,
                "context": md.context
            }
        }

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def append(self, match_details):
        self.match_details.append(match_details)

    def get_keyword_position(self) -> int:
        return self.match_details[0].offset

    def get_one_match_detail(self) -> MatchDetails:
        return self.match_details[0]

    def get_values(self):
        md = self.get_one_match_detail()
        return [self.filename,
                self.file_size_in_bytes,
                md.offset,
                md.keyword.word,
                md.context,
                # AU-59 show original path if it is a compressed file
                (self.file_path, self.display_path)]

    def __str__(self):
        if ENABLE_JSON_OUTPUT:
            return self.to_json()
        else:
            return self.to_text()

    def get_report_log(self) -> str:
        match_info = self.match_details[0]
        # AU-119 if report file not belongs to usb device_id is '0'
        # device_id = NativeOS.instance().get_device_info_from_filepath(self.file_path).device_id()
        # TODO: linux 系统磁盘列举存在问题，暂时屏蔽次功能
        device_id = 0
        return '%s\n%s\n%s\n%s %s\n%s' % (self.log_time,
                                          self.file_hash,
                                          match_info.key_info,
                                          device_id,
                                          match_info.context,
                                          self.file_path)
