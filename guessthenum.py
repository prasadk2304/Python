import random as rd

print("Guess the number game")

n=int(input("Enter a number : "))

rt = rd.randint(1, 1)

if n == rt:
    print("Number chose by computer is : ", rt)
    print("you won")
else : 
    print("Number chose by computer is : ", rt)
    print("you lost")