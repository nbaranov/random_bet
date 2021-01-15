#! /usr/bin/python3
# -*- coding: utf-8 -*-

from popanchik import popanchik
from popanchik import returnMatchesForPopanchik
from moduls.read_from_livescore import matches

def pressWrite(press):
    for i in press:
        fileout.write(f'{i} \n')

while True:
    data = (input("Собрать прогнозы \nна сегодня - 0 \nна завтра -1. \nВведите 0 или 1 :"))
    try:
        data = int(data)
        if data == 0:
            from moduls.start_hour import startHour
            hour = startHour()
            print(f'Используются матчи, которые начнутся после {hour}:00\n')
            break
        elif data == 1:
            hour = 0
            print(f'Используются все матчи, которые начнутся завтра\n')
            break
        else:
            print('Введите "0" для матчей сегодня или "1" для матчей завтра :')
    except:
        print('Введите "0" для матчей сегодня или "1" для матчей завтра :')

matches = matches(data)
popmatches = returnMatchesForPopanchik(matches, hour, 1.4, 1.75)
popanpress = popanchik(popmatches)

with open("out.txt", "w",encoding="UTF-8") as fileout:
    fileout.write("#ПальцемВНебо@probitybets\n\nПоддержка и благодарность:\nhttps://vk.com/app6887721_-93234960\n\n")
    if len(popanpress) < 1:
        fileout.write('Попанчик сегодня отдыхает')
    elif len(popanpress) > 1:
        fileout.write("Прессы от Попанчика на сегодня:\n")
        count = 0
        for press in popanpress:
            count += 1
            fileout.write(f"\nПресс {count}.\n")
            pressWrite(press)
    else:
        fileout.write("Пресс от Попанчика на сегодня:\n")
        for press in popanpress:
            pressWrite(press)

    fileout.write('\n\nВсе "попанcкие" матчи на сегодня:\n')
    for match in popmatches:
        if match["kw1"] < match["kw2"]:
            fileout.write(f'{match["country"]} {match["time"]} {match["team1"]} - {match["team2"]} П1 кф. {match["kw1"]} \n')
        else:
            fileout.write(f'{match["country"]} {match["time"]} {match["team1"]} - {match["team2"]} П2 кф. {match["kw2"]} \n')




print("\nРабота программы успешно завершена. \nПрогнозы добавлены в файл out.txt ")
