import requests
from bs4 import BeautifulSoup as bs


url = "https://www.scrapethissite.com/pages/simple/"

dico = {}
res = requests.get(url)

html = res.content

soup = bs(html,"lxml")

pays = soup.find_all("div",class_="col-md-4 country")

for pay in pays:
    dico[pay.find("h3",class_="country-name").get_text(strip=True)] = {'Capitale' : pay.find("span",class_="country-capital").get_text(),'Population' : pay.find("span",class_="country-population").get_text(),'Area' :pay.find("span",class_="country-area").get_text()}

print(dico)







