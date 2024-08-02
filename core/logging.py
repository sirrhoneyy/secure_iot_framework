import logging


class Logger:
    def __init__(self, log_file='iot_framework.log'):
        self.logger = logging.getLogger('IoTFrameworkLogger')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)
