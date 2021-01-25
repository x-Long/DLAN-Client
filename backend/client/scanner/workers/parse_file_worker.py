from time import sleep

from utils.log_utils import get_logger
from conf import WorkerNames, PROCESS_LOCK_SLEEP_SECONDS
from queue import Empty
from multiprocessing import Process, Event
from scanner.find_keywords import find_keyword_from_file
from utils.system_utils import OSUtils

logger = get_logger('parse-file')


class ParserProcess(Process):
    def __init__(self, name, task_queue, output_queue, task_done_event):
        Process.__init__(self, name=name)
        self.task_queue = task_queue
        self.output_queue = output_queue
        self.task_finished_event = task_done_event
        self.keep_running = True
        self.paused_event = Event()
        self.task_stop_event = Event()
        self.paused_event.set()
        # exit parser process when main client exit
        self.daemon = True

    def run(self):
        count = 0
        while True:
            if self.task_stop_event.is_set():
                break
            self.paused_event.wait()
            try:
                file_path = self.task_queue.get(block=False)
            except Empty:
                sleep(PROCESS_LOCK_SLEEP_SECONDS)
                if self.task_finished_event.is_set() and self.task_queue.empty():
                    break
            else:
                count += 1
                try:
                    print("analyzing", file_path)
                    report_event = find_keyword_from_file(file_path)
                    if report_event is not None:
                        print("analyzed {}".format(file_path))
                        self.output_queue.put(report_event)
                except FileNotFoundError as ex:
                    logger.exception("can not found %s" % file_path, exc_info=ex)
        print("{} finished".format(self.name))

    def pause(self):
        self.paused_event.clear()
        logger.debug('%s paused' % self.name)

    def resume(self):
        self.paused_event.set()
        logger.debug('%s resume' % self.name)

    def stop(self):
        self.task_stop_event.set()

def start_parser_processes(file_path_queue, output_queue):
    process_count = OSUtils.get_working_cpu_count()
    logger.info('creating %d processes to analyzing files' % process_count)
    process_info_list = []

    # create parser processes
    for i in range(1, process_count+1):
        task_finished_event = Event()
        process_name = '{}-{}'.format(WorkerNames.PARSER_WORKER_NAME, i)
        parser_process = ParserProcess(process_name, file_path_queue, output_queue, task_finished_event)
        parser_process.start()
        process_info_list.append([process_name, parser_process, task_finished_event])
    return process_info_list
