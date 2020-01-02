<<<<<<< ours
import random
import re
from read_from_livescore import matches

champs = ["ГЕРМАНИЯ: Третья лига\n",
		  "НИДЕРЛАНДЫ: Первый дивизион\n",
		  "АНГЛИЯ: Первая лига\n",
		  "АНГЛИЯ: Национальная лига\n",
		  "ИТАЛИЯ: Серия В\n",
		  "ИСПАНИЯ: Сегунда\n",
		  "ИСЛАНДИЯ: Высшая лига\n",
		  "ИСЛАНДИЯ: Дивизион 1\n",
		  "ФИНЛЯНДИЯ: Высшая лига\n",
		  "ШВЕЦИЯ: Первая лига\n" ]

'''
matches = []
for i in range(0 , len(lines) -1):
	if lines[i] in champs:
		matches.append(lines[i])
		#print(lines[i])
		i += 1
		while not re.match(r"[А-Я]{5,}", lines[i]):
			#print(i, lines[i])
			if re.match(r"[0-9]{2}:[0-9]{2}", lines[i]):
				if lines[i+1] != "TKP\n":
					if lines[i+4] and lines[i+5] and lines[i+6] != "-\n":
						matches.append([lines[i].strip(),  lines[i+1].strip(), lines[i+2].strip(), float(lines[i+4].strip()), float(lines[i+5].strip()), float(lines[i+6].strip())])
						i += 7
					else:
						i += 1
				else:
					if lines[i+5] and lines[i+6] and lines[i+7] != "-\n":
						matches.append([lines[i].strip(),  lines[i+2].strip(), lines[i+3].strip(), float(lines[i+5].strip()), float(lines[i+6].strip()), float(lines[i+7].strip())])
						i += 8
					else:
						i += 1
			else:
				i += 1
'''

matches_list = matches()
for match in matches_list:
	print(match)


fileout = open('out.txt', 'w', encoding='utf-8')

for line in matches:
	if re.match(r"[А-Я]{4,}", str(line)):
		fileout.write(str(line))
=======
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re
from read_from_livescore import matches
from moduls.ends import ends
from moduls.StartHour import startHour


def randomMathches(matches):
	randomMathches = []
	for match in matches:
		if (match["kw1"] > 1.45) and (match["kw2"] > 1.45) and int(match["time"][0:2]) > hour:
			randomMathches.append(match)
	print(f'''Найден{ends(len(randomMathches), "", "о", "о")} \
{len(randomMathches)} матч{ends(len(randomMathches), "", "а", "ей")} для Рандомчика''')
	return randomMathches


def randomchik():
	randomMathches = []

	if len(matches) < 2:
		print("У рандомчика матчей нет")
		return  randomMathches
	elif len(matches) > 5:
		count = random.randint(2,5)
>>>>>>> theirs
	else:
		count = random.randint(2,len(matches) - 1)

	for _ in range(count): 
		i = random.randint(0, len(matches)-1)
		chanceW1 = int (100 / matches[i]["kw1"])
		chanceX = int (100 / matches[i]["kx"])
		chanceW2 = int (100 / matches[i]["kw2"])
		fullChance = chanceW1 + chanceX + chanceW2

		result = random.randint(0, fullChance)
		if result <= chanceW1:
			randomMathches.append(f'{matches[i]["country"]} {matches[i]["time"]} {matches[i]["team1"]} - {matches[i]["team2"]}\tПобеда1\t{matches[i]["kw1"]}') 
		elif result <= chanceW1 + chanceX:
			randomMathches.append(f'{matches[i]["country"]} {matches[i]["time"]} {matches[i]["team1"]} - {matches[i]["team2"]}\tНичья\t{matches[i]["kx"]}')
		else:
			randomMathches.append(f'{matches[i]["country"]} {matches[i]["time"]} {matches[i]["team1"]} - {matches[i]["team2"]}\t Победа2\t{matches[i]["kw2"]}')
		matches.pop(i)
	return randomMathches

hour = startHour()
matches = randomMathches(matches()) # отбираем матчи фукцией randomMatches с аргументом функцией matches из модуля read_from_livescore
