'''
if ((len(lines[i]) < 4) or (re.search(r"(Ж)", lines[i][1])) or (re.search(r"(Ж)", lines[i][2]))
        or (re.search(r"U19", lines[i][1])) or (re.search(r"U19", lines[i][2]))
        or (re.search(r"U21", lines[i][1])) or (re.search(r"U21", lines[i][2]))
        or (re.search(r"U20", lines[i][1])) or (re.search(r"U20", lines[i][2]))
        or (re.search(r"U23", lines[i][1])) or (re.search(r"U23", lines[i][2]))):
    del lines[i]

if ((re.match(r"[А-Я ]{3,}:", lines[i][0])) and not
((re.match(r"АФРИКА:", lines[i][0])) or (re.match(r"ЕВРОПА:", lines[i][0])) or
 (re.match(r"МИР:", lines[i][0])) or (re.match(r"АЗИЯ:", lines[i][0])) or
 (re.search(r"Женская", lines[i][0])) or (re.search(r"Женщины", lines[i][0])) or (
         re.search(r"Women", lines[i][0])))):
'''