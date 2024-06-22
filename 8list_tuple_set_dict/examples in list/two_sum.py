a = input().split(',')
t = int(input("enter the target value:"))
l = [int(b) for b in a]
print(l)
for i in l:
    for j in l:
        if i+j == t:
            print(i,j)
print(a.index(i),a.index(j))
 # method 2
# y = [5,7,10,20]
# t1 = 12
# diff1 = 0
# for x in y:
#     diff1 = t1 - x

