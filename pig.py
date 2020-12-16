from random import choice

def popan_pig(popanmatches):
    temp_list = popanmatches.copy()
    if len(temp_list) == 0:
        return None
    elif len(temp_list) > 1:
        part = choice([True, False])
        if part:
            return popan_pig(temp_list[len(temp_list)//2:])
        else:
            return popan_pig(temp_list[:len(temp_list)//2])
    else:
        match = temp_list[0]
        if match['kw1'] < match['kw2']:
            return f'{match["country"]} {match["time"]} {match["team1"]} - {match["team2"]}\tПобеда1\tкф.\t{match["kw1"]}'
        else:
            return f'{match["country"]} {match["time"]} {match["team1"]} - {match["team2"]}\t Победа2\tкф.\t{match["kw2"]}'