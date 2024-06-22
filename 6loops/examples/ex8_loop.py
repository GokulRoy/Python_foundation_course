# factorial of a number
n = int(input("N="))
fac=1
while n >= 1:
    fac=fac*n
    n -= 1
print(f"Factorial of {n}:{fac}")