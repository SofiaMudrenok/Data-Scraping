import scrapy
from bs4 import BeautifulSoup
from lab2.items import Lab2Item

class LnuSpider(scrapy.Spider):
    name = "lnu"
    allowed_domains = ["lnu.edu.ua"]
    start_urls = ["http://lnu.edu.ua/about/faculties/"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        for fac in soup.find("ul",class_="structural-units").find_all("li"):
            txt = fac.find("h2").text
            href = fac.find("div",class_="details").find_all("p")[-1].find("span",class_="value").find("a").text
        
            yield Lab2Item(
                name= txt,
                link="https://" + href
            )