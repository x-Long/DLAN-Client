# -*-encoding:utf-8-*-

from time import sleep
from utils.log_utils import logger
from threading import Thread


def run_in_background(func):
    def wrapper(*args, **kw):
        if kw:
            logger.debug("call %s(): args: %s, %s", func.__name__, args, kw)
        elif args:
            logger.debug("call %s(): args: %s", func.__name__, args)
        try:
            t = Thread(target=func, name=func.__name__, args=args, kwargs=kw)
            # quit when main thread exit
            t.setDaemon(True)
            t.start()
        except Exception as ex:
            logger.exception("uncaught exception", exc_info=ex)
    return wrapper


@run_in_background
def foo_1(args="a1"):
    while True:
        print("foo_1", args)
        sleep(3)


def foo_2():
    while True:
        print("foo_2")
        sleep(3)


if __name__ == '__main__':
    foo_1("hahaha")
    foo_2()
