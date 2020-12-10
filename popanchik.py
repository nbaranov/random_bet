#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re
from moduls.ends import ends


def returnMatchesForPopanchik(matches, hour, mink, maxk):
    '''выбираются матчи с кефом на фаворита между 1,45 и 1,85, начнутся через 2 и более часов, не женских и не юниорских команд.'''
    popanmatches = [] 
    for line in matches:
        if ((mink <= line["kw1"] <= maxk or mink <= line["kw2"] <= maxk) and int(line["time"][0:2]) >= hour
                and not ((re.search(r"(\(Ж\))|(U\d{2})", line["team1"])) or (re.search(r"(\(Ж\))|(U\d{2})", line["team2"])))):
            popanmatches.append(line)
    return popanmatches


def getPopanPress(popanmatches):
    press = []
    coef = 1
    a = 0
    ligth_press = random.randint(2,3)
    if ligth_press > (len(popanmatches) - len(usedmatches)):
        print("Недостаточно попанских матчей на 2 пресса")
        return

    while a < ligth_press:
        i = random.randint(0, len(popanmatches) - 1)
        if popanmatches[i] not in usedmatches:
            usedmatches.append(popanmatches[i])
            a += 1
            if popanmatches[i]["kw1"] < popanmatches[i]["kw2"]:
                press.append(f'{popanmatches[i]["country"]} {popanmatches[i]["time"]} \
{popanmatches[i]["team1"]} - {popanmatches[i]["team2"]} П1 кф. {popanmatches[i]["kw1"]}')
                coef *= popanmatches[i]["kw1"]
            else:
                press.append(f'{popanmatches[i]["country"]} {popanmatches[i]["time"]} \
{popanmatches[i]["team1"]} - {popanmatches[i]["team2"]} П2 кф. {popanmatches[i]["kw2"]}')
                coef *= popanmatches[i]["kw2"]


    press.append(f"Ставка  Итоговый кф {round(coef, 2)}")
    return press


def popanchik(matches, hour, mink, maxk):
    popanpress = []
    popmatches = returnMatchesForPopanchik(matches, hour, mink, maxk)

    print(f'''Найден{ends(len(popmatches), "", "о", "о")} \
{len(popmatches)} матч{ends(len(popmatches), "", "а", "ей")} для Попанчика ''')

    for _ in range(amt_preses):
        press = getPopanPress(popmatches)
        if press == None: continue
        else: popanpress.append(press)

    return popanpress


amt_preses = 2
usedmatches = []

