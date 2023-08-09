# snake water gun game
# snake vs water > snake wins
# water vs gun > water wins
# gun vs snake > gun wins 

import random as rs

print("\nWelcome to the game")

uname = str(input("\nEnter your name : "))

print("So... nice name you got ... ")

lt = ["snake", "water", "gun"]

tn = int(input("\nEnter the number of rounds you want to play : "))

ucount = 0
ccount = 0
md = 0

while True:
    tc=int(input('''
Snake Water Gun game 
1 Begin game 
2 Stop | Exit game                                    
'''))
    if tc == 1:
        for a in range (0, tn):
                ui = int(input('''
1 snake
2 water
3 gun                                                      
'''))
                if ui == 1:
                    uselects = "snake"
                elif ui == 2:
                    uselects = "water"
                elif ui == 3:
                    uselects = "gun"
                cselects=rs.choice(lt)
                if uselects == cselects:
                    print("Match draw")
                    print(str(uname)+" chose : ", uselects)
                    print("computer chose : ", cselects)
                    md = md + 1
                elif(uselects == "gun" and cselects == "snake") or (uselects == "snake" and cselects == "water") or (uselects == "water" and cselects == "gun"):
                    print(str(uname)+" won the round")
                    print(str(uname)+" chose : ", uselects)
                    print("computer chose : ", cselects)
                    ucount = ucount + 1
                else:
                    print("Computer won the round")
                    print(str(uname)+" chose : ", uselects)
                    print("computer chose : ", cselects)
                    ccount = ccount + 1
        if ucount == ccount:
            print("\nFinal match draw")
            print("No of rounds won by "+str(uname)+" :", ucount)     
            print("No of rounds won by computer : ", ccount)
            print("No of rounds draw : ", md)
        elif ucount > ccount:
            print("\nCongratulation! .. You won the game") 
            print("No of rounds won by "+str(uname)+" :", ucount)
            print("No of rounds won by computer : ", ccount)
            print("No of rounds draw : ", md)
        else :
            print("\nComputer won the game")
            print("No of rounds won by "+str(uname)+" :", ucount)
            print("No of rounds won by computer : ", ccount)
            print("No of rounds draw : ", md)
    else :
        break        

