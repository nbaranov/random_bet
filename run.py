# -*- coding: utf-8 -*-

from moduls.StartHour import startHour
hour = startHour()
print(f'Используются матчи, которые начнутся после {hour}:00')


from popanchik import popanchik
from randomchik import randomchik

def pressWrite(press):
    for i in press:
        fileout.write(f'{i} \n')

popanpress = popanchik()
randomMatches = randomchik()

fileout = open("out.txt", "w",encoding="UTF-8")

if len(popanpress) < 1:
    fileout.write('Попанчик сегодня отдыхает')
else:
    fileout.write("#ПальцемВНебо@probitybets\n\nПоддержка и благодарность:\nhttps://vk.com/app6887721_-93234960\n\n")
    if len(popanpress) > 1:
        fileout.write("Прессы от Попанчика на сегодня:\n")
        count = 0
        for press in popanpress:
            count += 1
            fileout.write(f"\nПресс {count} .\n")
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

fileout.close()
input("\nРабота программы успешно завершена. \nПрогнозы добавлены в файл out.txt \nНажмите Enter чтобы закрыть программу.")