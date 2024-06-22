# we give input in string 10,20,30,20,40,10,50
inp = input().split(',') # we first split by comma
# here we converted in list by using elements
l = [int(item) for item in inp]
newL = []
for i in l:
    if i in newL:
        continue
    else:
        newL.append(i)
print(newL)

# method 2
a = input().split(',')
l2 = [int(b) for b in inp]
# coverting the list in s because the set deletes 
# duplicate values automatically
s = set (l2)
# after deletion we again covert into 
newL2 = list(s)
print(newL2)
