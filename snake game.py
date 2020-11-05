# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:33:51 2020

@author: ADMIN
"""

import random
end=100

def snake_ladder(pos):
    sl_dict={1:38,4:14,8:30,21:42,28:76,32:10,36:6,48:26,50:67,52:18,71:92,80:99,88:24,95:56,97:78}
    if pos in sl_dict.keys():
        return(sl_dict[pos])
    else:
        return(pos)


def play():
    pos=0
    turn=0
    print("Let's play Snakes and ladders!")
    while(1):
        c=input('Press 1 to roll Dice/0 to Quit')
        if(c==0):
            break;
        roll=random.randint(1,6)
        turn=turn+1
        pos_roll=pos+roll
        pos=snake_ladder(pos_roll)
        if(pos>pos_roll):
            print("Hurray! Tou climes a ladder ,Your score is ",pos)
        elif(pos<pos_roll):
            print("OOPS! You are bitten by a snake , Your score is ",pos)
        else:
            print("Your position is ",pos)
        if(pos>=end):
            print("You won in ",turn," turns")
            break;
        
play()
        