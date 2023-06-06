import requests
from bs4 import BeautifulSoup as bs
import json

dico = []
def transform_url():
    url="https://www.scrapethissite.com/pages/frames/"
    res = requests.get(url)
    if not res.ok:
        print(f'Code: {res.status_code},url: {url}')
    else: 
        html = res.content
        soup = bs(html, "lxml")
        return soup

def transform_url_frame(tortue):
    url=f"https://www.scrapethissite.com/pages/frames/?frame=i&family={tortue}"
    res = requests.get(url)
    if not res.ok:
        print(f'Code: {res.status_code},url: {url}')
    else: 
        html = res.content
        soup = bs(html, "lxml")
        return soup

def json_dump(data):
    with open('./json/site4.json', 'w') as f:
        json.dump([data], f, indent=4)
        

def page_getter(page,dico):
    tortue = transform_url_frame("Carettochelyidae")
    dico.append({"Name":tortue.find("span",class_="family-name").get_text(strip=True),"Common Name":tortue.find("strong",class_="common-name").get_text(strip=True),"Description":tortue.find("p",class_="lead").get_text(strip=True)})
    return dico
