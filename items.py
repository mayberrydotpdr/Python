# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Primary fields
    product_title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    product_code = scrapy.Field()
    image_urls = scrapy.Field()
    # Calculated fields
    images = scrapy.Field()
    location = scrapy.Field()
    # Housekeeping fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
    pass