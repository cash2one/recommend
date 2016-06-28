#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import tools

class VideoCourseGetter(object):

    def __init__(self, db, writer, logger):
        self.db_ins = db
        self.writer = writer
        self.logger = logger

    def get(self):
        self.db_ins.execute("SELECT * FROM cdb.`video_course` WHERE `status` = 1")
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
                item.get("detail"),
            ]
            writer.write("video_course", tools.formatter(values) + "\n")
        writer.close()
