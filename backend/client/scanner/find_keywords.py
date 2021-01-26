from app_config import AppMetaInfo
from common.report_event import ReportEvent, MatchDetails
from conf import KeywordsConf
from scan_config import ScanConfig
from scanner.file_info import FileInfo
from scanner.keywords_manager import KeywordsManager
from utils.file_utils import get_file_suffix_with_dot
if not AppMetaInfo.is_report_edition():
    from utils.img_utils import is_img_contain_text
from utils.log_utils import logger

blank_chars = ' \t \r\n'
under_line = len(blank_chars) * '_'
translate_table = str.maketrans(blank_chars, under_line)


# AU-337 keep at most two space character according to Boss Liu's suggestion
def keep_one_underline(text: str, is_left: bool) -> str:
    trans_line = text.translate(translate_table)
    if trans_line.count('_') <= 1:
        return trans_line
    else:
        if is_left:
            # 'apple_likes_banana_' => 'apple_likes_banana'
            if trans_line[-1] == '_':
                return trans_line[:-1].replace('_', '') + '_'
        else:
            if trans_line[0] == '_':
                return '_' + trans_line[1:].replace('_', '')
        return trans_line.replace('_', '')


class KeywordsFinder:
    max_size = KeywordsConf.MaxKeywordContextLen

    def __init__(self, find_iter, file_info):
        self.find_iter = find_iter
        self.file_info = file_info

    def get_line_by_keyword_offset(self, keyword: str, keyword_size, keyword_offset) -> str:
        start_pos = keyword_offset
        end_pos = start_pos + keyword_size

        steps = keyword_size
        half_size = int(KeywordsFinder.max_size / 2)
        while steps < half_size and start_pos > 0:
            start_pos -= 1
            steps += 1
        prefix = self.file_info.file_text[start_pos:keyword_offset]

        text_len = self.file_info.text_len
        while steps < KeywordsFinder.max_size and end_pos < text_len:
            end_pos += 1
            steps += 1
        suffix = self.file_info.file_text[keyword_offset+keyword_size:end_pos]
        prefix = keep_one_underline(prefix, True)
        suffix = keep_one_underline(suffix, False)
        keyword_context = "{}{}{}".format(prefix, keyword, suffix)
        # delete head and ending new line
        # replace containing new line and space to '_' same to CloudMonitor does
        return keyword_context

    def generate_report(self) -> ReportEvent:
        report_event = ReportEvent(self.file_info)
        collected_word = set()
        for i in self.find_iter:
            offset = i.start()
            word = i.group()
            matched_count = len(collected_word)
            if not KeywordsConf.MatchMultipleKeywords and matched_count == 1:
                break
            if matched_count >= KeywordsConf.MaxMatchedKeywordsCount:
                break
            if word not in collected_word:
                collected_word.add(word)
                word_len = len(word)
                keyword_info = KeywordsManager.get_keyword_from_word(word)
                context = self.get_line_by_keyword_offset(keyword_info.word, word_len, offset)
                details = MatchDetails(keyword_info, context, offset, self.file_info.file_size)
                report_event.append(details)
        report_event.match_details.sort(key=lambda x: x.keyword.rank, reverse=True)

        return report_event


# return `ReportEvent` if file contains keyword
# else return None
def find_keyword_from_file(file_path: str) -> ReportEvent:
    file_suffix = get_file_suffix_with_dot(file_path)
    # do not scan image whose resolution less than 800x600 acoording to Boss Liu's suggestion
    if file_suffix in ScanConfig.ImageSuffixList and not is_img_contain_text(file_path):
        logger.debug("ignore not text img {}".format(file_path))
        return None
    try:
        file_info = FileInfo(file_path)
    except FileNotFoundError:
        logger.warning('{} not exists'.format(file_path))
        return None
    # logger.info(file_info.file_text)
    re_iter = KeywordsManager.finditer(file_info.file_text)
    re_iter = list(re_iter)
    if len(re_iter) > 0:
        keyword_finder = KeywordsFinder(re_iter, file_info)
        report_event = keyword_finder.generate_report()
        return report_event
    else:
        return None

if __name__ == '__main__':
    file_path = r"D:\c\2007.dwg"
    s = find_keyword_from_file(file_path)
    print(s)
