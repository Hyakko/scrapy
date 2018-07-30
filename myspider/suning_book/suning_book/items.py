# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_sytle = scrapy.Field()
    book_tags = scrapy.Field()
    book_name = scrapy.Field()
    book_orgprice = scrapy.Field()
    book_trueprice = scrapy.Field()
    book_href = scrapy.Field()
    book_author = scrapy.Field()
    book_img = scrapy.Field()