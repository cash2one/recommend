#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import db
from libs import base_conf
from libs.log import Log

logger = Log("./logs/recommend").instance()

# def get_writer(conf):
#     writer_nodes = {}
#     writer_nodes["kpi_info"] = writer.WriterNode(conf.kpi_info, writer.WriterMode.append_binary, bak = True)
#     writer_nodes["kpi_total"] = writer.WriterNode(conf.kpi_total, writer.WriterMode.append_binary, bak = True)
#     return writer.Writer(writer_nodes)

def run():
    conf = base_conf.get_conf(["./conf/recommend.ini"])
    logger.info(conf)

    db_conf = db.get_db_pool(base_conf.get_conf([conf.db_ins]), dict_cursor = True)
    print db_conf

    # writer = get_writer(conf)

if __name__ == "__main__":
    run()
