#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

class Log(object):
    def __init__(self, log_path, level=logging.INFO, when="D", backup=7,
                 format="%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s",
                 datefmt="%m-%d %H:%M:%S"):
        self.log_path = log_path
        self.level = level
        self.when = when
        self.backup = backup
        self.format = format
        self.datefmt = datefmt
        self.init_flag = False

    def instance(self):
        if not self.init_flag:
            self.init_log()
        return logging

    def init_log(self):
        formatter = logging.Formatter(self.format, self.datefmt)
        logger = logging.getLogger()
        logger.setLevel(self.level)

        dir = os.path.dirname(self.log_path)
        if not os.path.isdir(dir):
            os.makedirs(dir)

        handler = logging.handlers.TimedRotatingFileHandler(self.log_path + ".log",
                                                            when=self.when,
                                                            backupCount=self.backup)
        handler.setLevel(self.level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        handler = logging.handlers.TimedRotatingFileHandler(self.log_path + ".log.wf",
                                                            when=self.when,
                                                            backupCount=self.backup)
        handler.setLevel(logging.WARNING)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

# class SMSHandler(logging.StreamHandler):
#     on_same_line = False
#     header = ""
#     def emit(self, record):
#         try:
#             msg = self.format(record)
#             a = sms.send(["15801689885"], "[%s] %s"  %(self.header, msg.replace("<","'").replace(">","'") ) )
#             #mail.send(['yuebin@baijiahulian.com'],"[blazer] fatal[%s]" %msg, "[blazer] %s"  % msg.replace("<","'").replace(">","'") )
#             #print a
#             self.flush()
#
#         except (KeyboardInterrupt, SystemExit):
#             raise
#         except:
#             self.handleError(record)

if __name__ == "__main__":
    L = Log("./log/draw_traffic_line").instance()
    L.info("HelloWorld!!!")
    L.debug("haha")
    L.warning("warning")
    L.fatal("fatal")
