# * is used to import all funtion in the library
from array import *
val = array('i',[5,2,4,6,1])
print(val)
# to ptint location and lrngth
print(val.buffer_info())
for a in val:
    print(a)
# to reverse the numbers
val1 = array('i',[5,2,4,6,1])
val1.reverse()
print(val1)
for i in range(5):
    print(val1[i])
val3 = array('u',['d','f','t','s'])
