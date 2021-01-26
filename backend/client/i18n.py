import json

from decorators import singleton
from locale import getdefaultlocale
from os import path

@singleton
class I18N:
    start_scan = '开始扫描'
    quick_scan = '快速扫描'
    pause_scan = '暂停扫描'
    resume_scan = '恢复扫描'

    scanning_files = '正在扫描'
    finish_scan = '扫描完成'
    scan_has_paused = '扫描已暂停'
    scan_has_stopped = '扫描已停止'

    login_now = '正在登陆...'

    mark_suspect = '标为疑似'
    withdraw_mark = '取消标记'

    def __init__(self):
        self.locale = getdefaultlocale()[0]
        # macos get None
        if self.locale is None:
            self.locale = 'zh_CN'
        # TODO: delete below line when we have foreign customers
        self._language = {}
        if not self.is_english_locale():
            self.load_locales()

    def load_locales(self):
        current_dir = path.dirname(path.abspath(__file__))
        locale_dir = path.join(current_dir, 'locales')
        locale_filename = "{}.json".format(self.locale)
        json_path = path.join(locale_dir, locale_filename)
        with open(json_path, 'r', encoding="utf8") as fp:
            self._language = json.load(fp)

    def is_chinese_lang(self) -> bool:
        return self.locale[:2] == 'zh'

    def is_english_locale(self) -> bool:
        return self.locale[:2] == 'en'

    def tr(self, word: str) -> str:
        return self._language.get(word, word)


if __name__ == '__main__':
    s = I18N.tr('failed connect to remote server')
    print(s)
