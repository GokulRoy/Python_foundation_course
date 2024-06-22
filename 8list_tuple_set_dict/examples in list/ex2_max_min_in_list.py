l= [15,2,60,52,20]

maxi = l[0]
mini = l[0]

for i in l:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print(maxi,mini)


# method 2
a= [15,2,60,52,20]
# we will sort the list by its values
a.sort()
length = len(a)
print(a[length-1], a[0])
print(a.index(60))