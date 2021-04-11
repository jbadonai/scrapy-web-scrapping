import scrapy
from ..items import BibleGatewayItem

class BibleGatwaySpider(scrapy.Spider):
    name = 'bible'
    start_urls = [
        'https://www.biblegateway.com/passage/?search=Genesis%201&version=KJV'
    ]

    def list2str(self, list):
        ans = ""
        for l in list:
            ans += f"{l}"

        return ans

    def parse(self, response, **kwargs):
        title = response.css('.bcv .dropdown-display-text::text').get()

        temp = str(title).split(" ")
        chapter = temp[-1]
        book = temp[:-1]
        book = self.list2str(book)
        print(f"Title: {title}")
        print(f"Book: {book}  Chapter: {chapter}")
        print("======================")

        all_text = response.css('.text-html p')
        verses = ""
        for text in all_text:
            verse = text.css('.chapternum::text, .versenum::text, .small-caps::text, .text::text').extract()
            verse = self.list2str(verse)
            verse = verse.replace("\xa0",". ")

            verses += f'{verse} \n'

        print(f"working on {book}, {chapter}...")
        items = BibleGatewayItem()
        items['book'] = book
        items['chapter'] = chapter
        items['verses'] = verses

        yield  items


        nextChapter = response.css('.next-chapter').css('a::attr(href)').get()
        if nextChapter is not None:
            yield response.follow(nextChapter, self.parse)


