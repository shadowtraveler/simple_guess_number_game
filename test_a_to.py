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

def easy_com(already_guess={},my_ans=[],play_num=4,guess_time=0):
    while(1):
        num=[0,1,2,3,4,5,6,7,8,9]
        com_ans=random.sample(num,k=play_num)
        if(already_guess.get(str(com_ans))==None):
            already_guess[str(com_ans)]=1
            break
    print("computer guess:",com_ans)
    tmp=CheckNumber(my_ans,com_ans)
    guess_time+=1
    fin=0
    if(tmp[0]==play_num):
        fin=1
        print("Computer(easy) win the game by ",guess_time," time guesses.")
        return already_guess,guess_time,fin
    else:
        print(tmp[0],"A ",tmp[1],"B")
        return already_guess,guess_time,fin

num=[0,1,2,3,4,5,6,7,8,9]
play_num=4
ans=random.sample(num,k=play_num)
guess_time=0
while(1):
    game_mod=""
    game_mod=input("Play for yourserlf, input 1\nPlay with Computer, input 2\nExit Game, input 0\ninput:")
    if(game_mod=='1' or game_mod=='2'):
        com_guess_time=0
        com_already_guess={}
        while(1):
            my_input=""
            my_input=input("Please input "+str(play_num)+" different number(input 0 to return):")
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
            if(game_mod=='2'):
                com_already_guess,com_guess_time,fin=easy_com(already_guess=com_already_guess,my_ans=ans,play_num=play_num,guess_time=com_guess_time)
                if(fin==1):
                    break
    #elif(game_mod=='2'):
    elif(game_mod=='0'):
        break
    
