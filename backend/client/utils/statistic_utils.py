import time
from utils.time_utils import to_human_time


def timeit_statistic(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        cost_ms = (te - ts) * 1000
        spent_time = to_human_time(cost_ms)
        from utils.log_utils import logger
        logger.info('%r cost: %s' % (method.__name__, spent_time))
        return result

    return timed
