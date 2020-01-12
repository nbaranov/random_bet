#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs

'''
def matches():

    driver = webdriver.Chrome(executable_path="/home/nick/Documents/random_bet/chromedriver")
    driver.get("https://www.livescore.in/ru/")
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div[2]/div[7]/div[2]/div[1]/div[1]/div[4]').click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div[2]/div").click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/form/div[6]/div[1]/div/label[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/a').click()
    time.sleep(1)

    html = driver.page_source

    with open('livescore.html', 'w', encoding="utf-8") as doc:
        for line in html:
            doc.write(line)

    driver.close()

'''
with open('livescore.html', 'r', encoding="utf-8") as doc:
    html = doc.read()


matches = []
atr_match = [
    "div", 'class_="event__match event__match--scheduled event__match--oneLine"',
    "div", 'class_="event__match event__match--scheduled event__match--last event__match--oneLine"',
]

soup = bs(html)
table = soup.find("div", class_="sportName soccer")

for row in table:
    if row.find("div", class_="event__titleBox"):
        country = row.find("div", class_="event__titleBox")
        spans = country.find_all("span")
        country = f"{spans[0].text}: {spans[1].text}"
        print(country)
    
    elif row.find(atr_match):
        match = row.find_all(atr_match)
        if len(match[1].text) > 5:
            if (re.match(r"\d{2}:\d{2}", match[1].text) and match[6].span != None and
                match[7].span != None and match[7].span != None):
                print(match)
                matches.append({
                    "country": country,
                    "time": match[2].text,
                    "team1": match[3].text,
                    "team2": match[4].text,
                    "kw1": float(match[6].span.text),
                    "kx": float(match[7].span.text),
                    "kw2": float(match[8].span.text)
                    })
        elif (re.match(r"\d{2}:\d{2}", match[1].text) and match[5].span != None and
            match[6].span != None and match[7].span != None):
            matches.append({
                "country": country,
                "time": match[1].text,
                "team1": match[2].text,
                "team2": match[3].text,
                "kw1": float(match[5].span.text),
                "kx": float(match[6].span.text),
                "kw2": float(match[7].span.text)
                })
    
#return matches

matches()
