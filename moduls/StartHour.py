import time

def startHour():
    hour = int(str(time.asctime())[11:13])
    if hour < 9:
        return 11
    else: 
        return hour + 2
