# we give variable and expresion in 
# single line by storing them in a variable (add is storing)
# it is called ananymous fun
add = lambda x,y: x+y
r = add(8,6)
print(r)

square = lambda a: a**2
s= square(4)
print(s)
# 2 variables in differ places
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
