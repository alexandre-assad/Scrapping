import requests
from bs4 import BeautifulSoup as bs
import json

dico = []
def transform_url(page):
    url=f"https://www.scrapethissite.com/pages/frames/"
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