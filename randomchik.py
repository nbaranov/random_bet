#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re
from moduls.read_from_livescore import matches
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
	else:
		count = random.randint(2,len(matches) - 1)

	for _ in range(count): 
		i = random.randint(0, len(matches)-1)
		chanceW1 = int (100 / matches[i]["kw1"])
		chanceX = int (100 / matches[i]["kx"])
		chanceW2 = int (100 / matches[i]["kw2"])
		fullChance = chanceW1 + chanceX + chanceW2
		stavka = random.randint(50,100)
		result = random.randint(0, fullChance)
		if result <= chanceW1:
			randomMathches.append(f'{matches[i]["country"]} {matches[i]["time"]} {matches[i]["team1"]} - {matches[i]["team2"]}\tПобеда1\tсумма\t{stavka}\tкф.\t{matches[i]["kw1"]}') 
		elif result <= chanceW1 + chanceX:
			randomMathches.append(f'{matches[i]["country"]} {matches[i]["time"]} {matches[i]["team1"]} - {matches[i]["team2"]}\tНичья\tсумма\t{stavka}\tкф.\t{matches[i]["kx"]}')
		else:
			randomMathches.append(f'{matches[i]["country"]} {matches[i]["time"]} {matches[i]["team1"]} - {matches[i]["team2"]}\t Победа2\tсумма\t{stavka}\tкф.\t{matches[i]["kw2"]}')
		matches.pop(i)
	return randomMathches

hour = startHour()
matches = randomMathches(matches()) # отбираем матчи фукцией randomMatches с аргументом функцией matches из модуля read_from_livescore
