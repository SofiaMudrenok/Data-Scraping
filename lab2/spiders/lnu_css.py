import scrapy

from lab2.items import Lab2Item

class LnuCssSpider(scrapy.Spider):
    name = "lnu_css"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["https://lnu.edu.ua/about/faculties/"]

    def parse(self, response):
        items=response.css('ul.structural-units').css('li.clearfix')
        for fac in items:
            txt = fac.css('h2::text').get()
            href = fac.css('div.details').css('p')[-1].css('span.value').css('a::text').get()
        
            yield Lab2Item(
                name= txt,
                link="https://" + href
            )