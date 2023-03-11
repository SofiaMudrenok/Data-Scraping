from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://lnu.edu.ua"
URL = BASE_URL + "/about/faculties/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

page = get(URL, headers=HEADERS)
page = BeautifulSoup(page.content, "html.parser")

    
with open("data.txt", "w", encoding='utf-8') as f:
    for fac in page.find("ul",class_="structural-units").find_all("li"):
        txt = fac.find("h2").text
        href = fac.find("div",class_="details").find_all("p")[-1].find("span",class_="value").find("a").text
        url = BASE_URL + href
        print(txt)
        print(url)
        f.writelines(txt + "\n")
        f.writelines(url + "\n")

      
       
       
