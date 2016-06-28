#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs import db
from libs import base_conf
from libs.log import Log

logger = Log("./logs/recommend").instance()

def run():
    conf = base_conf.get_conf(["./conf/recommend.ini"])
    logger.info(conf)
    db_conf = db.get_db_pool(base_conf.get_conf(base_conf.get_conf([conf.db_ins])), dict_cursor = True)
    print db_conf

if __name__ == "__main__":
    run()
