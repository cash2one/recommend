#!/usr/bin/env python
#-*- coding:utf-8 -*-
import math

class TfIdf(object):

    def __init__(self, data, writer):
        self.data = data
        self.writer = writer
        self.N = 0
        self.DF = {}
        self.TF = {}
        self.DC = {}

    def tf(self, freq, count):
        return round(float(freq) / count, 5)

    def idf(self, df):
        return round(1 + math.log(self.N / (1 + df)), 5)

    def tfidf(self, tf, idf):
        return round(tf * idf, 5)

    def get(self):
        for line in open(self.data, "rb"):
            line = line.strip("\n")
            doc_id, terms = line.split("\x01")
            if doc_id not in self.TF:
                self.TF[doc_id] = {}
            self.N += 1
            for term in terms.split(","):
                if not term.strip():
                    continue
                print doc_id, term
                word, freq = term.split(":", 1)
                self.TF[doc_id][word] = int(freq)
                self.DF[word] = self.DF.get(word, 0) + 1
                self.DC[doc_id] = self.DC.get(doc_id, 0) + int(freq)

        self.compute_tfidf()

    def compute_tfidf(self):
        words = {}
        for doc_id in self.TF:
            ret = {}
            if doc_id not in self.DC:
                continue
            term_count = self.DC[doc_id]
            for word in self.TF[doc_id]:
                tf = self.tf(self.TF[doc_id][word], term_count)
                idf = self.idf(self.DF[word])
                ret[word] = self.tfidf(tf, idf)
            ret = sorted(ret.iteritems(), key=lambda d:d[1], reverse = True)
            ret = ",".join([":".join([_word, str(_tfidf)]) for _word, _tfidf in ret])
            self.writer.write("video_course_tfidf", doc_id + "\x01" + ret + "\n")
