# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class SuningBookPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        self.collection = client['ribai']['book']

    def process_item(self, book, spider):
        self.collection.insert(dict(book))
