# -*-encoding:utf-8-*-
from abc import ABC
from os import path, remove
from directory_config import DirectoryConfig
from utils.log_utils import logger
from utils.time_utils import get_formatted_time


class LocalTaskException(Exception):
    pass


class TaskNotExists(LocalTaskException):
    """
    throw this exception when start a task but task not exists
    """
    pass


class TaskIsRunning(LocalTaskException):
    """
    throw this exception when start a task but task not exists
    """
    pass


class RemoteTask:
    def __init__(self):
        self._task_dir = DirectoryConfig.TASK_DIR
        filename = "{}.task".format(self.get_name())
        self._flag_file = path.join(self._task_dir, filename)
        self._is_finished = False
        self._is_started = False
        self._output = None

    def run(self):
        raise NotImplementedError()

    def is_block(self) -> bool:
        """
        if task execute very fast(within 3 seconds) we start task and wait for output
        :return:
        """
        raise NotImplementedError()

    def run_task(self):
        """
        you should always check `self.is_task_exists` before execute this method
        repeat run same task cause exception: TaskIsRunning
        :raise
            TaskNotExists() when task not exists
            TaskIsRunning() when task is running
        :return:
        """
        self.raise_if_repeat_run()
        self.set_started()
        logger.info("start {}".format(self.get_name()))
        self.run()
        if self.is_block():
            self.set_finished()

    def get_name(self) -> str:
        return self.__class__.__name__

    def set_started(self):
        self._is_started = True

    def is_started(self) -> bool:
        return self._is_started

    def set_finished(self):
        logger.info("set %s finished", self.get_name())
        self._is_finished = True

    def is_finished(self):
        return self._is_finished

    def raise_if_repeat_run(self):
        if not self.is_task_exists():
            raise TaskNotExists()
        if self._is_started:
            raise TaskIsRunning()

    def set_output(self, data):
        self._output = data

    def get_output(self):
        return self._output

    def is_task_exists(self):
        return path.exists(self._flag_file)

    def save_task(self):
        with open(self._flag_file, 'w') as fp:
            current_time = get_formatted_time()
            fp.write(current_time)
        logger.info("create %s", self.get_name())

    def close_task(self):
        if path.isfile(self._flag_file):
            # HELP: it is very wired that client call this method when login finished
            remove(self._flag_file)
            logger.info("remove %s", self.get_name())


class BlockedRemoteTask(RemoteTask, ABC):
    def is_block(self) -> bool:
        return True


class NoneBlockRemoteTask(RemoteTask, ABC):
    def is_block(self) -> bool:
        return False
