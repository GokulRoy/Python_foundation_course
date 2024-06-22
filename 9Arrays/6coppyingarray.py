from numpy import *
a1 = array([1,5,3,8,3,9])
a2 =array([0,97,34,151,1585,12])
# adding num to array elements
a3 = a1 + 5
print(a3)
# adding 2 array
print (a1 + a2)
print(log(a1))
print(sum(a1))
print(max(a1))
print(min(a1))
# concatinating
print(concatenate([a1,a2]))
# coppying with same address
# values also changed
a5 = a1
a1[0] = 0
print(a1)
print(a5)
print(id(a1))
print(id(a5))
print(id(a2))
# coppying by differnt adress (shallow copy)
a4 = a1.view()
a1[2] = 10
print(a1)
print(a4)
print(id(a1))
print(id(a4))
# (deep copy) it wont change coppied elementa
a6 = a1.copy()
a1[1] = 23
print(a1)
print(a6)
print(id(a1))
print(id(a6))