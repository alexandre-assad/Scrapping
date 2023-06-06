import requests
from bs4 import BeautifulSoup as bs
import json
import re

dico = []
def url_product(url):
    res = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    html = res.content
    soup = bs(html, "lxml")
    return soup


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
        
def boot_scrap(url,dico):
    page = url_product(url) 
    name = page.find("h1",class_="e1994wwj3 css-1gdf8fv em8aoju0").get_text()
    try:
        prix = page.find("span",class_="css-wwiaj0 exudj7t1").get_text()
    except:
        prix = "Non disponible"
    dico.append({'Name':name,'Prix':prix})
    return dico
    
def page_getter(gender,page,dico):
    page = transform_url(gender,page)
    boots = page.find_all("a",class_="css-umiid9 e11ql7691")
    for boot in boots:
        url = "https://www.moonboot.com" + boot["href"]
        dico = boot_scrap(url,dico)
    return dico

def scrape(dico):
    genders = ["man",'woman']
    for gender in genders:
        for i in range(1,how_many_pages(gender)+1):
            dico = page_getter(gender,i,dico)
    json_dump(dico)
    return dico
print(scrape(dico))
