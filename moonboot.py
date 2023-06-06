import requests
from bs4 import BeautifulSoup as bs
import json

dico = []
def transform_url(gender,page):
    url=f"https://www.moonboot.com/fr-fr/shopping/{gender}?pageindex={page}"
    res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    if not res.ok:
        print(f'Code: {res.status_code},url: {url}')
    else: 
        html = res.content
        soup = bs(html, "lxml")
        return soup

def json_dump(data):
    with open('./json/moonboot.json', 'w') as f:
        json.dump([data], f, indent=4)

def how_many_pages(gender):
    page = 1
    soup = transform_url(gender,page)
    compteur = 0
    while True:
        try:      
            if soup.find("button",{"title":"Page suivante","class":"e1c9s0c21 css-1younqe e18fm3l50"})["disabled"] == "":
                compteur += 1
        except:
            page += 1
        if compteur == 1:
            return page
        soup = transform_url(gender,page)
        
        
page5 = transform_url("man",3)

print(how_many_pages("man"))
