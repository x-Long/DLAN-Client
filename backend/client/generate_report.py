# -*-encoding:utf-8-*-
import math
import time
from typing import List
from fpdf import FPDF
from common.report_settings import ReportSettings
from native.native_os import NativeOS
from utils.basic_utils import humanize_bytes
from utils.device_info import get_device_mac
from utils.device_info import get_network_mac
from utils.log_utils import logger
from os import path

from utils.system_utils import OSUtils
from utils.thread_decorator import run_in_background


def silent_write_pdf_to_file(pdf: FPDF, save_path: str):
    logger.info("saving reports to %s", save_path)
    assert pdf is not None
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        pdf.output(save_path, 'F')
    logger.info("save report success")


def get_font_dir() -> str:
    project_dir = path.dirname(path.realpath(__file__))
    return project_dir


def init_pdf() -> FPDF:
    font_dir = get_font_dir()

    mic_path = path.join(font_dir, 'mic_font/msyh.ttf')
    mic_bd_path = path.join(font_dir, 'mic_font/msyhbd.ttf')
    pdf = FPDF(orientation="P", format='A4', unit='in')
    # Remember to always put one of these at least once.
    pdf.add_font('msyh', '', mic_path, uni=True)
    pdf.add_font('msyhbd', '', mic_bd_path, uni=True)
    pdf.set_font('msyh', '', 10.0)
    pdf.set_draw_color(43, 109, 173)
    # Add new page. Without this you cannot create the document.
    pdf.add_page()
    return pdf


class Percent:
    Short = 1
    Middle = 2
    Long = 5


def compute_width_map(percent, base) -> dict:
    """
    when fill in pdf tables some field may longer than other fields
    we should increase that field's width manually

    by doing that automatically here is a `Percent` helper
    we can decide a field's length is short middle or long and auto campute the actual width
    with percent and base

    if base is 100 and there are 3 fields: short(1) middle(2) long(5)
    their actuall width is
    short  (1 / 8) * 100 = 12.5
    middle (2 / 8) * 100 = 25.0
    long   (5 / 8) * 100 = 62.5

    :param percent:
    :param base:
    :return:
    """
    s = sum(percent)
    len_map = {}
    for i, v in enumerate(percent):
        len_map[i] = v/s * base
    return len_map


class BaseReport:
    def __init__(self, headers, contents):
        pdf = init_pdf()
        self.epw = pdf.w - 2 * pdf.l_margin
        self.pdf = pdf
        self.col_height = 2.5 * pdf.font_size
        self.content_height = 2 * pdf.font_size
        self.table_name = "报警动态报告"
        self.headers = headers
        self.contents = contents
        self.sequence_width = 1
        self._col_width = None
        self.percent_size = None

    @property
    def content_header(self) -> str:
        return self.contents[0]

    def set_col_width(self, width_list: list):
        assert isinstance(width_list, list)
        assert len(width_list) == len(self.content_header)
        self._col_width = compute_width_map(width_list, self.epw)
        # how many characters can each column contains
        self._raw_len_array = [
            math.ceil(i/self.pdf.font_size) for i in self._col_width.values()
        ]

    def set_title(self):
        self.pdf.set_font('msyh', '', 16.0)
        self.pdf.ln(0.25)
        self.pdf.cell(self.epw, 0.0, self.table_name, align='C')
        self.pdf.set_font('msyh', '', 8.0)
        self.pdf.ln(0.5)

    def get_col_width(self, col_no) -> float:
        content_header_count = len(self.content_header) + 1
        assert 0 <= col_no
        assert col_no < content_header_count
        if self._col_width is None:
            rest_width = self.epw - self.sequence_width
            if self.percent_size is None:
                # set all fields to equal width when `percent_size` not set
                self.percent_size = [Percent.Middle for i in range(content_header_count)]
            self._col_width = compute_width_map(self.percent_size, rest_width)
        return self._col_width.get(col_no)

    def save_to_file(self, save_path: str) -> str:
        gen_date = time.strftime("%Y.%m.%d", time.localtime())
        filename = "{}_{}.pdf".format(self.table_name, gen_date)
        if save_path is None:
            save_path = filename
        silent_write_pdf_to_file(self.pdf, save_path)
        return save_path

    def make_report(self, save_path: str) -> str:
        self.set_title()
        self.set_front_header()
        self.set_content_header()
        self.set_content()
        self.save_to_file(save_path)
        return save_path

    def set_content_header(self):
        self.pdf.ln(self.col_height)
        self.pdf.set_fill_color(128, 189, 226)
        for i, word in enumerate(self.content_header):
            self.pdf.cell(self.get_col_width(i), self.col_height, word, 'LTRB', fill=True)
        self.pdf.ln(self.col_height)

    def dynamic_layout_column(self, column_no, word: str, col_max_word_count:int):
        dx_line = 0
        rest_space = col_max_word_count
        start = end = 0
        column_info = {0: word}
        line_count = 1
        for s in word:
            if '\u4e00' <= s <= '\u9fff':
                rest_space -= 1
            else:
                rest_space -= 0.5
            end += 1
            if rest_space <= 0:
                column_info[dx_line] = word[start:end]
                start = end
                rest_word = word[start:]
                rest_len = len(rest_word)
                if rest_len == 0:
                    break
                dx_line += 1
                line_count += 1
                rest_space = col_max_word_count
                column_info[dx_line] = rest_word
                if rest_len < rest_space:
                    break
        return column_info, line_count

    def set_content(self):
        self.pdf.set_fill_color(206, 212, 218)
        all_lines = self.contents[1:]
        for row_no, row in enumerate(all_lines):
            len_arr = []
            line_max_words = []
            # 计算每一列需要多少行
            for column_no in range(0, len(row)):
                column_text = str(row[column_no])
                col_max_word_count = self._raw_len_array[column_no]
                column_info, column_need_lines = self.dynamic_layout_column(column_no, column_text, col_max_word_count)
                line_max_words.append(column_info)
                len_arr.append(column_need_lines)
            # 计算当前报告行所需列数最大值
            max_lines = max(len_arr)
            is_color = bool(row_no % 2 != 0)
            last_index = max_lines - 1
            scale_height = self.content_height * 0.8
            for dx_index in range(0, max_lines):
                align = 'LR' if dx_index != last_index else 'LRB'
                height = scale_height if dx_index != last_index else self.content_height
                for row_index, row_value in enumerate(row):
                    column_info = line_max_words[row_index]
                    if column_info is not None:
                        word = column_info.get(dx_index, '')
                        column_width = self.get_col_width(row_index)
                        self.pdf.cell(column_width, height, word, align, fill=is_color)
                self.pdf.ln(height)

    def set_front_header(self):
        if self.headers is None:
            return
        if len(self.headers) > 1:
            header_fields_count = len(self.headers[0])
        else:
            header_fields_count = len(self.headers)
        header_width = self.epw / header_fields_count
        self.pdf.set_fill_color(128, 189, 226)
        for i, line in enumerate(self.headers):
            for item in line:
                # item is a tuple
                if len(item) == 2:
                    title, value = item
                    content = "{}: {}".format(title, value)
                else:
                    content = item[0]
                content = '-' if content is None else content
                self.pdf.cell(header_width, self.col_height, content, 'LTRB', fill=True)
            self.pdf.ln(self.col_height)
        return self.pdf


class LocalScanReport(BaseReport):
    def __init__(self, title: str, front_header, contents):
        super().__init__(front_header, contents)
        self.contents = contents
        self.table_name = title
        content_header = contents[0]
        content_header_len = len(content_header)
        content_line = contents[-1]
        content_len = len(content_line)

        if content_header_len != content_len:
            raise ValueError("content len not equal header len {} != {}\n{} vs {}".format(
                            content_header_len, content_len,
                            content_header, content_line))


def get_current_time():
    t = time.strftime("%Y.%m.%d %H:%M", time.localtime())
    return t


def generate_report(username: str,
                    contents: List,
                    is_suspect: bool) -> LocalScanReport:
    name_str = "未知用户" if username is None else username
    report_count = len(contents) - 1
    suspect_word = "疑似" if is_suspect else "未确定"
    generate_time = get_current_time()

    #TODO: 主机信息独占一行，每个网卡名称和网卡地址占一行，每个磁盘信息占一行
    disk_info = []
    for i, disk in enumerate(NativeOS.instance().unique_disks()):
        disk_info.append(
            [
                ('磁盘', i+1),
                (disk.model, ),
                ('实际容量', humanize_bytes(disk.size)),
                (disk.serials, )
            ]
        )
    mac_addr = [('网卡地址',)]
    t = get_device_mac()
    mac_count = len(t)
    if mac_count > 3:
        t = t[:3]
    elif mac_count < 3:
        rest_space = 3 - mac_count
        for _ in range(rest_space):
            t.append('-')
    for mac in t:
        mac_addr.append(
            (mac, )
        )

    headers = [
                [
                ("用户名", name_str),
                ("判定类型", suspect_word),
                ('生成时间', generate_time),
                ("报告总数", report_count)
                ],
                mac_addr,
        ]
    headers.extend(disk_info)

    title = f"{name_str}-{suspect_word}-自查报告"
    s = LocalScanReport(title, headers, contents)
    return s


@run_in_background
def save_scan_report_as_pdf(user_name: str, save_path: str, report_fields: List, report_settings: ReportSettings, finish_signal=None) -> str:
    content_header_map = {
        "序号": Percent.Short,
        "文件名": Percent.Middle,
        "大小": Percent.Short,
        "创建时间": Percent.Middle,
        "关键字": Percent.Short,
        "位置": Percent.Short,
        "上下文": Percent.Long,
        "路径": Percent.Long
    }
    if not report_settings.want_filename:
        content_header_map.pop("文件名")
    if not report_settings.want_filesize:
        content_header_map.pop("大小")
    if not report_settings.want_createtime:
        content_header_map.pop("创建时间")
    if not report_settings.want_keyword:
        content_header_map.pop("关键字")
    if not report_settings.want_offset:
        content_header_map.pop("位置")
    if not report_settings.want_context:
        content_header_map.pop("上下文")
    if not report_settings.want_path:
        content_header_map.pop("路径")

    content_header = list(content_header_map.keys())
    contents = report_fields
    contents.insert(0, content_header)

    s = generate_report(user_name, contents, report_settings.want_suspect)
    col_width_fields = list(content_header_map.values())
    s.set_col_width(col_width_fields)
    s.make_report(save_path)
    if finish_signal is not None:
        finish_signal.emit()