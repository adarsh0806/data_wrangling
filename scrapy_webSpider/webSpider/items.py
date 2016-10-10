# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


# class WebspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class Article(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Each Item object represents a single page on the website. We are collecting the title field from
    # each page.
    title = Field()