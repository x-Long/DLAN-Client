from time import time, strftime, localtime, gmtime


def to_day_hour_min_sec(ms):
    days = hours = minutes = seconds = 0
    if ms >= 1000:
        seconds = ms / 1000
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
    return days, hours, minutes, seconds


def to_human_time(ms):
    if ms < 1000:
        return '%d ms' % ms
    d, h, m, s = to_day_hour_min_sec(ms)

    time_map = {
        'days': d,
        'hours': h,
        'minutes': m,
        'seconds': s,
    }
    output = ''
    for k, v in time_map.items():
        if k == 'seconds':
            fmt = '%.2f %s'
        else:
            fmt = '%d %s '

        if v > 0:
            output += fmt % (v, k)
    return output.strip()


def timeit(method):
    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result

    return timed


def get_formatted_time(fmt='%Y-%m-%d %H:%M'):
    return strftime(fmt, localtime(time()))


def get_current_date(fmt='%Y-%m-%d'):
    return strftime(fmt, localtime(time()))


def epoch_to_local_date(epoch_seconds: float) -> str:
    s = localtime(epoch_seconds)
    display_date = "%04d-%02d-%02d %02d:%02d" % (s.tm_year, s.tm_mon, s.tm_mday, s.tm_hour, s.tm_min)
    return display_date

def get_elapsed_time_text(elapsed_ms):
    d, h, m, s = to_day_hour_min_sec(elapsed_ms)
    if d == 0:
        msg = '%02d:%02d:%02d' % (h, m, s)
    else:
        msg = '%d 天 %02d:%02d:%02d' % (d, h, m, s)
    return msg
