#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs


def show_persent_of_load(start, finish):
    for i in range(start, finish+1):
        sys.stdout.write(f"\rЗагрузка матчей и коэфициентов {i}%\r")
        time.sleep(0.04)


def load_matches(data):

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome("./chromedriver", chrome_options=options)
    #driver = webdriver.Chrome("chromedriver")

    driver.get("https://www.livescore.in/ru/")
    show_persent_of_load(0,50)
    time.sleep(0.5)
    if data:
        calend = driver.find_elements_by_class_name("calendar__nav")
        calend[1].click()
        time.sleep(0.5)
    show_persent_of_load(50, 80)
    tabs = driver.find_elements_by_class_name("tabs__tab")
    tabs[3].click()
    show_persent_of_load(80, 100)
    print()

    html = driver.page_source

    #with open('livescore.html', 'w', encoding="utf-8") as doc:
    #    for line in html:
    #        doc.write(line)
    driver.close()
    return html

def html_to_dict(html):
    #with open('livescore.html', 'r', encoding="utf-8") as doc:
    #    html = doc.read()

    matches = []
    atr_match = [
        "div", 'class_="event__match event__match--scheduled event__match--oneLine"',
        "div", 'class_="event__match event__match--scheduled event__match--last event__match--oneLine"']

    table = bs(html, 'html.parser').find("div", class_="sportName soccer")

    for row in table:
        if row.find("div", class_="event__titleBox"):
            country = row.find("div", class_="event__titleBox")
            spans = country.find_all("span")
            country = f"{spans[0].text}: {spans[1].text}"      
        elif row.find(atr_match):
            match = row.find_all(atr_match)
            if (len(match[1].text) == 5 or match[1].text[5:8] == "TKP"):
                try:
                    if all([match[5].span != None,
                        match[6].span != None,
                        match[7].span != None]):
                        matches.append({
                            "country": country,
                            "time": match[1].text,
                            "team1": match[2].text,
                            "team2": match[3].text,
                            "kw1": float(match[5].span.text),
                            "kx": float(match[6].span.text),
                            "kw2": float(match[7].span.text)
                            })
                except IndexError:
                    if all([match[6].span != None,
                        match[7].span != None, 
                        match[8].span != None]):
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

def matches(data):
    return html_to_dict(load_matches(data))
