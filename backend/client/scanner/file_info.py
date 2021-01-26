import subprocess
from os import path
from os import environ
from time import time

from conf import PARSER_TIMEOUT_SECONDS
from scan_config import ScanConfig
from utils.basic_utils import force_decode
from global_variables import GlobalVariables
from directory_config import DirectoryConfig
from utils.system_utils import OSUtils
from scanner.file_type import get_file_type, UnsupportedFileType
from scanner.file_type import FileType
from utils.basic_utils import is_above_python36
from utils.log_utils import logger

PDFTOTEXT_NAME = 'pdftotext'
DOCTOTEXT_NAME = 'doctotext'
OCRTOTEXT_NAME = "imgtotext"
DWGTOTEXT_NAME = "dwgtotext"

if OSUtils.is_windows():
    DOCTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, '{0}\\{0}.exe'.format(DOCTOTEXT_NAME))
    PDFTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, '{0}\\{0}.exe'.format(PDFTOTEXT_NAME))
    IMGTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}\\{0}.exe".format(OCRTOTEXT_NAME))
    DWGTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}\\{0}.exe".format(DWGTOTEXT_NAME))
elif OSUtils.is_linux():
    DOCTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, DOCTOTEXT_NAME)
    # finding that uos-20 have pdftotext by default so we do not package it to installer
    PDFTOTEXT_PATH = PDFTOTEXT_NAME
    DWGTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}/{0}".format(DWGTOTEXT_NAME))
    IMGTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}/{0}".format(OCRTOTEXT_NAME))
elif OSUtils.is_macos():
    DOCTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}/{0}".format(DOCTOTEXT_NAME))
    PDFTOTEXT_PATH = PDFTOTEXT_NAME
    # finding that uos-20 have pdftotext by default so we do not package it to installer
    DWGTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}/{0}".format(DWGTOTEXT_NAME))
    IMGTOTEXT_PATH = path.join(DirectoryConfig.TOOLS_DIR, "{0}/{0}".format(OCRTOTEXT_NAME))
else:
    raise NotImplementedError(OSUtils.get_arch_name())

if PDFTOTEXT_PATH == PDFTOTEXT_NAME:
    if is_above_python36():
        file_path = subprocess.check_output("command -v {}".format(PDFTOTEXT_NAME), shell=True, encoding='utf-8').strip()
    else:
        file_path = subprocess.check_output("command -v {}".format(PDFTOTEXT_NAME), shell=True).strip().decode()
    PDFTOTEXT_PATH = file_path
elif not path.exists(PDFTOTEXT_PATH):
    raise FileNotFoundError(PDFTOTEXT_PATH)
if not path.exists(DOCTOTEXT_PATH):
    raise FileNotFoundError(DOCTOTEXT_PATH)


# AU-132 hide console window when call Popen with pyinstaller on windows 
# https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess
def subprocess_args(include_stdout=True):
    # The following is true only on Windows.
    if hasattr(subprocess, 'STARTUPINFO'):
        # On Windows, subprocess calls will pop up a command window by default
        # when run from Pyinstaller with the ``--noconsole`` option. Avoid this
        # distraction.
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # Windows doesn't search the path by default. Pass it an environment so
        # it will.
        env = environ
    else:
        si = None
        env = None
    if include_stdout:
        ret = {'stdout': subprocess.PIPE}
    else:
        ret = {}

    # On Windows, running this from the binary produced by Pyinstaller
    # with the ``--noconsole`` option requires redirecting everything
    # (stdin, stdout, stderr) to avoid an OSError exception
    # "[Error 6] the handle is invalid."

    env = {
        'TESSDATA_PREFIX': DirectoryConfig.OCR_DATA_DIR,
    }
    ret.update({'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': si,
                'env': env})
    return ret


class FileInfo:
    def __init__(self, file_path):
        if not path.exists(file_path):
            raise FileNotFoundError
        self.file_path = file_path
        self.txt_path = None
        self._txt_buff = None
        self._cmdline = None
        self.text_len = None
        self.file_type = get_file_type(self.file_path)

    def generate_cmd(self):
        file_type = self.file_type
        if file_type == FileType.PdfType:
            self._cmdline = [PDFTOTEXT_PATH, self.file_path, '-']
        elif file_type == FileType.OfficeType:
            self._cmdline = [DOCTOTEXT_PATH, self.file_path]
        elif file_type == FileType.ImageType:
            self._cmdline = [IMGTOTEXT_PATH, self.file_path, 'stdout', '-l', 'chi_sim']
        elif file_type == FileType.CadType:
            if OSUtils.is_windows():
                self._cmdline = [DWGTOTEXT_PATH, "-h", "-x", ".*?",  self.file_path]
            else:
                self._cmdline = [DWGTOTEXT_PATH, "-h", "-x", ".*?",  self.file_path]
        else:
            raise UnsupportedFileType(self.file_path)
        return self._cmdline

    @property
    def filename(self) -> str:
        return path.basename(self.file_path)

    @property
    def file_size(self):
        return path.getsize(self.file_path)

    def cmd_executor(self, timeout_seconds:int) -> str:
        file_type = get_file_type(self.file_path)
        if file_type == FileType.TextType:
            with open(self.file_path, "rb") as f:
                output_bytes = f.read()
        else:
            cmd = self.generate_cmd()
            if OSUtils.is_windows():
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, **subprocess_args(False))
            else:
                env_ = None
                if OSUtils.is_linux():
                    if self.file_type == FileType.CadType:
                        dwg_dir = path.dirname(DWGTOTEXT_PATH)
                        env_ = {
                            "LD_LIBRARY_PATH": dwg_dir,
                        }
                    elif self.file_type == FileType.ImageType:
                        img_dir = path.dirname(IMGTOTEXT_PATH)
                        env_ = {
                            'TESSDATA_PREFIX': DirectoryConfig.OCR_DATA_DIR,
                            "LD_LIBRARY_PATH": img_dir,
                        }
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env_)
            try:
                output_bytes = p.communicate(timeout=timeout_seconds)[0]
            except subprocess.TimeoutExpired:
                logger.warning("timeout {} seconds for {}".format(timeout_seconds, ' '.join(self._cmdline)))
                p.kill()
                output_bytes = b''
        txt = force_decode(output_bytes)
        return txt

    @property
    def file_text(self) -> str:
        # do not repeat convert file
        if self._txt_buff is None:
            if ScanConfig.IsStatisticTime:
                begin_time = time()
            # img files need more time to parse
            if self.file_type == FileType.ImageType:
                timeout_seconds = 60
            else:
                timeout_seconds = PARSER_TIMEOUT_SECONDS
            try:
                self._txt_buff = self.cmd_executor(timeout_seconds)
            except Exception as ex:
                logger.warning("failed execute {}".format(self._cmdline), exc_info=ex)
                self._txt_buff = ""
                return ""
            if ScanConfig.IsStatisticTime:
                end_time = time()
                cost_time = (end_time - begin_time) * 1000
                GlobalVariables.record_convert_ms(cost_time)
            if self._txt_buff is None:
                raise ValueError(self.file_path)
            self.text_len = len(self._txt_buff)
        return self._txt_buff

