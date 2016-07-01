#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import db
from libs import base_conf
from libs import base_parser
from libs import log
from data import get_data
from data import get_keywords
from data import get_tfidf
from libs import writer
from segment import seg

logger = log.Log("./logs/recommend").instance()

def get_writer(conf):
    writer_nodes = {}
    writer_nodes["video_course"] = writer.WriterNode(conf.video_course, writer.WriterMode.append_binary, bak = True)
    writer_nodes["video_course_keywords"] = writer.WriterNode(conf.video_course_keywords, writer.WriterMode.append_binary, bak = True)
    writer_nodes["video_course_tfidf"] = writer.WriterNode(conf.video_course_tfidf, writer.WriterMode.append_binary, bak = True)
    return writer.Writer(writer_nodes)

def run():
    conf = base_conf.get_conf(["./conf/recommend.ini"])
    logger.info(conf)

    writer = get_writer(conf)

    # 从数据库获得视频课
    db_pool = db.get_db_pool(base_conf.get_conf([conf.db_ins]))
    video_course = get_data.VideoCourseGetter(
        db_pool,
        writer,
        logger
    )
    video_course.get()
    writer.close_key("video_course")

    # 将视频课处理成doc_id => term,term,term
    segger = seg.SegGetter(conf.stop_words, conf.user_dict)
    parser = base_parser.base_parser_t([
                                        "number", "name", "portrait", "price", "introduce",
                                        "label_ids", "subject_id", "new_subject_id", "detail",
                                        ],
                                        sep = "\x01"
                                        )
    keywords = get_keywords.KeywordsGetter(
        writer,
        conf,
        logger,
        segger,
        parser
    )
    keywords.get()
    writer.close_key("video_course_keywords")

    # 计算tfidf 不过这种方法依赖于课程本身
    tfidf = get_tfidf.TfIdf(conf.video_course_keywords, writer)
    tfidf.get()

    writer.close()

if __name__ == "__main__":
    run()
