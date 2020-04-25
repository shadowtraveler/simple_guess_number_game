# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:27:51 2020

@author: steve
"""

import random

def CheckNumber(ans,guess):
    play_num=4
    a=0
    b=0
    for i in range(play_num):
        for j in range(play_num):
            if(ans[i]==guess[j]):
                if(i==j):
                    a+=1
                elif(i!=j):
                    b+=1
    return [a,b]

def MyGuess(num):
    tmp=[]
    play_num=4
    first_check=10**(play_num-1)
    if(num<first_check):
        while(num>10):
            tmp.insert(0,int(num%10))
            num/=10
        tmp.insert(0,int(num))
        tmp.insert(0,0)
    else:
        while(num>10):
            tmp.insert(0,int(num%10))
            num/=10
        tmp.insert(0,int(num))
    return tmp

num=[0,1,2,3,4,5,6,7,8,9,0]
play_num=4
ans=random.sample(num,k=play_num)
guess_time=0
while(1):
    my_input=""
    my_input=input("Please input "+str(play_num)+" different number:")
    if(my_input=='0'):
        break
    guess=MyGuess(int(my_input))
    tmp=CheckNumber(ans,guess)
    guess_time+=1
    if(tmp[0]==play_num):
        print("You win the game by ",guess_time," time guesses.")
        break
    else:
        print(tmp[0],"A ",tmp[1],"B")
    
