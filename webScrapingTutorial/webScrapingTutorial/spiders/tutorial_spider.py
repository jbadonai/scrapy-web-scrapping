import scrapy
from ..items import WebscrapingtutorialItem

# 'https://www.thewineshops.com/wine',
class TutorialSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [

        'https://www.thewineshops.com/wine'
    ]



    def parse(self, response, **kwargs):
       try:
        all = response.xpath("//div[@class='product-item-info']").xpath("//a").xpath("@data-gtm-event").extract()
       except Exception as e:
           print(f">><<<>>><<>> {e}")
       print(">>>>>>", len(all))
       for index, a in enumerate(all):
           print()
           print(index + 1,".")
           a = a.replace('false', "False")

           data = eval(a)["ecommerce"]["click"]["products"][0]
           pName = data['name']
           if str(pName).lower().__contains__("ml"):
               temp = str(pName).split(" ")
               vol = temp[-1]
               pVol = vol
           else:
               pVol = None
           pPrice = data['price']
           pCategory = data['category']

           items = WebscrapingtutorialItem()
           items['pName'] = pName
           items['pVol'] = pVol
           items['pPrice'] = pPrice
           items['pCategory'] = pCategory

           # print(f" items: {items}")
           yield items
