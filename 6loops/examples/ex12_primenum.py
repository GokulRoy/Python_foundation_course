# method 1
num = int(input("enter the num:"))
for i in range(2,num):
    if num % i == 0:
        print("not prime")
        break
    else:
        print("prime")
        break



# method 2
n = int(input("enter the num:"))
for i in range(2,n):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")
    