# -*- coding: utf-8 -*-
import scrapy
from suning_book.items import SuningBookItem
import re
import time

class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["snbook.suning.com"]
    start_urls = (
        'http://snbook.suning.com/web/trd-fl/100301/46.htm',
    )

    def parse(self, response):
        book_style_list = response.xpath("//li[contains(@class, 'lifirst')]")

        for book_style in book_style_list:
            book = SuningBookItem()
            book['book_sytle'] = book_style.xpath(".//div[@class='second-sort']//a/text()").extract_first()

            url = book_style.xpath("./div[@class='second-sort']/a/@href").extract_first()

            url = 'http://snbook.suning.com' + url
            i = 1
            yield scrapy.Request(
                url,
                callback=self.parse_book_list,
                meta={'book': book, 'page':i}
            )


    def parse_book_list(self, response):
        book = response.meta["book"]
        page = response.meta['page']
        # print("@" * 100)
        # print(book)
        # time.sleep(3)
        detail_url = response.xpath('//div[@class="book-title"]/a/@href').extract()
        next_url = response.xpath('//a[@class="next"]').extract_first()

        for url in detail_url:
            book['book_href'] = url
            # print(book)
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'book': book}
            )

        if next_url:
            page += 1
            print(page)
            next_url = 'http://snbook.suning.com/web/trd-fl/100300/9.htm?pageNumber={}&sort=0'.format(page)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta={'book':book}
            )


    def parse_detail(self, response):
        book = response.meta['book']
        book['book_name'] = response.xpath("//h1/strong/text()").extract_first()
        book['book_orgprice'] = re.findall(r"\"pbPrice\":\'(.*?)\'", response.text)
        book['book_author'] = response.xpath("//div[@class='parm parm-author wauto']/a/text()").extract_first()
        book['book_trueprice'] = re.findall(r"\"bp\":\'(.*?)\'", response.text)
        # print(book)
        yield book