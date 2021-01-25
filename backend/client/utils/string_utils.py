# -*-encoding:utf-8-*-

import random
import string
from os import path, makedirs
from hashlib import sha256


def generate_random_str(default_len=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(default_len))


def generate_random_path(root="/tmp", should_create=True):
    assert root is not None
    if not path.exists(root):
        makedirs(root)
    while True:
        dirname = generate_random_str()
        full_path = path.join(root, dirname)
        if not path.exists(full_path) and should_create:
            makedirs(full_path)
            print("making", full_path)
            return full_path


def hash_string(text) -> str:
    assert text
    assert len(text) > 0
    b_text = text.encode()
    m = sha256(b_text)
    s_text = m.hexdigest()
    return s_text


# AU-263 shorten keyword context and delete '_'
# AU-343 需求：
#   pdf显示 “关键字上下文” 时，只保留关键字两边的下划线且最多保留两个。
# AU-343 设计思路：
#   将 context 划分为 3 部分：
#   "++++++++keyword++++++++"
#      1   |    2    |   3
#   2: 关键字部分，包括关键字和左右两边的两个字符。
#   1: 关键字区域前的部分
#   3: 关键字区域后的部分
#   将 1、3 部分的下滑线替换为空，然后重新拼接3个部分，
#   写成伪码类似于：
#       context = sec1.replace('_', '') + sec2 + sec3.replace('_', '')
def shorter_context(keyword: str, context: str) -> str:
    max_context_size = 24
    pos = context.find(keyword)
    if pos < 0:
        return context[:max_context_size].replace('_', '')
    else:
        # AU-343
        if pos >= 3:
            # 如果 pos 前存在至少 3 个字符，sec1 区域才存在
            # xxxKEYxxxxxx
            #    ^
            #    +-- pos
            context = context[:pos-2].replace('_', '') + context[pos-2:]
            pos = context.find(keyword)
        if pos + len(keyword) + 2 < len(context):
            # 如果 keyword 后存在至少 3 个字符，sec3 区域才存在
            # xxxxxxxxKEYxxxxxx
            #         ^  ^ ^   ^-- len(_context)
            #         |  | +-- pos + len(keyword) + 2
            #         |  +-- pos + len(keyword)
            #         +-- pos
            context = context[:pos + len(keyword)+2] + context[pos + len(keyword)+2:].replace('_', '')
        word_len = len(keyword)
        keyword_pos = context.find(keyword)
        if keyword_pos >= max_context_size:
            return context[keyword_pos:keyword_pos+max_context_size]
        else:
            return context[:max_context_size]
