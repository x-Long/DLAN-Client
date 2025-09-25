# from secrets import token_bytes
import random


def token_bytes(nSize):
    s = bytearray(random.getrandbits(8) for _ in range(nSize))
    return bytes(s)
