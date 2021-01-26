import shutil

from directory_config import DirectoryConfig
from os import path, system

from utils.system_utils import OSUtils


def main_script() -> str():
    script_path = 'app_config.py'
    return path.join(DirectoryConfig.SRC_DIR, script_path)


def package(script_path: str):
    tmp_dir = path.join(DirectoryConfig.TMP_DIR, 'pyinstaller')
    if path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    cmd = f'''
pyinstaller {script_path}
    --icon {DirectoryConfig.SRC_DIR}/res/audit.ico
    --add-data {DirectoryConfig.SRC_DIR}/locales;locales
    --specpath {tmp_dir}/spec
    --workpath {tmp_dir}/build
    --distpath {tmp_dir}/dist
    '''.replace('\n', ' ')
    if OSUtils.is_windows():
        cmd = cmd.replace('/', '\\')
    print(cmd)
    system(cmd)


def main():
    s = main_script()
    package(s)


if __name__ == '__main__':
    main()
