import requests
from bs4 import BeautifulSoup as bs
import json

dico = []
def transform_url(page):
    res = requests.get(
        url=f"https://www.scrapethissite.com/pages/ajax-javascript/#2013")
    html = res.content
    soup = bs(html, "lxml")
    return soup


def json_dump(data):
    with open('./json/site3.json', 'w') as f:
        json.dump([data], f, indent=4)
        
def page_getter(page, dico):
    films = transform_url(page).find_all("tr", class_="film")
    for film in films:
        best_pic = film.find("td",class_="film-best-picture ")
        print(best_pic)
    return dico

films = transform_url(3).find_all("tr", class_="film")
for film in films:
    best_pic = film.find("td",class_="film-best-picture ")
    print(best_pic)
            