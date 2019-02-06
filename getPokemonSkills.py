# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import csv

url = "https://kamigame.jp/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3SM/%E3%82%8F%E3%81%96/index.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

table = soup.findAll("table")[2]
skills = table.findAll("td", {"rowspan":"2"})
type = table.findAll("span")

csvFile = open("skills.csv", 'wt', newline = '', encoding = 'utf-8')
writer = csv.writer(csvFile)

for i in range(len(skills)):
    print(skills[i].find("a").string, type[i].find("a").string)

try:
    for i in range(len(skills)):
        row = [skills[i].find("a").string, type[i].find("a").string]
        writer.writerow(row)
finally:
    csvFile.close()

