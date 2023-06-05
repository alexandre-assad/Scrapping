import requests
from bs4 import BeautifulSoup as bs
import json


dico = []


def transform_url(page):
    res = requests.get(
        url=f"https://www.scrapethissite.com/pages/forms/?page_num={page}&per_page=25")
    html = res.content
    soup = bs(html, "lxml")
    return soup


def json_dump(data):
    with open('./json/site2.json', 'w') as f:
        json.dump([data], f, indent=4)


def page_getter(page, dico):
    equipes = transform_url(page).find_all("tr", class_="team")
    for equipe in equipes:

        try:
            dico.append({'Name': equipe.find("td", class_="name").get_text(strip=True), 'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find("td", class_="ot-losses").get_text(
                strip=True), 'Win%': equipe.find("td", class_="pct text-success").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-success").get_text(strip=True)})

        except:
            try:
                dico.append({'Name': equipe.find("td", class_="name").get_text(strip=True), 'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find(
                    "td", class_="ot-losses").get_text(strip=True), 'Win%': equipe.find("td", class_="pct text-success").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-danger").get_text(strip=True)})

            except:
                try:
                    dico.append({'Name': equipe.find("td", class_="name").get_text(strip=True), 'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find(
                        "td", class_="ot-losses").get_text(strip=True), 'Win%': equipe.find("td", class_="pct text-danger").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-success").get_text(strip=True)})

                except:
                    dico.append({'Name': equipe.find("td", class_="name").get_text(strip=True), 'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find(
                        "td", class_="ot-losses").get_text(strip=True), 'Win%': equipe.find("td", class_="pct text-danger").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-danger").get_text(strip=True)})
    return dico


def how_many_pages():
    page = 1
    soup = transform_url(page)
    pagination = soup.find("ul", class_="pagination")
    while True:
        all_a = pagination.find_all("a")
        compteur = 0
        for i in all_a:

            try:

                if i['aria-label'] == "Next":
                    compteur += 1
            except:
                pass
        if compteur == 1:
            page += 1
            soup = transform_url(page)
            pagination = soup.find("ul", class_="pagination")
            compteur = 0
        else:
            return page


def get_page():
    data = []
    dico = []
    for i in range(1, how_many_pages()+1):
        data = page_getter(i, dico)
    json_dump(data)


get_page()
