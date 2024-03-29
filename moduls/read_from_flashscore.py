#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from typing import Text
import requests

from bs4 import BeautifulSoup as bs

def load_matches(data):

    if data == 0:
        response = requests.get('http://www.flashscore.mobi/?d=0&s=5')
        html = response.text.replace('<br />', '\n')
    elif data == 1:
        response = requests.get('http://www.flashscore.mobi/?d=1&s=5')
        html = response.text.replace('<br />', '\n')

        
    with open('livescore.html', 'w', encoding="utf-8") as doc:
        for line in html:
            doc.write(line)
    return html

def html_to_dict(html):
    # with open('livescore.html', 'r', encoding="utf-8") as doc:
    #     html = doc.read()
    matches = []
    
    table = bs(html, 'html.parser').find('div', attrs={'id' : 'score-data'}).text.split('\n')
    table[0] = table[0].split('!')[1]
    for row in table:
        try:
            if (re.match('[A-Z]{3}', row)):
                row = re.split("(\d{2}:\d{2})|(\d+')", row)
                country = row[0]
                if ("-:-" in row[3]) and ('[' in row[3]) and (']' in row[3] and ('Перенесен' not in row[3])):
                    time = row[1]
                    teams = row[3].split('-:-')[0].strip().split(' - ')
                    team1, team2 = teams[0], teams[1]
                    kf = row[3].split('[')[-1][:-1].split('|')
                    matches.append({
                        "country": country,
                        "time": time,
                        "team1": team1,
                        "team2": team2,
                        "kw1": float(kf[0].strip()),
                        "kx": float(kf[1].strip()),
                        "kw2": float(kf[2].strip())
                        })
            elif ("-:-" in row) and ('[' in row) and (']' in row) and ('Перенесен' not in row):
                time = row[:5]
                teams = row.split('-:-')[0][5:].strip().split(' - ')
                team1, team2 = teams[0], teams[1]
                kf = row.split('[')[-1][:-1].split('|')
                matches.append({
                    "country": country,
                    "time": time,
                    "team1": team1,
                    "team2": team2,
                    "kw1": float(kf[0].strip()),
                    "kx": float(kf[1].strip()),
                    "kw2": float(kf[2].strip())
                    })
        except IndexError:
            continue
        except ValueError:
            continue # В случае если нет коэффциента на победу (стоит прочерк)
    return matches

def get_matches(data):
    return html_to_dict(load_matches(data))

if __name__ == '__main__':
    matches = html_to_dict(load_matches(0))
    print(matches)