# calculate the sum of N natural numbers 
n = int(input("enter the first positive numbers: "))
sum = 0
for i in range(1,(n+1)):
    sum += i
print(f"Summ of first {n} natural numbers: {sum}")


x=int(input())
j=1
s=0
while j<=x:
    s+=j
    j+=1
print(s)