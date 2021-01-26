# -*-encoding:utf-8-*-

from tasks.remote_tasks.device_info_task import GetDeviceInfoTask
from tasks.remote_tasks.scan_file_task import DiskScanTask
# Notice: do not remove above two imports as they are actually being used

from tasks.task_interface import LocalTaskException, RemoteTask
from decorators import singleton
import json
import base64
import sys
import inspect
from utils.log_utils import logger

class EmptyTaskException(LocalTaskException):
    pass


class UnknownTaskException(LocalTaskException):
    pass


def list_remote_tasks() -> dict:
    """
    https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
    :return:
    """
    m = sys.modules[__name__]
    d = {}
    for name, obj in inspect.getmembers(m):
        if inspect.isclass(obj):
            if obj.__module__.startswith("tasks.remote_tasks."):
                d[name] = obj
    assert len(d) > 0
    return d


@singleton
class TaskName:
    """
    supported remote task are:
        DiskScanTask
        GetDeviceInfoTask
    above tasks are dynamic loaded from tasks/remote_tasks
    """
    def __init__(self):
        self._task_map = list_remote_tasks()
        for i in self._task_map.keys():
            setattr(self, i, i)

    def get_class(self, name) -> RemoteTask:
        return self._task_map.get(name)


def base64_dict(result: dict) -> str:
    if not isinstance(result, dict):
        raise TypeError("require dict object")
    json_str = json.dumps(result)
    b64_device_info = base64.b64encode(json_str.encode())
    s_info = b64_device_info.decode()
    return s_info


@singleton
class RemoteTaskManage:
    def __init__(self):
        self._task_map = {}
        self._result_list = []

    def assign_task(self, task_name, **args):
        clz = TaskName.get_class(task_name)
        task = clz(**args)
        task = self._task_map[task_name] = task
        task.save_task()

    def new_task(self, task_obj: RemoteTask):
        clz_name = type(task_obj).__name__
        task_obj.save_task()
        self._task_map[clz_name] = task_obj


    @property
    def count(self):
        return len(self._all_tasks)

    @property
    def _all_tasks(self):
        task_list = self._task_map.values()
        task_list = list(task_list)
        return task_list

    def has_task(self) -> bool:
        for task in self._all_tasks:
            if task.is_task_exists():
                return True
        return False

    def run_first_task(self):
        """
        do not make any network operation here
        save task output to result queue and let other consumer to handle it
        :return:
        """
        if self.count == 0:
            raise EmptyTaskException()

        for task in self._all_tasks:
            if task.is_task_exists():
                if not task.is_started():
                    if task.is_block():
                        task.run_task()
                        output = task.get_output()
                        encoded_data = base64_dict(output)
                        self._result_list.append(encoded_data)
                    else:
                        task.run_task()
                    # execute one task and break loop
                    break

    def release_first_task(self):
        if self._all_tasks:
            task = self._all_tasks[0]
            if task.is_finished():
                task.close_task()
                self._task_map.pop(task.get_name())

    def check_output(self):
        if self.has_task():
            self.run_first_task()
        if self._result_list:
            result = self._result_list.pop(0)
        else:
            result = None
        self.release_first_task()
        return result


def main():
    RemoteTaskManage.assign_task(TaskName.GetDeviceInfoTask)
    RemoteTaskManage.assign_task(TaskName.DiskScanTask, is_quick=True, filename="full.rlog")
    from time import sleep
    while True:
        s = RemoteTaskManage.check_output()
        if s:
            logger.info("get task output %s", s)
        sleep(1)


if __name__ == '__main__':
    main()