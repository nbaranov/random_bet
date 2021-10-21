#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

def dataAndStartHour():
    hour = int(str(time.asctime())[11:13])
    if hour < 9:
        return (0, 11)
    else: 
        return (0, (hour + 2))  if ((hour + 2) < 24) else (1, 0) 
