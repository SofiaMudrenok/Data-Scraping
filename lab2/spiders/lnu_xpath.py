import scrapy
from lab2.items import Lab2Item

class LnuSpider(scrapy.Spider):
    name = "lnu_xpath"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/about/faculties/"]

    def parse(self, response):
        items=response.xpath('//ul[contains(@class,"structural-units")]').xpath('.//li')
        for fac in items:
            txt = fac.xpath('.//h2/text()').get()
            href = fac.xpath('.//div[contains(@class,"details")]').xpath('.//p')[-1].xpath('.//span[contains(@class,"value")]').xpath('.//a/text()').get()
        
            yield Lab2Item(
                name= txt,
                link="https://" + href
            )