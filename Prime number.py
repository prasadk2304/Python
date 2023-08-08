flag = False

n=int(input("Enter a positive integer : "))

if n == 1 or n == 0:
    print(n, "is not a prime number")
elif (n > 1) : 
    for a in range (2, n):
        if (n % a) == 0:
            flag = True
        break

if flag:
    print(n, "is not a prime number")
else:
     print(n, "is a prime number")  
