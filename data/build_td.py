#!/usr/bin/env python

class TermDocBuilder(object):
    def __init__(self, data, max_term = False):
        self.data = data
        self.max_term = max_term

    def build(self):
        ret = {}
        for line in open(self.data, "rb"):
            doc_id, tfidf = line.strip("\n").split("\x01")
            tfidfs = tfidf.split(",")
            if self.max_term:
                tfidfs = tfidfs[:self.max_term]
            for termweight in tfidfs:
                term, weight = termweight.split(":")
                term = term.decode("utf-8")
                if term not in ret:
                    ret[term] = []
                ret[term].append((doc_id, float(weight)))
        return ret
