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
	else:
		W1 = int(100 / line[3])
		X = int(100 / line[4])
		W2 = int(100 / line[5])
		i = random.randint(1, W1+X+W2)
		#print(W1, W1+X, W1+X+W2, i)
		if i < W1:
			fileout.write(str(line[0]) + "\t" + str(line[1]) + "\t-\t" + str(line[2]) + "\t Победа 1 \t ставка:\t" + str(random.randint(5, 50) *10) + "\t кеф. \t" + str(line[3]) + "\n")
		elif i < W1 + X:
			fileout.write(str(line[0]) + "\t" + str(line[1]) + "\t-\t" + str(line[2]) + "\t Ничья \t ставка:\t" + str(random.randint(5, 50) *10) + "\t кеф. \t" + str(line[4]) + "\n")
		else:
			fileout.write(str(line[0]) + "\t" + str(line[1]) + "\t-\t" + str(line[2]) + "\t Победа 2 \t ставка:\t" + str(random.randint(5, 50) *10) + "\t кеф. \t" + str(line[5]) + "\n")

fileout.close()
