from numpy import *
arr1 = array([
    [1,2,3],
    [4,5,6]
])
arra = array([
    [1,2,3,8,6,26],
    [4,5,6,6,2,6]
])
# matrix format but it is array
# to print the array type 1x1 r 1x2 r 2x2 r 2x3
print(arr1.shape)
print(arr1.size)
# to make 1 d array
arr2 = arr1.flatten()
print(arr2)
# to make 3x 4 r to make array dimenton
arr3 = arr2.reshape(3,2)
print(arr3)
#no of array(2) and shape of array(2x3)
print(arra.reshape(2,2,3))
# matrix
m1 = matrix('1,2,3;6,4,5;6,7,8')
m2 = matrix('1,2,3;6,4,5;6,7,8')
print(m1)
print(m1.max())
print(m2.sum())
# mul matrix
m3 = m1*m2
print(m3)
# sum matrix
m4 = m1 + m2
print(m4)