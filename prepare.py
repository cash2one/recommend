#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import db
from libs import base_conf
from libs import log
from data import get_data
from libs import writer
from segment import seg

logger = log.Log("./logs/recommend").instance()

def get_writer(conf):
    writer_nodes = {}
    writer_nodes["video_course"] = writer.WriterNode(conf.video_course, writer.WriterMode.append_binary, bak = True)
    writer_nodes["video_course_keywords"] = writer.WriterNode(conf.video_course_keywords, writer.WriterMode.append_binary, bak = True)
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

    segger = seg.SegGetter(conf.stop_words, conf.user_dict)
    parser = base_parser.base_parser_t([
                                        "number", "name", "portrait", "price", "introduce",
                                        "label_ids", "subject_id", "new_subject_id", "detail",
                                        ],
                                        sep = "\x01"
                                        )
    keywords = get_data.KeywordsGetter(
        writer,
        conf,
        logger,
        segger,
        parser
    )
    keywords.get()


if __name__ == "__main__":
    run()
