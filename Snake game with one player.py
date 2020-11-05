# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:14:35 2020

@author: ADMIN
"""

import random

def play(psn,flag):
    snake_begin=-1
    snake_end=-1
    while(snake_begin<=snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    print('Snake from ',snake_begin,' to ',snake_end)
    r=random.randint(1,6)
    print('Dice rolled: ',r)
    if(psn==0):
        if(r==1 or r==6):
            psn=1
    else:
        psn=psn+r
    print('Position= ',psn)
    if(psn==snake_begin and flag==0):
        print("Bitten  by snake")
        psn=snake_end
        flag=1
    if(psn>=100):
        print('You won')
        return
    play(psn,flag)
    
position=0
print('position=',position)
play(position,0)