#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs

def matches(data):


    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get("https://www.livescore.in/ru/")
    time.sleep(5)
    if data == 1:
        calend = driver.find_elements_by_class_name("calendar__nav")
        calend[1].click()
        time.sleep(4)
    tabs = driver.find_elements_by_class_name("tabs__tab")
    tabs[3].click()
    time.sleep(4)
    botons = driver.find_elements_by_class_name("header__button")
    botons[1].click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="livescore-settings-form"]/div[6]/div[1]/div/label[1]/input').click()
    time.sleep(0.5)
    driver.find_element_by_id("lsid-window-close").click()
    time.sleep(0.5)


    html = driver.page_source

    with open('livescore.html', 'w', encoding="utf-8") as doc:
        for line in html:
            doc.write(line)

    driver.close()

    with open('livescore.html', 'r', encoding="utf-8") as doc:
        html = doc.read()


    matches = []
    atr_match = [
        "div", 'class_="event__match event__match--scheduled event__match--oneLine"',
        "div", 'class_="event__match event__match--scheduled event__match--last event__match--oneLine"',
    ]

    soup = bs(html, 'html.parser')
    table = soup.find("div", class_="sportName soccer")

    for row in table:
        if row.find("div", class_="event__titleBox"):
            country = row.find("div", class_="event__titleBox")
            spans = country.find_all("span")
            country = f"{spans[0].text}: {spans[1].text}"
        
        elif row.find(atr_match):
            match = row.find_all(atr_match)
            if (len(match[1].text) == 5 or match[1].text[5:8] == "TKP"):
                try:
                    if (match[5].span != None and
                        match[6].span != None and 
                        match[7].span != None):
                        matches.append({
                            "country": country,
                            "time": match[1].text,
                            "team1": match[2].text,
                            "team2": match[3].text,
                            "kw1": float(match[5].span.text),
                            "kx": float(match[6].span.text),
                            "kw2": float(match[7].span.text)
                            })
                except:
                    if (match[6].span != None and
                        match[7].span != None and 
                        match[8].span != None):
                        matches.append({
                            "country": country,
                            "time": match[1].text[:5],
                            "team1": match[3].text,
                            "team2": match[4].text,
                            "kw1": float(match[6].span.text),
                            "kx": float(match[7].span.text),
                            "kw2": float(match[8].span.text)
                            })

    return matches

