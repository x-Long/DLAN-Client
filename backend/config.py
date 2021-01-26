import json
from os import path
from utils.basic_utils import force_decode


def load_server_config() -> dict:
    fp = open("config.json", "rb")
    row_line = fp.read()
    txt_line = force_decode(row_line)
    d = json.loads(txt_line)
    return d


class PathConfig:
    AppRoot = ''
    BackendDir = path.join(AppRoot, 'backend')
    ConfigPath = path.join(BackendDir, 'config.json')


class RuntimeConfig:
    def __init__(self):
        self._server_config = None
        pass

    def instance(self):
        pass

    def get_server_config(self) -> dict:
        if self._server_config is None:
            self._server_config = load_server_config()
        return self._server_config

