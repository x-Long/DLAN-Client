import re
from typing import List

from common.custom_error import FatalException
from common.xadl_keyword import Keyword
from conf import UTF8_ENCODING, NEW_LINE, UTF8_SPACE
from os import path

from directory_config import DirectoryConfig
from utils.log_utils import logger
from conf import KeywordsConf
from re import compile
from decorators import singleton


@singleton
class KeywordsManager:
    def __init__(self, keyword_file=DirectoryConfig.KEYWORD_FILE_PATH):
        self.file_path = keyword_file
        self.keywords_list = []
        self._re_pattern = None
        self.load_keywords()

    def finditer(self, text):
        assert isinstance(text, str)
        return self._re_pattern.finditer(text)

    @property
    def keywords(self):
        return [i.word for i in self.keywords_list]

    def get_keyword_from_word(self, word):
        # AU-103 word may contains spaces whereas keywords do not have it
        # delete spaces from word before compare as spaces has been removed when loading keywords
        nospace_word = re.sub(r"[\s]*", "", word)
        for keyword in self.keywords_list:
            if keyword.word == nospace_word:
                return keyword
        words = ','.join([i.word for i in self.keywords_list])
        raise FatalException('can not find {} from {}'.format(word, words))

    def remove_duplicate_words(self):
        keywords_set = set()
        tmp_list = []
        for i in self.keywords_list:
            if i.word not in keywords_set:
                tmp_list.append(i)
                keywords_set.add(i.word)
        self.keywords_list = tmp_list

    def compile_re_pattern(self):
        keywords = ["[\s]*".join(k.word) if len(k.word) < 4 else k.word for k in self.keywords_list]
        re_pattern = '|'.join(keywords)
        self._re_pattern = compile(re_pattern)

    def dump_to_file(self):
        with open(self.file_path, 'w', encoding=UTF8_ENCODING) as fp:
            for i in self.keywords_list:
                s = f'{i.rank}-{i.word}\n'
                fp.write(s)

    def reset_keywords_file(self):
        default_keywords = """
1-秘密
1-机密
1-绝密
"""
        with open(self.file_path, 'w', encoding=UTF8_ENCODING) as fp:
            fp.write(default_keywords)
            logger.info("init default keywords str {}".format(default_keywords))

    def load_keyword_text(self) -> List[str]:
        with open(self.file_path, 'r', encoding=UTF8_ENCODING) as fp:
            buf = fp.read()
            keywords_lines = buf.split('\n')
            return keywords_lines

    # keywords are sorted by rank
    def _load_from_file(self):
        # AU-187 keywords file load failed on ZhouBo's machine reported at 2020-8-21
        # it turns out that keywords file get decode error
        try:
            keywords_lines = self.load_keyword_text()
        except UnicodeDecodeError as ex:
            logger.warning("load keyword failed", exc_info=ex)
            self.reset_keywords_file()
            keywords_lines = self.load_keyword_text()
        keywords_list = []
        for i, line in enumerate(keywords_lines):
            line = line.strip()
            # AU-52 invalid utf-8 two bytes spaces cause
            # AU-103 ignore all spaces when compare keywords
            word_bytes = line.encode(UTF8_ENCODING)
            if word_bytes.find(UTF8_SPACE) > 0:
                word_bytes = word_bytes.replace(UTF8_SPACE, b'')
                logger.debug("removing utf8 space from {}".format(word_bytes))
            line = word_bytes.decode()
            if len(line) < KeywordsConf.MinKeywordLineLen:
                logger.debug("ignore empty keyword line")
            elif line.find(KeywordsConf.SEP) < 0:
                logger.warning(f"ignore invalid keyword {line}")
            else:
                rank, keyword = line.split(KeywordsConf.SEP)
                # AU-187 when user edit keyword file on windows system with notepad
                # utf8 BOM will add automatically which will raise an ValueError on convert rant to int
                if rank.startswith('\ufeff'):
                    rank = rank.encode().decode('utf-8-sig')
                try:
                    keyword = Keyword(keyword, int(rank))
                    keywords_list.append(keyword)
                except ValueError as ex:
                    logger.error("parse keyword %s error", line, exc_info=ex)
        return keywords_list

    def load_keywords(self):
        try:
            self.keywords_list = self._load_from_file()
        except Exception as ex:
            logger.exception('failed load keywords', exc_info=ex)
            self.reset_keywords_file()
            self.keywords_list = self._load_from_file()
        self._apply()

    def _apply(self):
        self.remove_duplicate_words()
        self.keywords_list.sort(key=lambda x: x.rank)
        self.compile_re_pattern()
        self.dump_to_file()

    def load_from_list(self, keywords_list):
        self.keywords_list.clear()
        for word in keywords_list:
            keyword = Keyword(word, 1)
            self.keywords_list.append(keyword)
        self._apply()

    def show(self):
        for i in self.keywords_list:
            print(i.word, len(i.word))

    def reload(self, file_path):
        assert file_path is not None
        if path.exists(file_path):
            self.file_path = file_path
            self.keywords_list.clear()
            self._re_pattern = None

        logger.info('reload keywords from %s' % self.file_path)
        self.load_keywords()

    def to_text(self):
        return '\n'.join([x.to_json() for x in self.keywords_list])


if __name__ == '__main__':
    KeywordsManager.show()
