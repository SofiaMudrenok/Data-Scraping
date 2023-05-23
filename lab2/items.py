# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab2Item(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    pass

class News(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

class Item(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()