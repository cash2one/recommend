#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import re

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

    def del_html_tag(self, string):
        return re.sub(r"<[^>]+?>", "", string)

    def tf_to_string(self, tf):
        return ",".join([":".join([word.encode("utf-8"), str(tf[word])]) for word in tf if len(word) <= 6])

    def is_test(self, desc):
        desc = desc.lower()
        if desc.find("test") != -1 or desc.find("测试") != -1:
            return True
        return False

    def get(self):
        if not os.path.isfile(self.conf.video_course):
            return False
        # try:
        for line in open(self.conf.video_course, "rb"):
            if self.parser.parse(line.strip("\n")):
                desc = self.parser.name + self.del_html_tag(self.parser.introduce) + self.del_html_tag(self.parser.detail) + self.parser.label_ids + ",".join(self.parser.subject_id.split(",")[3:])
                if self.is_test(desc):
                    continue
                tf = self.segger.seg(desc)
                self.writer.write("video_course_keywords", self.parser.number + "\x01" + self.tf_to_string(tf.get("tf")) + "\n")
        self.writer.close()
        # return True
        # except Exception as info:
            # return False
