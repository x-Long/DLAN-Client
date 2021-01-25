from os import name, getenv

PROCESS_NAME = 'audit'
TOOLS_LOGGER_NAME = 'doc-to-text'
STATISTIC_LOGGER_NAME = 'statistic'
PUBLIC_SERVER_HOST = 'bmb1688.com'

UTF8_ENCODING = 'utf-8'
ENABLE_JSON_OUTPUT = False


# decrease multiprocess lock competitions
PROCESS_LOCK_SLEEP_SECONDS = 0.01

PARSER_TIMEOUT_SECONDS = 20
RECONNECT_INTERVAL_SECONDS = 5

KEYWORD_FILENAME = 'Specialkeywords.txt'

UTF8_SPACE = b'\xc2\xa0'

if name == 'nt':
    NEW_LINE = '\r\n'
else:
    NEW_LINE = '\n'


class WorkerNames:
    PARSER_WORKER_NAME = 'parser-files-worker'
    SCANNER_WORKER_NAME = 'scanner-worker'
    COLLECTOR_WORKER_NAME = 'collect-result-worker'


class KeywordsConf:
    SEP = '-'
    MatchMultipleKeywords = True
    # one line min size should be 3 "RANK-KEYWORD"
    MinKeywordLineLen = 3
    MaxMatchedKeywordsCount = 3
    MaxKeywordContextLen = 64
    NEW_LINE = ['\n', '\r\n']


IS_DEBUG = getenv('DEBUG') is not None
