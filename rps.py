# rock vs paper > paper wins 
# rock vs scissor > rock Wins
# paper vs scissor > scissor wins

import random as rd

l = ["rock", "scissor", "paper"]

bn = int(input("Enter number of round you want to play : "))
while True:
    ucount = 0; ccount = 0
    np = int(input('''
Start Rock Paper Scissor game 
1 Begin
2 Exit                                     
'''))    
    if np == 1:
        for a in range (1, bn):
                ui = int(input('''
1 paper 
2 rock
3 scissor
'''))
                if ui == 1:
                    uselects = "paper"
                elif ui == 2:
                    uselects = "rock"
                elif ui == 3:
                    uselects = "scissor"         
                cselects = rd.choice(l)
                if uselects == cselects:
                    print("User selects : ", uselects) 
                    print("Computer selects : ", cselects)   
                    print("Match Draw") 
                    ucount = ucount + 1
                    ccount = ccount + 1
                elif(uselects == "rock" and cselects == "scissor") or (uselects == "paper" and cselects == "rock") or (uselects == "scissor" and cselects == "paper"):
                    print("User selects : ", uselects) 
                    print("Computer selects : ", cselects)   
                    print("User won the round") 
                    ucount = ucount + 1
                else:
                    print("User selects : ", uselects) 
                    print("Computer selects : ", cselects)   
                    print("Computer won the round") 
                    ccount = ccount + 1
        if ucount == ccount:
            print("\nFinaL Game Draw............")
            print("No of rounds won by user : ", ucount)
            print("No of rounds won by computer : ", ccount)
        elif ucount > ccount:
            print("\nCongratulations! User won the final game ............")
            print("No of rounds won by user : ", ucount)
            print("No of rounds won by computer : ", ccount)
        else:
            print("\nComputer won the final game ............")
            print("No of rounds won by user : ", ucount)
            print("No of rounds won by computer : ", ccount)    

    else:
        break

