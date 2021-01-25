import shutil
import json
from os import path
from directory_config import DirectoryConfig
from decorators import singleton
from utils.basic_utils import force_decode
from utils.log_utils import logger


# you should implement default_json and config_path as property
# https://stackoverflow.com/questions/1325673/how-to-add-property-to-a-class-dynamically
class BaseConfig(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self):
        super().__init__()
        j = self._load_data()
        for k, v in j.items():
            self[k] = v

    def check_and_restore(self) -> dict:
        if not self.should_restore:
            return {}
        src_file = self._get_install_path()
        if not path.exists(src_file):
            raise FileNotFoundError(src_file)
        shutil.copyfile(self._get_install_path(), self.get_config_path())
        logger.debug("restore from {}".format(self._get_install_path()))
        with open(self._get_install_path(), "r") as fp:
            j = json.load(fp)
            return j

    def _load_data(self) -> dict:
        config_path = self.get_config_path()
        if not path.exists(config_path):
            return self.check_and_restore()
        elif path.getsize(config_path) == 0:
            logger.warning("empty {}".format(config_path))
            return self.check_and_restore()
        else:
            logger.debug("{} load config {}".format(self._class_name(), config_path))
            with open(config_path,  'rb') as fp:
                buf = force_decode(fp.read())
                return json.loads(buf)

    def _class_name(self):
        return type(self).__name__

    def _get_config_filename(self):
        return "{}.json".format(self._class_name().lower())

    def _get_install_path(self):
        return path.join(DirectoryConfig.INSTALL_DIR, "data", self._get_config_filename())


class InstalledConfig(BaseConfig):
    @property
    def should_restore(self):
        return False

    def get_config_path(self):
        return path.join(DirectoryConfig.INSTALL_DIR, "data", self._get_config_filename())


class RuntimeConfig(BaseConfig):
    def get_config_path(self):
        return path.join(DirectoryConfig.RUNTIME_DATA_DIR, self._get_config_filename())

    @property
    def should_restore(self):
        return True

    def save(self):
        save_path = self.get_config_path()
        with open(save_path, 'w') as fp:
            json.dump(self, fp)


@singleton
class AppMetaInfo(InstalledConfig):
    """
    generate appmetainfo.json to <app_install_dir>/data follow below format
    {
        "version": "0.0.0",
        "packaged_name": "not_exists"
    }"""
    @property
    def is_network_client(self):
        return self.get("is_network_client", False)

    @property
    def app_cn_name(self) -> str:
        return self.get("app_cn_name", "朗威计算机终端保密检查系统")

    @property
    def company_name(self) -> str:
        return "西安帝岚电子科技有限公司"

    @property
    def version(self) -> str:
        return self.get("version", "10.0.0")

    def is_report_edition(self) -> bool:
        return self.get("is_report_edition", False)

    @property
    def commit(self) -> str:
        return self.get("commit", "debug-version")

    def is_cn_test(self) -> bool:
        return self.get("test_on_cn_release", False)

    def enable_scan_img(self) -> bool:
        return self.get("enable_scan_img", True)

    def is_enable_scan_dwg(self) -> bool:
        return self.get('support_dwg', True)


@singleton
class StrategyConfig(RuntimeConfig):
    kMaxUpdateCount = 3
    @property
    def enable_compress(self):
        return self["enable_compress"] == 1

    @property
    def ignore_dup_file(self):
        return self["ignore_dup_file"] == 1

    @property
    def can_erase_file(self):
        # disable erase file by default
        return self.get("can_erase_file", True)

    def set_erase_file(self, enable):
        self['can_erase_file'] = int(enable)
        self.save()

    def increase_update_count(self):
        current_version = AppMetaInfo.version
        count = self.get(current_version, 0) + 1
        self[current_version] = count
        self.save()

    def should_check_update(self) -> bool:
        current_version = AppMetaInfo.version
        return self.get(current_version, 1) < StrategyConfig.kMaxUpdateCount

    def get_update_count(self) -> int:
        current_version = AppMetaInfo.version
        return self.get(current_version, 1)

    def reset_update_count(self):
        self[AppMetaInfo.version] = 0
        self.save()

    def max_reconnect_timeout_seconds(self) -> int:
        return self.get("max_reconnect_timeout_seconds", 10 * 60)

    def save_ukey_auth_info(self, epoch_seconds:int, code: str):
        self['ukey_auth_info'] = (epoch_seconds, code)
        self.save()

    def get_ukey_auth_info(self) -> tuple:
        return self.get('ukey_auth_info', (0, 0))


if __name__ == '__main__':
    StrategyConfig.reset_update_count()
    print(StrategyConfig.get_update_count())
