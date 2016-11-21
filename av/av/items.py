# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class FhItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    date = scrapy.Field()
    act = scrapy.Field()


class ActItem(scrapy.Item):
    name = scrapy.Field()
    note = scrapy.Field()
    other = scrapy.Field()
    birth = scrapy.Field()
    date = scrapy.Field()
    sanwei = scrapy.Field()
