from sys import argv, exit, version_info
from network.update_thread import check_update_wrapper

if len(argv) == 2 and argv[1] == '--check-update':
    check_update_wrapper()
    exit(0)

import signal
from os.path import expanduser
from threading import Thread
from conf import PROCESS_NAME
from loginconfig import LoginConfig
from network.update_thread import is_started_by_upgrade
from gui.control.ui_controller import wakeup_login_window
from gui.run import start_default_window, start_main_window
from directory_config import DirectoryConfig
from os import getpid

from sentry_helper import init_sentry
from upgrade_actions.manage_upgrade import perform_upgrade
from utils.system_utils import OSUtils

major, minor = version_info[:2]
if not (major >= 3 and minor >= 4):
    print('Python %d.%d is not supported.\nYou should run this program with python >= 3.4' % (major, minor))
    exit(1)

from os import path
from utils.log_utils import logger, enable_debug
from scanner.scanner_manage import ScannerManager
from optparse import OptionParser
from global_variables import GlobalVariables, set_notify
from multiprocessing import cpu_count
from app_config import AppMetaInfo, StrategyConfig



def parse_startup_arguments():
    startup_cmdline = ' '.join(argv)

    parser = OptionParser()
    parser.add_option('-V', '--version', action='store_true', help='show client version')
    parser.add_option('-N', '--no-gui', action='store_true', help='run in background')
    parser.add_option('-D', '--debug', action='store_true', help='debug mode show more logs')
    parser.add_option('-S', '--scan-dir', dest='scan_dir', help='determine which path to scan')
    parser.add_option('-P', '--process-num', dest='process_num', type=int,
                      help='set processes number to analyzing files, default set it to cpu cores number')
    parser.add_option('-X', '--suffix', dest='suffix', help='scan specific suffix files only like *.docx')
    parser.add_option('--auto-start', action='store_true')
    args, values = parser.parse_args()
    no_gui = args.no_gui
    process_num = args.process_num
    suffix = args.suffix
    debug = args.debug
    scan_dir = args.scan_dir
    is_auto_start = False if args.auto_start is None else True

    if args.version:
        print("version is", AppMetaInfo.version)
        exit(0)
    if process_num is None:
        GlobalVariables.concurrent_process_count = cpu_count()
    else:
        if process_num < 1:
            process_num = 1
        elif process_num > cpu_count():
            process_num = cpu_count()
        GlobalVariables.concurrent_process_count = process_num

    if suffix is not None:
        suffix = suffix.replace('*', '')
        if not suffix.startswith('.'):
            suffix = '.' + suffix
        if suffix not in StrategyConfig.supported_files_suffix:
            logger.error('un-support suffix [%s]' % suffix)
            exit(1)
        else:
            StrategyConfig.supported_files_suffix = [suffix]

    if scan_dir is not None:
        scan_dir = expanduser(scan_dir)
        GlobalVariables.scanning_root = [scan_dir]
    if debug:
        enable_debug()
        logger.debug('debug mode is on')
    return no_gui, is_auto_start, scan_dir


def sigint_handler(*args):
    exit(0)


def main():
    # FIXME: when multiprocess running also invoke this logical
    if False and has_other_instance():
        logger.info('wake up exists instance {}'.format(argv))
        wakeup_login_window()
        exit(0)
    app_version = AppMetaInfo.version
    commit = AppMetaInfo.commit
    logger.info(f"client start {app_version}-{commit}")
    config = LoginConfig()
    if config.load_config() and config.is_public_server():
        init_sentry(app_version, commit, config.username, config.host)
    # https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing
    import multiprocessing
    multiprocessing.freeze_support()
    install_thread_excepthook()

    if is_started_by_upgrade():
        perform_upgrade()
        logger.info('upgrade successfully to ' + app_version)
        set_notify("升级到" + app_version, "自动升级完成")
        StrategyConfig.reset_update_count()
    cmd_mode, auto_start, scan_dir = parse_startup_arguments()
    if cmd_mode:
        logger.info('run in cmd mode')
        sm = ScannerManager([scan_dir], save_path=path.join(DirectoryConfig.TMP_DIR, 'scan-result.txt'))
        sm.start()
    else:
        GlobalVariables.is_auto_start = auto_start
        start_default_window()


def has_other_instance():
    if OSUtils.is_windows():
        import win32event, win32api, winerror
        # AU-132 hold the global mutex or python's GC will release it
        # and new instance can not detect this global mutex
        GlobalVariables.mutex = win32event.CreateMutex(None, 1, PROCESS_NAME)
        lastErrorCode = win32api.GetLastError()
        return lastErrorCode == winerror.ERROR_ALREADY_EXISTS
    elif OSUtils.is_linux():
        pid_file = DirectoryConfig.PID_FILE
        need_refresh = False
        if path.exists(pid_file):
            exists_pid = open(pid_file).read()
            cmdline = '/proc/{}/cmdline'.format(exists_pid)
            if path.exists(cmdline):
                line = open(cmdline).read()
                if line.find('audit') > 0:
                    return True
            else:
                need_refresh = True
        else:
            need_refresh = True
        if need_refresh:
            current_pid = str(getpid())
            with open(pid_file, 'w') as fp:
                fp.write(current_pid)
    elif OSUtils.is_macos():
        return False
    else:
        raise NotImplementedError(OSUtils.get_arch_name())
    return False


def install_thread_excepthook():
    """
    Workaround for sys.excepthook thread bug
    (https://sourceforge.net/tracker/?func=detail&atid=105470&aid=1230540&group_id=5470).
    Call once from __main__ before creating any threads.
    If using psyco, call psycho.cannotcompile(threading.Thread.run)
    since this replaces a new-style class method.
    """
    import sys
    run_old = Thread.run
    def run(*args, **kwargs):
        try:
            run_old(*args, **kwargs)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            # TODO: add sentry here to statistic unhandled errors
            logger.error("Uncaught Exception:", exc_info=sys.exc_info())
            sys.exit(1)

    Thread.run = run


if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    if not OSUtils.is_windows() and AppMetaInfo.is_cn_test():
        start_main_window()
    main()

