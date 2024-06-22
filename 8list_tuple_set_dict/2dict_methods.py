d = {1:"A", 2:"B"}
print(d)
# adding a element
d[3] = "C"
print(d)
# get() method (fo getting keys or values)
print(d.get(1))
# pop() (method for removing)
print(d.pop(2)) #first it prints 2 value 
print(d) # now it print d value
# values() method ( it values of the d ex : A , B)
print(d.values())
# keys() method (it prints keys of the d)
print(d.keys())
# items() all items 
print(d.items())
# to copy
a = d.copy()
print(a)

m = dict(a)
print(m)