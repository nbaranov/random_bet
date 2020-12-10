<<<<<<< HEAD
#!/usr/bin/python3
=======
#! /bin/python3
>>>>>>> 92f26e8e87f80157b6005a2edbca9673996bea3e
# -*- coding: utf-8 -*-

from popanchik import popanchik
from randomchik import randomchik
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
popanpress = popanchik(matches, hour, 1.4, 1.75)
randomMatches = randomchik(matches, hour)

with open("out.txt", "w",encoding="UTF-8") as fileout:
    if len(popanpress) < 1:
        fileout.write('Попанчик сегодня отдыхает')
    else:
        fileout.write("#ПальцемВНебо@probitybets\n\nПоддержка и благодарность:\nhttps://vk.com/app6887721_-93234960\n\n")
        if len(popanpress) > 1:
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

    if len(randomMatches) < 1:
        fileout.write("\nРандомчик сегодня отдыхает")
    else:
        fileout.write("\nПрогнозы от Рандомчика на сегодня\n")
        for match in randomMatches:
            fileout.write(match + "\n")


print("\nРабота программы успешно завершена. \nПрогнозы добавлены в файл out.txt ")
