#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

class KeywordsGetter(object):
    def __init__(self, writer, conf, logger, segger, parser):
        self.writer = writer
        self.conf = conf
        self.logger = logger
        self.segger = segger
        self.parser = parser

    '''
        item.get("number"),
        item.get("name"),
        item.get("portrait"),
        item.get("price"),
        item.get("introduce"),
        item.get("label_ids"),
        item.get("subject_id"),
        item.get("new_subject_id"),
        item.get("detail")
    '''

    def get(self):
        if not os.path.isfile(self.conf.video_course):
            return False
        print self.conf.video_course
        try:
            for line in open(self.conf.video_course, "rb"):
                if self.parser.parse(line.strip("\n")):
                    print self.parser.number
                    #  self.parser.number, self.parser.name, self.parser.introduce, self.parser.label_ids, self.parser.new_subject_id, self.parser.detail

            return True
        except Exception as info:
            print info
            return False
