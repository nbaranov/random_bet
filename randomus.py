# -*- coding: utf-8 -*-
import random, re, sys

def read_file(name):
    lines = []
    filein = open(name, 'r', encoding = 'utf-8')
    for line in filein:
        lines.append(line)
    filein.close()
    print(lines)
    return lines

def matches():
    lines = read_file('in.txt')
    matches = []
    for i in range(0 , len(lines) -1):
        if re.match(r"[А-Я]{3,}: ", lines[i]):
            j = i + 4
            while True:
                try:
                    if re.match(r"[0-9]{2}:[0-9]{2}", lines[j]):
                        if lines[j+1] != "TKP\n":
                            if (lines[j+4] != "-\n" and
                                lines[j+5] != "-\n" and
                                lines[j+6] != "-\n"):
                                matches.append([lines[i].strip(),  lines[j].strip(), lines[j+1].strip(), lines[j+2].strip(), lines[j+4].strip(), lines[j+5].strip(), lines[j+6].strip()])
                            j += 7
                        else:
                            if (lines[j+5] != "-\n" and
                                lines[j+6] != "-\n" and
                                lines[j+7] != "-\n"):
                                matches.append([lines[i].strip(),  lines[j].strip(), lines[j+2].strip(), lines[j+3].strip() , lines[j+5].strip(), lines[j+6].strip(), lines[j+7].strip()])
                            j += 8
                    else:
                        if re.match(r"[А-Я]{3,}: ", lines[j]):
                            i = j
                            break
                        else:
                            j += 1
                except Exception:
                    break
    return matches

def popanmatches(matches):
    popanmatches = []
    for line in matches:
        if 1.45 <= float(line[4]) <= 1.85 or 1.45 <= float(line[5]) <= 1.85 or 1.45 <= float(line[6]) <= 1.85:
            popanmatches.append(line)
    return popanmatches

def popan(popanmatches):
    press = []
    coef = 1
    if len(popanmatches) <=4:
        print("Попан без пресса")
        return press
    else:
        valpress = 5
    count = 0
    forpress = []
    while count < valpress:
        i = random.randint(0, len(popanmatches)-1)
        if popanmatches[i] not in forpress:
            forpress.append(popanmatches[i])
            count +=1
    for line in forpress:
        if float(line[4]) < float(line[6]):
            press.append(line[0] + " " + str(line[1] + " " + line[2] + " -  " + line[3] + " П1 кф. " + line[4]))
            coef *= float(line[4])
        else:
            press.append(line[0] + " " + str(line[1] + " " + line[2] + " -  " + line[3] + " П2 кф. " + line[6]))
            coef *= float(line[6])
    press.append(str("Ставка  \tИтоговый кф\t" + str(round(coef,2))))
    print("Попанчик cобрал пресс с кф: "+ str(round(coef,2)))
    return press

def randbet(line):
    W1 = int(100 / float(line[4]))
    X = int(100 / float(line[5]))
    W2 = int(100 / float(line[6]))
    i = random.randint(1, W1+X+W2)
    if i < W1:
        return(str(line[1]) + "\t" + str(line[2]) + "\t-\t" + str(line[3]) + "\t Победа 1 \t ставка:\t" + str(random.randint(5, 50) *10) + "\t кеф. \t" + str(line[4]))
    elif i < W1 + X:
        return(str(line[1]) + "\t" + str(line[2]) + "\t-\t" + str(line[3]) + "\t Ничья \t ставка:\t" + str(random.randint(5, 50) *10) + "\t кеф. \t" + str(line[5]))
    else:
        return(str(line[1]) + "\t" + str(line[2]) + "\t-\t" + str(line[3]) + "\t Победа 2 \t ставка:\t" + str(random.randint(5, 50) *10) + "\t кеф. \t" + str(line[6]))
    

def rand(matches):
    champs = read_file("randomchamps.txt")
    randmatch = []
    count = 0
    for i in range(0, len(matches) - 1):
        if (matches[i][0] in champs) and (matches[i][0] not in randmatch):
            randmatch.append(matches[i][0])
            randmatch.append(randbet(matches[i]))
            count += 1
        elif (matches[i][0] in champs):
            randmatch.append(randbet(matches[i]))
            count += 1
    print("У Рандомчика матчей на сегодня: " + str(count))
    return randmatch


matches = matches()
randmatches = rand(matches)
#for i in randmatches:
#    print(i)

popanmatches = popanmatches(matches)
popanpress = popan(popanmatches)
#for i in popanpress:
#   print(i)

fileout = open("out.txt", "w", encoding = "UTF 8")
if len(randmatches) < 1:
    fileout.write('У Рандомчика сегодня выходной\n')
else:
    fileout.write('"Прогнозы" от Рандомчика на сегодня:\n')
    for i in randmatches:
        fileout.write(i + "\n")

fileout.write("\n\n")

if len(popanmatches) < 1:
    fileout.write('Попанчик сегодня отдыхает')
else:
    fileout.write("Пресс от Попанчика на сегодня:\n")
    for i in popanpress:
        fileout.write(i + "\n")
fileout.close()