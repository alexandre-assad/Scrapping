import requests
from bs4 import BeautifulSoup as bs
import json

dico = []
def transform_url():
    url="https://www.scrapethissite.com/pages/frames/?frame=i"
    res = requests.get(url)
    if not res.ok:
        print(f'Code: {res.status_code},url: {url}')
    else: 
        html = res.content
        soup = bs(html, "lxml")
        return soup

def json_dump(data):
    with open('./json/moonboot.json', 'w') as f:
        json.dump([data], f, indent=4)