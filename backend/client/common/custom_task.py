from threading import Event, Thread
from utils.log_utils import logger

# https://stackoverflow.com/questions/3262346/pausing-a-thread-using-threading-class
class PauseAbleThread(Thread):
    def __init__(self):
        self.keep_running = True
        self.is_finished = False
        super().__init__()
        self.pause_event = Event()
        self.pause_event.set()

    def check_paused(self):
        self.pause_event.wait()

    def pause(self):
        self.pause_event.clear()
        logger.info('paused')

    def resume(self):
        self.pause_event.set()
        logger.info('resumed')

    def stop(self):
        self.pause_event.set()
        self.keep_running = False
        logger.info('stopped')
