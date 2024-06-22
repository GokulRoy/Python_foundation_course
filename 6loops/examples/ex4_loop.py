# print even numbers from 1 to n using for
n = int(input("N="))
for i in range(1,(n+1)):
    if i%2 == 0:
        print(i)
        i+=1

# print even numbers from 1 to n using while

j=1
while j<=n:
    if j%2 == 0:
         print(j)
    j+=1   
