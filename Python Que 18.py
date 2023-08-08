#18. Write a Python program to calculate the sum of three given numbers. 
#If the values are equal, return three times their sum.

x=eval(input("Enter value of x : "))
y=eval(input("Enter value of y : "))
z=eval(input("Enter value of z : "))

if (x==y==z):
    print((x+y+z)*3)
else:
    print(x+y+z)    