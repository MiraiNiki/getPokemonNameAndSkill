# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import csv

purl = "https://kamigame.jp/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3SM/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%9A%E3%81%8B%E3%82%93%EF%BC%88%E7%AC%AC%E4%B8%80%E4%B8%96%E4%BB%A3%EF%BC%89.html"
req = requests.get(purl)

soup = BeautifulSoup(req.content, "html.parser")

tablet = soup.findAll("table")[1]
names = tablet.findAll("td", {"style":"text-align:center"})
print(names)
for name in names:
    if len(name.findAll("a"))>=2:
        print(name.findAll("a")[1].string)

        url = "https://kamigame.jp/ポケモンSM/ポケモン/"+name.findAll("a")[1].string+".html"
        r = requests.get(url)
        
        soup = BeautifulSoup(r.content, "html.parser")
        
        table = soup.findAll("table",{"","pokemon_acquire_moves_level_up"})[0].find("tbody")
        skills = table.findAll("td", {"colspan":"7"})
        csvFile = open("pokemonSkill.csv", 'w', newline = '', encoding = 'utf-8')
        writer = csv.writer(csvFile)
        
        for i in range(len(skills)):
            print(skills[i].find("a").string)

            for i in range(len(skills)):
                row = [name.findAll("a")[1].string, skills[i].find("a").string]
                writer.writerow(row)
        csvFile.close()

