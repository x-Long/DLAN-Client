# -*-encoding:utf-8-*-
import sys
"""
do not import any other utils incase of cyclical dependence
"""


def humanize_bytes(num: int, suffix='B') -> str:
    if num < 1024.0:
        return '%.1fB' % num
    for unit in ['B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def force_decode(string:bytes) ->str:
    """
    dwgtotext parse text from dwg files
    sometime neither gbk nor gbk can decode succseefully from cad file
    select longger decode result from utf8 or gbk
    """
    if not isinstance(string, bytes):
        raise ValueError('expected bytes array')
    decode_chars_count = []
    for i in ['utf8', 'gbk']:
        try:
            return string.decode(i)
        except UnicodeDecodeError as ex:
            decode_chars_count.append(ex.start)
    # neither utf8 or gbk decode successfully
    # select the longer decode one
    utf8_len, gbk_len = decode_chars_count
    selected_encoding = 'utf8' if utf8_len > gbk_len else 'gbk'
    return string.decode(selected_encoding, errors='ignore')

def is_above_python36() -> bool:
    v = sys.version_info
    return v.major==3 and v.minor>=6

if __name__ == '__main__':
    s = humanize_bytes(256052966400)
    print(s)