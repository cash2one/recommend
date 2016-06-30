#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import base_conf
from libs import log
from data import build_td
from data import query
from segment import seg
import time

logger = log.Log("./logs/server").instance()

def run():
    conf = base_conf.get_conf(["./conf/server.ini"])
    logger.info(conf)

    # build term->doc
    term_doc = build_td.TermDocBuilder(conf.video_course_tfidf, 30)
    term_doc_index = term_doc.build()

    segger = seg.SegGetter(conf.stop_words, conf.user_dict)
    q = query.Query(segger, term_doc_index, {})
    q.get("高考物理牛顿定律")

if __name__ == "__main__":
    run()
