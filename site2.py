import requests
from bs4 import BeautifulSoup as bs
import json


dico = {}


def transform_url(page):
    res = requests.get(url = f"https://www.scrapethissite.com/pages/forms/?page_num={page}&per_page=100")
    html = res.content
    soup = bs(html, "lxml")
    return soup

def json_dump(data):
    with open('site2.json', 'w') as f:
        json.dump([data], f, indent=4)


equipes = transform_url(1).find_all("tr", class_="team")

i= 0
for equipe in equipes:
    try:
        dico[equipe.find("td", class_="name").get_text(strip=True)] = {'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find("td", class_="ot-losses").get_text(
            strip=True), 'Win%': equipe.find("td", class_="pct text-success").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-success").get_text(strip=True)}
    except:
        try:
            dico[equipe.find("td", class_="name").get_text(strip=True)] = {'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find(
                "td", class_="ot-losses").get_text(strip=True), 'Win%': equipe.find("td", class_="pct text-success").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-danger").get_text(strip=True)}
        except:
            try:
                dico[equipe.find("td", class_="name").get_text(strip=True)] = {'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find(
                    "td", class_="ot-losses").get_text(strip=True), 'Win%': equipe.find("td", class_="pct text-danger").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-success").get_text(strip=True)}
            except:
                dico[equipe.find("td", class_="name").get_text(strip=True)] = {'Year': equipe.find("td", class_="year").get_text(strip=True), 'Wins': equipe.find("td", class_="wins").get_text(strip=True), 'Losses': equipe.find("td", class_="losses").get_text(strip=True), 'OT losses': equipe.find(
                    "td", class_="ot-losses").get_text(strip=True), 'Win%': equipe.find("td", class_="pct text-danger").get_text(strip=True), 'Goal For': equipe.find("td", class_="gf").get_text(strip=True), 'Goals Against': equipe.find("td", class_="ga").get_text(strip=True), '+/-': equipe.find("td", class_="diff text-danger").get_text(strip=True)}

print(dico)
json_dump(dico)




