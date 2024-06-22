# to copy from one array to another
from array import*
vals = array('i',[5,3,6,8,4,1])
newarr = array(vals.typecode, (a for a in vals))
print(vals)
print(newarr)
# looping will print only numbers
for a in newarr:
    print(a)