import threading
from os import rename, path, remove
from time import sleep
from utils.log_utils import logger
from queue import Empty
from conf import WorkerNames, UTF8_ENCODING, PROCESS_LOCK_SLEEP_SECONDS
from global_variables import GlobalVariables


class CollectResultThread(threading.Thread):
    def __init__(self, output_queue, save_path):
        threading.Thread.__init__(self, name=WorkerNames.COLLECTOR_WORKER_NAME)
        self.output_queue = output_queue
        self.scan_finished_event = threading.Event()
        self.save_path = save_path
        self.tmp_path = self.save_path + '.tmp'
        self.fp = None

    def run(self):
        self.fp = open(self.tmp_path, 'w', encoding=UTF8_ENCODING)
        matched_keywords_count = 0
        while not self.scan_finished_event.is_set() or not self.output_queue.empty():
            try:
                sleep(PROCESS_LOCK_SLEEP_SECONDS)
                scan_result = self.output_queue.get(block=False, timeout=1)
            except Empty:
                sleep(PROCESS_LOCK_SLEEP_SECONDS)
            else:
                matched_keywords_count += 1
                logger.debug("collect %s" % scan_result.to_text())
                self.fp.write(scan_result.to_text() + '\n')

        self.fp.close()
        if path.exists(self.save_path):
            remove(self.save_path)
        rename(self.tmp_path, self.save_path)
        GlobalVariables.matched_keywords_count = matched_keywords_count
        logger.info('%s finished get %d results' % (self.getName(), matched_keywords_count))

    def notify_finished(self):
        self.scan_finished_event.set()
