from utils.log_utils import logger


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner()


def ignore_uncaught_exception(func):
    def wrapper(*args, **kw):
        try:
            # quit when main thread exit
            func(*args, **kw)
        except Exception as ex:
            logger.exception("uncaught exception", exc_info=ex)
    return wrapper

