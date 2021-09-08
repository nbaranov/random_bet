#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re
from moduls.ends import ends


def MatchesForPopanchik(matches, hour, mink, maxk):
    '''выбираются матчи с кефом на фаворита между 1,45 и 1,85, начнутся через 2 и более часов, не женских и не юниорских команд.'''
    popanmatches = [] 
    for line in matches:
        if all([(mink <= line["kw1"] <= maxk or mink <= line["kw2"] <= maxk),
                (int(line["time"][0:2]) >= hour),
                not ((re.search(r"(\(Ж\))|(U\d{2})", line["team1"])) or (re.search(r"(\(Ж\))|(U\d{2})", line["team2"]))),
                not (re.search(r"(товар)|(убок)|(рофей)|(БРАЗИЛИЯ)", line["country"]))]):
            popanmatches.append(line)
    return popanmatches


def getPopanPress(popanmatches, minCoefOfPress):
    coef = 1
    usedmatches = []
    press = []
    while coef < minCoefOfPress:
        if (len(popanmatches) - len(usedmatches) == 0):
            print("Недостаточно попанских матчей на пресс")
            return 
        i = random.randint(0, len(popanmatches) - 1)
        if popanmatches[i] not in usedmatches:
            usedmatches.append(popanmatches[i])
            if popanmatches[i]["kw1"] < popanmatches[i]["kw2"]:
                press.append(f'{popanmatches[i]["country"]} {popanmatches[i]["time"]} \
{popanmatches[i]["team1"]} - {popanmatches[i]["team2"]} П1 кф. {popanmatches[i]["kw1"]}')
                coef *= popanmatches[i]["kw1"]
            else:
                press.append(f'{popanmatches[i]["country"]} {popanmatches[i]["time"]} \
{popanmatches[i]["team1"]} - {popanmatches[i]["team2"]} П2 кф. {popanmatches[i]["kw2"]}')
                coef *= popanmatches[i]["kw2"]
    
    press.append(f"Итоговый кф {round(coef, 2)}")
    return press


def popanchik(popmatches, minCoefOfPress, amt_preses):
    popanpress = []

    print(f'''Найден{ends(len(popmatches), "", "о", "о")} \
{len(popmatches)} матч{ends(len(popmatches), "", "а", "ей")} для Попанчика ''')
    if len(popmatches) > 10:
        for _ in range(amt_preses):
            press = getPopanPress(popmatches, minCoefOfPress)
            if press == None: continue
            else: popanpress.append(press)

    return popanpress




