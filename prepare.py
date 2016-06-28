#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import db
from libs import base_conf
from libs import log
from data import get_data
from libs import writer

logger = log.Log("./logs/recommend").instance()

def get_writer(conf):
    writer_nodes = {}
    writer_nodes["video_course"] = writer.WriterNode(conf.video_course, writer.WriterMode.append_binary, bak = True)
    return writer.Writer(writer_nodes)

def run():
    conf = base_conf.get_conf(["./conf/recommend.ini"])
    logger.info(conf)

    writer = get_writer(conf)

    db_pool = db.get_db_pool(base_conf.get_conf([conf.db_ins]))
    video_course = get_data.VideoCourseGetter(
        db_pool,
        writer,
        logger
    )
    video_course.get()

if __name__ == "__main__":
    run()
