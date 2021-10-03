#! /usr/bin/python3
# -*- coding: utf-8 -*-

from popanchik import popanchik
from popanchik import MatchesForPopanchik
from moduls.read_from_flashscore import get_matches

MIN_COEF_OF_MATCH = 1.4
MAX_COEF_OF_MATCH = 1.75
MIN_COEF_OF_EXPRESS = 3
AMT_EXPRESES = 1

def pressWrite(press):
    for i in press:
        fileout.write(f'{i} \n')
        print(f'{i}')

print(f"Capper will create {AMT_EXPRESES} express with min coef. {MIN_COEF_OF_EXPRESS}, \
with coef. on matches from {MIN_COEF_OF_MATCH} to {MAX_COEF_OF_MATCH}")
while True:
    #data = (input("Собрать прогнозы \nна сегодня - 0 \nна завтра -1. \nВведите 0 или 1 :"))
    data = 0
    try:
        data = int(data)
        if data == 0:
            from moduls.start_hour import startHour
            hour = startHour()
            print(f'Use matches that start after {hour}:00\n')
            break
        elif data == 1:
            hour = 0
            print(f'USe all matches that start tomorow\n')
            break
        else:
            print('Write "0" for today matches or "1" for tomorow matches:')
    except:
        print('Write "0" for today matches or "1" for tomorow matches:')

matches = get_matches(data)
popmatches = MatchesForPopanchik(matches, hour, MIN_COEF_OF_MATCH, MAX_COEF_OF_MATCH)
popanpress = popanchik(popmatches, MIN_COEF_OF_EXPRESS, AMT_EXPRESES)

with open("out.txt", "w",encoding="UTF-8") as fileout:
    fileout.write("#ShotInTheDark \n\nDonat:\nhttps://www.tinkoff.ru/collectmoney/crowd/baranov.nikita10/XlSt485616/?short_link=76v8PDLRznk&httpMethod=GET\n\n")
    if len(popanpress) < 1:
        fileout.write('Capper has no predictions')
    elif len(popanpress) > 1:
        fileout.write("Express from Capper for today:\n")
        count = 0
        for press in popanpress:
            count += 1
            fileout.write(f"\nExpress {count}.\n")
            pressWrite(press)
    else:
        fileout.write("Express from Capper for today::\n")
        for press in popanpress:
            pressWrite(press)




print('\nCapper finished work. \nPredicptions in the file "out.txt" ')
