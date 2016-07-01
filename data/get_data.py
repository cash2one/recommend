#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import tools
import re

class VideoCourseGetter(object):

    def __init__(self, db, writer, logger):
        self.db_ins = db
        self.writer = writer
        self.logger = logger

    def get(self):
        sql = "SELECT * FROM cdb.`video_course` WHERE `status` = 1"
        self.db_ins.execute(sql, print_sql = False)
        self.logger.info("sql = [%s]" % sql)
        count = 0
        while True:
            item = self.db_ins.next()
            if not item:
                break
            # 如果标题小于五个字，介绍小于20个字直接当作垃圾课程去掉
            if len(item.get("name")) < 6 or len(item.get("introduce")) < 21:
                continue
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
            course_item = re.sub(r"\n", " ", tools.formatter(values, c = "\x01"))
            self.writer.write("video_course", course_item + "\n")
            count += 1
        self.logger.info("video_course count [%s]" % count)
