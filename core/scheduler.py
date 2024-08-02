import threading
import time


class Scheduler:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.thread = threading.Thread(target=self.run)
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            self.function(*self.args, **self.kwargs)
            time.sleep(self.interval)

    def start(self):
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        self.thread.join()
