import random as rd

print("Guess the color game\n")

ls = ["red", "black", "yellow", "white", "orange", "green", "blue", "indigo", "violet", "purple", "pink", "silver", "gold", "brown", "gray" ]
cc=rd.choice(ls)

n = str(input("Enter your favourite color : "))

if n == cc:
    print("Congratulation!, you won.......")
else:
    print("Color chose by computyeller : ", cc)
    print("You lost..... Better luch next time")