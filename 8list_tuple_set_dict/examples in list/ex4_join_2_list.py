a = [10,20,30,40,50]
b = [90,80,70,60]
# joining list method 1
print(a+b)
# joining list method 2
for i in b:
    a.append(i)

print(a)

 # joining list method 2
x = [10,20,30,40,50]
y = [90,80,70,60]
x.extend(y)
print(x)
n = x.index(50)
print(n)
m = x[4]
print(m)
x.pop(4)
print(x)
