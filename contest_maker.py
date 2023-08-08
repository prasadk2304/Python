import random as rd 

print("Welcome to Lucky Pot")

n = int(input('''
Enter your ticket number 

There are only 100 tickets for this contest
numbering from 1 to 100 :
'''
))
rt = rd.randint(1, 2)
if n > 100:
    print("Invalid ticket number")
elif n == rt:
    print("Contest winner ticket number is : ", rt)
    print("Congratulations ! ..... You won the contest")
else :
    print("Contest winner ticket number is : ", rt)
    print("Bad luck .... You lost the contest")