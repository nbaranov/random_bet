# -*- coding: utf-8 -*-

import re


def read_file(name):
    lines = []
    filein = open(name, 'r', encoding='utf-8')
    for line in filein:
        lines.append(line)
    filein.close()
    return lines


def matches():
    filein = read_file('in.txt')
    lines = []
    for line in filein:
        lines.append(line.split("\t"))

    matches = []
    for i in range(len(lines) - 1, 0, -1):
        if not ((re.match(r"[А-Я ]{3,}:", lines[i][0])) or (
                re.match(r"[0-9]{2}:[0-9]{2}", lines[i][0]) and lines[i][3] == '-')):
            del lines[i]
        elif (re.match(r"[А-Я ]{3,}:", lines[i][0])):
            liga = ""
            for j in range(0, len(lines[i]) - 4):
                liga += str(lines[i][j] + " ")
            lines[i] = [liga.strip()]

    for i in range(1, len(lines) - 2):
        if (re.match(r"[А-Я ]{3,}:", lines[i][0])):
            j = i + 1
            while True:
                try:
                    if re.match(r"[0-9]{2}:[0-9]{2}", lines[j][0]):
                        if lines[j][1] != "TKP":
                            if (lines[j][4] != "-" and
                                    lines[j][5] != "-" and
                                    lines[j][6] != "-"):
                                matches.append({"country": lines[i][0].strip(),
                                                "time": lines[j][0].strip(),
                                                "team1": lines[j][1].strip(),
                                                "team2": lines[j][2].strip(),
                                                "kw1": float(lines[j][4].strip()),
                                                "kx": float(lines[j][5].strip()),
                                                "kw2": float(lines[j][6].strip())})
                            j += 1
                        else:
                            if (lines[j][5] != "-" and
                                    lines[j][6] != "-" and
                                    lines[j][7] != "-"):
                                matches.append({"country": lines[i][0].strip(),
                                                "time": lines[j][0].strip(),
                                                "team1": lines[j][2].strip(),
                                                "team2": lines[j][3].strip(),
                                                "kw1": float(lines[j][5].strip()),
                                                "kx": float(lines[j][6].strip()),
                                                "kw2": float(lines[j][7].strip())})
                            j += 1
                    elif re.match(r"[А-Я ]{3,}: ", lines[j]):
                        i = j
                        break
                    else:
                        j += 1
                except Exception:
                    break
    return matches

