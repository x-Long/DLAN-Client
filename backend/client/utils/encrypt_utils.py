# AU-205 I come to 航天706 for packaing 银河麒麟 which only installed python3.5 that do not have secrets module
# from secrets import token_bytes
import random


def token_bytes(nSize):
    s = bytearray(random.getrandbits(8) for _ in range(nSize))
    return bytes(s)
