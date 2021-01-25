from json import dumps

from conf import UTF8_SPACE


def encode_keyword(keyword):
    # convert special space to normal space
    de = keyword.encode().replace(UTF8_SPACE, b'\x20')
    word = de.decode()
    # remove character '*' SPACE from keyword
    word = word.replace('*', '').replace(' ', '')
    return word


class Keyword:
    def __init__(self, keyword, rank):
        self.word = encode_keyword(keyword)
        self.rank = rank

    def __str__(self):
        return "{}-{}".format(self.rank, self.word)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.word == other.word and self.rank == other.rank

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @property
    def rank_text(self) -> str:
        rank_map = {
            1: "特殊",
            2: "严重",
            3: "重要",
            4: "一般"
        }
        return rank_map.get(self.rank, "未定义")