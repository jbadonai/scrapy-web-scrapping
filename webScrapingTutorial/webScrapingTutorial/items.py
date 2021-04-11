# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapingtutorialItem(scrapy.Item):
    # define the fields for your item here like:
    pName = scrapy.Field()
    pVol = scrapy.Field()
    pPrice = scrapy.Field()
    pCategory = scrapy.Field()
    pass


class DictionaryItem(scrapy.Item):
    # define the fields for your item here like:
    word = scrapy.Field()
    partOfSpeech = scrapy.Field()
    pronunciation = scrapy.Field()
    definitions = scrapy.Field()

    pass


class JumiaItem(scrapy.Item):
    phoneName = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()


class BibleGatewayItem(scrapy.Item):
    book = scrapy.Field()
    chapter = scrapy.Field()
    verses = scrapy.Field()
