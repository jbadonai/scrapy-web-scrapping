import scrapy
from ..items import DictionaryItem
# from webScrapingTutorial.webScrapingTutorial.items import DictionaryItem

import  time
import subprocess
'''
RESOURCES:
=========
https://pypi.org/project/scrapy-user-agents/
https://github.com/rejoiceinhope/scrapy-proxy-pool
'''

class DictionarySpider(scrapy.Spider):
    def __init__(self):
        self.page = 1
        self.currentWord = ""
        self.currentPronunciation = ""
        self.currentPartOfSpeech = ""
        self.currentDefinitions = ""

    name = 'dictionary'
    start_urls = [

            'https://www.dictionary.com/list/w/1',

    ]

    def list2str(self, list):
        ans = ""
        for l in list:
            ans += f"{l}"

        return ans

    def isInternet(self):
        result = subprocess.getoutput('ping www.google.com -n 1')
        if str(result).lower().__contains__('ttl='):
            return True
        else:
            return False


    def parse(self, response, **kwargs):
        data = response.css('.css-aw8l3w')
        wordListURL = data.css('a::attr(href)').extract()
        wordList = data.css('a::text').extract()

        next_page_url = response.css('.e1wvt9ur5 a::attr(href)').get()
        # print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   next page url: {next_page_url}")

        # loop through the word list on current page to extract definition

        for url in wordListURL:
            print(f"working on url: {url}")
            yield response.follow(url, callback=self.extract_definition)


        # go to next page
        if next_page_url is not None:
            self.page += 1
            yield response.follow(next_page_url, callback=self.parse)


    def extract_definition(self, response):
        # all section of different definition
        alldata = response.css('#collins-section+ .e16867sm0 , #luna-section+ .e16867sm0 , .ej3iuhp0+ .e16867sm0')
        all_definitions = []
        # for each section [word, pronunciation, part of speech, list of definition.]
        for data in alldata:
            # word
            word = data.css('.e1wg9v5m4::text').extract()
            word = self.list2str(word)

            # pronounciation
            pro = data.css('.evh0tcl2::text, .small-caps::text, .pron::text, .bold::text, .label::text').extract()
            pro = self.list2str(pro)

            # Part of speech
            pos_main = data.css('.e1hk9ate1')
            pos1 = pos_main.css('.luna-pos::text').extract()
            pos1 = self.list2str(pos1)
            pos2 = pos_main.css('.e1hk9ate3::text , .pron-spell::text , .bold::text').extract()
            pos2 = self.list2str(pos2)
            pos = f"{pos1} {pos2}"

            # Definition
            defn_list = data.css('.e1q3nk1v3')
            defn = ""
            for index, d in enumerate(defn_list):
                this_defn = d.css('.e1q3nk1v4::text, .e1w1pzze1::text , .status::text , .css-1ghs5zt .italic:nth-child(2)::text , .italic:nth-child(1)::text , .e1q3nk1v4::text , .e1q3nk1v4 .italic::text , .luna-xref::text , .xref::text, .tx::text, .kw::text, .e1w1pzze1::text').extract()
                this_defn = self.list2str(this_defn)

                this_example = d.css('.luna-example::text').extract()
                this_example = self.list2str(this_example)

                if this_example != "":
                    defn += f"{index + 1}. {this_defn} \n\t\t{this_example}\n\t"
                else:
                    defn += f"{index + 1}. {this_defn}\n\t"

            all_definitions.append(defn)


            self.currentWord = word
            self.currentPartOfSpeech = pos
            self.currentPronunciation = pro
            self.currentDefinitions = defn

            items = DictionaryItem()

            items['word'] = self.currentWord
            items['pronunciation'] = self.currentPronunciation
            items['partOfSpeech'] = self.currentPartOfSpeech
            items['definitions'] = self.currentDefinitions

            yield items


