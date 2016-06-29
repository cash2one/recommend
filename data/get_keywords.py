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

    def tf_to_string(self, tf):
        return ",".join([":".join([word, tf[word]]) for word in tf])

    def get(self):
        if not os.path.isfile(self.conf.video_course):
            return False
        try:
            for line in open(self.conf.video_course, "rb"):
                if self.parser.parse(line.strip("\n")):
                    tf = self.segger.seg(self.parser.name + self.parser.introduce + self.parser.detail)
                    print self.tf_to_string(tf.get("tf"))
                    #  self.parser.number, self.parser.name, self.parser.introduce, self.parser.label_ids, self.parser.new_subject_id, self.parser.detail

            return True
        except Exception as info:
            return False
