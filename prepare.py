#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import db
from libs import base_conf
from libs.log import Log
from data import get_data

logger = Log("./logs/recommend").instance()

# def get_writer(conf):
#     writer_nodes = {}
#     writer_nodes["kpi_info"] = writer.WriterNode(conf.kpi_info, writer.WriterMode.append_binary, bak = True)
#     writer_nodes["kpi_total"] = writer.WriterNode(conf.kpi_total, writer.WriterMode.append_binary, bak = True)
#     return writer.Writer(writer_nodes)

def run():
    conf = base_conf.get_conf(["./conf/recommend.ini"])
    logger.info(conf)

    db_pool = db.get_db_pool(base_conf.get_conf([conf.db_ins]))
    print db_pool

    video_course = get_data.VideoCourseGetter(db_pool, conf)
    video_course.get()

    # writer = get_writer(conf)

if __name__ == "__main__":
    run()
