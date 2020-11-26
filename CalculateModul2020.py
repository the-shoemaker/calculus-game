def checkName():
    global Name, i, NameArr
    NameExists = False
    x = 0
    while x < i:
        if NameArr[x] == Name:
            NameExists = True
        x = x+1
    if NameExists == True:
        Question = "Name "+Name+" already exists. Take an other one... "
        Name = input(Question)
        checkName()

import random
from random import randint
        
while True:
    Players = input('How many people play? ')
    Players = int(Players)
    if Players > 11:
        print('Sorry, not more than 10 players alowed. Players set to 10. ')
        Players = 10

    NameArr = []
    ScoreArr = []
    HighScore = 0
    i = 0
    while i < Players:
        plc = i+1
        plc = str(plc)
        Question = "Player "+plc+" what's your Name? "
        Name = input(Question)
        checkName()
        NameArr.append(Name)
        i=i+1

    print("")
    
    i = 0
    while i < Players:
        Score=0
        Stop=False
        while Stop==False:
            Number=randint(1,100)
            Number2=randint(1,100)
            NumberStr = str(Number)
            Number2Str = str(Number2)
            CalcStr = "Hey " + NameArr[i] + " what's " + NumberStr + " + " + Number2Str + " = "
            Answer=input(CalcStr)
            Answer=int(Answer)
            if Answer==123456:
                print('Easter Egg, Alarm! ')
                print('You Winn!')
                Stop=True
                Score=+31**5
            else:
                if Answer==Number+Number2:
                    print('You did it! ')
                    Score=Score+1
                else: Stop=True
                print('The right Number was: ',Number+Number2)
        ScoreArr.append(Score)
        if Score > HighScore:
            HighScore = Score
        print("")
        i=i+1
        
    print("")
    
    s = HighScore
    while s >= 0:
        i = 0
        while i < Players:
            if ScoreArr[i] == s:
                print('Name: ', NameArr[i], ' Score: ', ScoreArr[i])
            i=i+1
        s=s-1
    print("")
    print("")
    print("")
