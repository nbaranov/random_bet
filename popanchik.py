#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re
from read_from_livescore import matches
from moduls.ends import ends


def popanmatches(matches):
    popanmatches = []
    print(f'Используются матчи, которые начнутся после {hour}:00')
    for line in matches:
        if ((1.45 <= line["kw1"] <= 1.85 or 1.45 <= line["kw2"] <= 1.85) and int(line["time"][0:2]) > hour
                and not ((re.search(r"(Ж)", line["team1"])) or (re.search(r"(Ж)", line["team2"]))
                         or (re.search(r"U19", line["team1"])) or (re.search(r"U19", line["team2"]))
                         or (re.search(r"U21", line["team1"])) or (re.search(r"U21", line["team2"]))
                         or (re.search(r"U20", line["team1"])) or (re.search(r"U20", line["team2"]))
                         or (re.search(r"U23", line["team1"])) or (re.search(r"U23", line["team2"])))):
            popanmatches.append(line)
    return popanmatches


def popan(popanmatches):
    press = []
    coef = 1
    while coef < min_coef:
        i = random.randint(0, len(popanmatches) - 1)
        if popanmatches[i] not in usedmatches:
            usedmatches.append(popanmatches[i])
            if popanmatches[i]["kw1"] < popanmatches[i]["kw2"]:
                press.append(popanmatches[i]["country"] + " " + popanmatches[i]["time"] + " " +
                             popanmatches[i]["team1"] + " -  " + popanmatches[i]["team2"] + " П1 кф. " + str(
                    popanmatches[i]["kw1"]))
                coef *= popanmatches[i]["kw1"]
            else:
                press.append(popanmatches[i]["country"] + " " + popanmatches[i]["time"] + " " +
                             popanmatches[i]["team1"] + " -  " + popanmatches[i]["team2"] + " П2 кф. " + str(
                    popanmatches[i]["kw2"]))
                coef *= popanmatches[i]["kw2"]
        if len(usedmatches) == len(popanmatches):
            break
    press.append(str("Ставка  \tИтоговый кф\t" + str(round(coef, 2))))
    #    print("Попанчик cобрал пресс с кф: "+ str(round(coef,2)))
    return press


hour = int(input("Со скольки часов брать матчи? "))
popanmatches = popanmatches(matches())
popanpress = []
usedmatches = []

print(
    f'Найден{ends(len(popanmatches), "", "о", "о")} {len(popanmatches)} попански{ends(len(popanmatches), "й", "х", "х")} матч{ends(len(popanmatches), "", "а", "ей")} \n')
amt_preses = int(input("Желаемое количество прессов "))
min_coef = float(input("Желаемый минимальный кеф пресса "))

for i in range(amt_preses):
    popanpress.append(popan(popanmatches))
    if len(usedmatches) == len(popanmatches):
        print("Все попанские матчи были использовали. Кеф последнего пресса может быть меньше желаемого")
        break

fileout = open("popan_out.txt", "w", encoding="UTF 8")

if len(popanpress) < 1:
    fileout.write('Попанчик сегодня отдыхает')
else:
    fileout.write("#ПальцемВНебо@probitybets\n\nПоддержка и благодарность:\nhttps://vk.com/app6887721_-93234960\n\n")
    if len(popanpress) > 1:
        fileout.write("Прессы от Попанчика на сегодня:\n")
    else:
        fileout.write("Пресс от Попанчика на сегодня:\n")
    count = 0
    for press in popanpress:
        count += 1
        fileout.write("\n" + str(count) + ".\n")
        print("\n" + str(count) + ".")
        for i in press:
            fileout.write(i + "\n")
            print(i)

fileout.close()
print(
    f'\nИспользовано {len(usedmatches)} попански{ends(len(usedmatches), "й", "х", "х")} матч{ends(len(usedmatches), "", "а", "ей")}')
print(f'Попанчик собрал {count} пресс{ends(count, "", "а", "ов")}')
input(
    "\nРабота программы успешно завершена. \nПрогнозы добавлены в файл popan_out.txt \nНажмите Enter чтобы закрыть программу.")
