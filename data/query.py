#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Query(object):
    def __init__(self, segger, td, doc):
        self.segger = segger
        self.term_doc = td
        self.doc = doc

    def get(self, query):
        if not query:
            return False
        tf = self.segger.seg(query)

        tf = tf.get("tf")
        result = {}
        for term in tf:
            if term not in self.term_doc:
                continue
            for doc in self.term_doc[term]:
                doc_id, tfidf = doc
                if doc_id not in result:
                    result[doc_id] = 0.0
                result[doc_id] += tf[term] * tfidf
        result = sorted(result.iteritems(), key=lambda d:d[1], reverse = True)

        for doc, weight in result:
            print doc, weight
