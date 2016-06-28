#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import tools

class VideoCourseGetter(object):

    def __init__(self, db, writer, logger):
        self.db_ins = db
        self.writer = writer
        self.logger = logger

    def get(self):
        sql = "SELECT * FROM cdb.`video_course` WHERE `status` = 1"
        self.db_ins.execute(sql)
        self.logger.info("sql = [%s]" % sql)
        count = 0
        while True:
            item = self.db_ins.next()
            if not item:
                break
            values = [
                item.get("number"),
                item.get("name"),
                item.get("portrait"),
                item.get("price"),
                item.get("introduce"),
                item.get("label_ids"),
                item.get("subject_id"),
                item.get("new_subject_id"),
                item.get("detail")
            ]
            self.writer.write("video_course", tools.formatter(values, c = "\x01") + "\n")
            count += 1
        self.logger.info("video_course count [%s]" % count)
        self.writer.close()
