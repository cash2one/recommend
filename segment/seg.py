#!/usr/bin/env python
#-*- coding:utf-8 -*-
import jieba
import os

class SegGetter(object):
    def __init__(self, stop_words = False, user_dict = False):
        if user_dict:
            jieba.load_userdict(user_dict)
        self.stop_words = self.load_stop_words(stop_words)

    def load_stop_words(self, stop_words):
        ret = {}
        if not stop_words:
            return ret
        try:
            if os.path.isfile(stop_words):
                sw = open(stop_words, "rb")
                for line in sw:
                    word = line.strip()
                    if not word:
                        continue
                    ret[word.decode("utf-8")] = True
            return ret
        except:
            return ret

    # 分词
    def seg(self, query):
        words = jieba.cut(query, cut_all = True)
        ret = []
        for word in words:
            word = word
            if len(word) < 2:
                continue
            if word in self.stop_words:
                continue
            ret.append(word)
        tf = {}
        for word in ret:
            tf[word] = tf.get(word, 0) + 1
        result = {
            "ori": ret,
            "tf": tf
        }
        return result

if __name__ == "__main__":
    sg = SegGetter("./stopwords.txt", user_dict = "./userdict.txt")
    print " ".join(sg.seg(u"雅思机经真题，").get("tf"))
    print " ".join(sg.seg(u"2016年6月18日雅思机经[听力]_雅思_机经_听力_雅思新闻_雅思机经_跟谁学雅思官网").get("tf"))
    # print " ".join(sg.seg("我是一个中国人，"))
    # print " ".join(sg.seg("我是一个中国人，"))
