# print odd numbers from 1 to x 
x = int(input("X="))
for j in range(0,(x)):
    if j%2 == 0:
        j+=1
        print(j)
i=1
while i<=x:
    if not(i%2 == 0):
         print(i)
    i+=1   
