from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lab2.items import *
from bs4 import BeautifulSoup

class LnuSpider(scrapy.Spider):
    name = "lnu_db"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/about/faculties/"]
    rules = [Rule(LinkExtractor(allow='^.*(faculty-)([a-z])*$'), callback='parse', follow=True)]


    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        img = soup.find("div",class_="thumb").find("a").img["src"]
        
        yield {
            'image_urls': [img]
        }


        for fac in soup.find("ul",class_="structural-units").find_all("li"):
            item = Item()
            txt = fac.find("h2").text
            href = fac.find("div",class_="details").find_all("p")[-1].find("span",class_="value").find("a").text
        
            item["title"] = txt
            item["url"] = href
            yield item