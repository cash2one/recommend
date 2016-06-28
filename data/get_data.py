#!/usr/bin/env python
#-*- coding:utf-8 -*-

class VideoCourseGetter(object):

    def __init__(self, db, conf):
        self.db_ins = db
        self.config = conf

    def get(self):
        self.db_ins.execute("SELECT * FROM `cdb.video_course` WHERE `status` = 1")
        for item in self.db_ins.next_all():
            print item
