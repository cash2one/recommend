#!/usr/bin/env python

class DocBuilder(object):
    def __init__(self, data):
        self.data = data

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

    def build(self):
        ret = {}
        for line in open(self.data, "rb"):
            items = line.strip("\n").split("\x01")
            ret[int(items[0])] = {
                "url": "http://www.genshuixue.com/video_course/getcourseshowdetail?number=%s" % items[0],
                "name": items[1].decode("utf-8"),
                "portrait": items[2],
                "price": items[3],
                "introduce": items[4].decode("utf-8"),
            }
        return ret
