import requests
from bs4 import BeautifulSoup as bs
import json

dico = []
def transform_url(page):
    url=f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={2015-page}"
    res = requests.get(url)
    if not res.ok:
        print(f'Code: {res.status_code},url: {url}')
    else: 
        html = res.content
        soup = bs(html, "lxml")
        return soup


def json_dump(data):
    with open('./json/site3.json', 'w') as f:
        json.dump([data], f, indent=4)
        
def page_getter(page, dico):
    dico.append(json.loads(transform_url(page).get_text(strip=True)))
    return dico

def scrap(dico):
    for i in range(6):
        dico = page_getter(i, dico)
    json_dump(dico)

scrap(dico)