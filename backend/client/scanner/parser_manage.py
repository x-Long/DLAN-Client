from scanner.workers.parse_file_worker import start_parser_processes
from utils.log_utils import logger
from scanner.workers.collect_result_worker import CollectResultThread


class ParserManage:
    def __init__(self, file_path_queue, save_path, output_queue):
        self.file_path_queue = file_path_queue
        self.output_queue = output_queue
        self.process_info_list = None
        self.save_path = save_path
        self.saving_file = (save_path is not None)

        if self.saving_file:
            self.collect_result_thread = CollectResultThread(self.output_queue, self.save_path)
        else:
            logger.info('skip saving result to file')

    def pause(self):
        for process_name, process, task_finished_event in self.process_info_list:
            process.pause()

    def resume(self):
        for process_name, process, task_finished_event in self.process_info_list:
            process.resume()

    def stop(self):
        for process_name, process, task_finished_event in self.process_info_list:
            process.stop()

    def start(self):
        self.process_info_list = start_parser_processes(self.file_path_queue, self.output_queue)
        if self.saving_file:
            logger.debug('starting collect result worker')
            self.collect_result_thread.start()

    def notify_finished(self):
        for process_name, process, task_finished_event in self.process_info_list:
            logger.info('notifying %s finished' % process_name)
            task_finished_event.set()
            process.join()
        if self.saving_file:
            self.collect_result_thread.notify_finished()
            self.collect_result_thread.join()
