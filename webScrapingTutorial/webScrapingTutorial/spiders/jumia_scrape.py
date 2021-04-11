import scrapy
from ..items import JumiaItem


class PhoneScrape(scrapy.Spider):
    name = 'phone'
    start_urls = {
        'https://www.jumia.com.ng/mobile-phones/',
        'https://www.jumia.com.ng/watches-sunglasses/'
    }

    def parse(self, response, **kwargs):
        # all_data = response.css("._4cl-3cm-shs")
        all_data = response.css(".info")
        for data in all_data:
            price = data.css(".prc::text").extract_first()
            # print(f"price: {price}")

            description = data.css("h3.name::text").extract_first()

            try:
                phone_name = str(description).split(" ")[0]
                # print(f"phone Name: {phone_name}")
            except:
                phone_name = None


            # print(f"Description: {description}")
            if price is not None:

                item = JumiaItem()
                item['phoneName'] = phone_name
                item['price'] = price
                item['description'] = description

                yield item




