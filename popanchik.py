#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re
from read_from_livescore import matches
from moduls.ends import ends
from moduls.StartHour import startHour


def popanmatches(matches):
    popanmatches = []
#    print(f'Используются матчи, которые начнутся после {hour}:00')
    for line in matches:
        if ((1.45 <= line["kw1"] <= 1.85 or 1.45 <= line["kw2"] <= 1.85) and int(line["time"][0:2]) > hour
                and not ((re.search(r"\(Ж\)", line["team1"])) or (re.search(r"\(Ж\)", line["team2"]))
                         or (re.search(r"U19", line["team1"])) or (re.search(r"U19", line["team2"]))
                         or (re.search(r"U21", line["team1"])) or (re.search(r"U21", line["team2"]))
                         or (re.search(r"U20", line["team1"])) or (re.search(r"U20", line["team2"]))
                         or (re.search(r"U23", line["team1"])) or (re.search(r"U23", line["team2"])))):
            popanmatches.append(line)
    return popanmatches


def popan(popanmatches):
    press = []
    coef = 1
    a = 0
    ligth_press = random.randint(2,5)
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


def popanchik():
    popanpress = []

    print(f'''Найден{ends(len(popanmatches), "", "о", "о")} \
{len(popanmatches)} матч{ends(len(popanmatches), "", "а", "ей")} для Попанчика ''')

    for _ in range(amt_preses):
        press = popan(popanmatches)
        if press == None: continue
        else: popanpress.append(press)

    return popanpress


hour = startHour()
amt_preses = 2
usedmatches = []
popanmatches = popanmatches(matches())
