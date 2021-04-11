import scrapy
from ..items import DictionaryItem

class DictionaryExtractor(scrapy.Spider):
    name = "olddictionary"
    start_urls = {
        'https://www.dictionary.com/list/a/2'
    }

    def parse(self, response, **kwargs):
        all = response.css(".css-aw8l3w::text").extract()
        items = DictionaryItem()
        items['wordList'] = all
        yield items
