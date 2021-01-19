import logging
from logging import handlers


class LogGer:
    def __init__(self, logfile):
        self.logger = logging.getLogger("logs1.log")
        self.logger.setLevel("INFO")
        self.logfile = logfile

    def log_fun(self, msg_data):
        """
        记录日志
        :return:
        """
        file_fmt = logging.Formatter("[%(asctime)s] [%(module)s] [%(funcName)s] [%(levelname)s] %(message)s")
        file_handler = logging.FileHandler(filename=self.logfile, mode="a", encoding="utf-8")
        file_handler.setFormatter(file_fmt)
        console_fmt = logging.Formatter("[%(asctime)s] [%(levelname)s]")
        sl = logging.StreamHandler()
        sl.setFormatter(console_fmt)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(sl)
        self.logger.info(msg_data)
        # 在记录日志之后移除句柄,不添加这两行代码日志会记录重复
        self.logger.removeHandler(sl)
        self.logger.removeHandler(file_handler)

