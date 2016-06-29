#!/usr/bin/env python
#-*- coding:utf-8 -*-
import math

class TfIdf(object):

    def __init__(self, data):
        self.data = data
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
            doc_id, terms = line.split("\t")
            if doc_id not in self.TF:
                self.TF[doc_id] = {}
            self.N += 1
            for term in terms.split(","):
                word, freq = term.split(":")
                self.TF[doc_id][term] = int(freq)
                self.DF[word] = self.DF.get(word, 0) + 1
                self.DC[doc_id] = self.DC.get(doc_id, 0) + int(freq)

        self.compute_tfidf()

    def compute_tfidf(self):
        for doc_id in self.TF:
            ret = []
            term_count = self.DC[doc_id]
            for word in self.TF[doc_id]:
                tf = self.tf(self.TF[doc_id][word], term_count)
                idf = self.idf(self.DF[word])
                ret.append("%s:%s" % (word, self.tfidf(tf, idf)))
            print "\t".join(map(str, [doc_id, ",".join(ret)]))
