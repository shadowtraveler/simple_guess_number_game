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

def cheat(my_ans,my_guess_time):
    while(1):
        cheat=""
        cheat=input("admin mode\nNo cheat!!! No cheat!!!\ninput 1:watch status\ninput 2:see the answer\ninput 3:modified guess time\ninput 0:Exit admin mode\ninput:")
        if(cheat=='0'):
            break
        elif(cheat=='1'):
            print("your guess time:",my_guess_time)
            input("Press Enter to continue...")
        elif(cheat=='2'):
            print("answer:",my_ans)
            input("Press Enter to continue...")
        elif(cheat=='3'):
            try:
                tmp=int(input("input number to modify your guess time"))
                my_guess_time=tmp
                print("Your guess time is ",my_guess_time)
                input("Press Enter to continue...")
            except:
                print('please input integer')
                input("Press Enter to continue...")
    return my_ans,my_guess_time

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

def smart_com(already_guess={},my_ans=[],paly_num=4,guess_time=0):
    print("Coming soon...")

num=[0,1,2,3,4,5,6,7,8,9]
play_num=4
ans=random.sample(num,k=play_num)
guess_time=0
while(1):
    game_mod=""
    game_mod=input("Play for yourserlf, input 1\nPlay with Computer, input 2\nPlay with Hard Computer, input 3\nExit Game, input 0\ninput:")
    if(game_mod=='1'):
        while(1):
            my_input=""
            my_input=input("Please input "+str(play_num)+" different number(input 0 to return):")
            if(my_input=='0'):
                break
            elif(my_input=='cheat'):
                cheat(ans,guess_time)
                continue
            guess=MyGuess(int(my_input))
            tmp=CheckNumber(ans,guess)
            guess_time+=1
            if(tmp[0]==play_num):
                print("You win the game by ",guess_time," time guesses.")
                input("Press Enter to continue...")
                break
            else:
                print(tmp[0],"A ",tmp[1],"B")
                input("Press Enter to continue...")
    elif(game_mod=='2'):
        com_guess_time=0
        com_already_guess={}
        while(1):
            my_input=""
            my_input=input("Please input "+str(play_num)+" different number(input 0 to return):")
            if(my_input=='0'):
                break
            elif(my_input=='cheat'):
                ans,guess_time=cheat(ans,guess_time)
                continue
            guess=MyGuess(int(my_input))
            tmp=CheckNumber(ans,guess)
            guess_time+=1
            if(tmp[0]==play_num):
                print("You win the game by ",guess_time," time guesses.")
                input("Press Enter to continue...")
                break
            else:
                print(tmp[0],"A ",tmp[1],"B")
                input("Press Enter to continue...")
            com_already_guess,com_guess_time,fin=easy_com(already_guess=com_already_guess,my_ans=ans,play_num=play_num,guess_time=com_guess_time)
            input("Press Enter to continue...")
            if(fin==1):
                break
    elif(game_mod=='3'):
        smart_com()
        input("Press Enter to continue...")
    elif(game_mod=='0'):
        break
    
