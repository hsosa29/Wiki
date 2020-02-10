# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    ranking=scrapy.Field()
    enlaces=scrapy.Field()
    ruta=scrapy.Field()
    palabras=scrapy.Field()
    pass
   
