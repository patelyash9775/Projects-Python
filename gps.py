# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:32:47 2020

@author: ADMIN
"""

import csv

with open('route.csv','r') as f:
    reader = csv.reader(f)
    
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        print(lat)
        print(long)
        print(lat+long)